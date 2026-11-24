"""Refresh the activity numbers line in the profile READMEs.

Reads public contribution counts for one GitHub user and rewrites the single
line between the numbers markers in README.md and README.zh-CN.md. When a
number changed, both files go into one commit made through the GitHub API, so
GitHub signs it. When only the date would change, nothing is committed.

Needs the `gh` CLI with a token in GH_TOKEN. Standard library only.
"""

import argparse
import base64
import datetime
import json
import re
import subprocess
import sys
from typing import NamedTuple

MARK_START = "<!-- numbers:start -->"
MARK_END = "<!-- numbers:end -->"
FILES = {"README.md": "en", "README.zh-CN.md": "zh"}
COMMIT_MESSAGE = "chore: refresh activity numbers"

STATS_QUERY = """
query($login: String!) {
  user(login: $login) {
    contributionsCollection {
      totalCommitContributions
      totalPullRequestContributions
      contributionCalendar { totalContributions }
    }
  }
}
"""

COMMIT_MUTATION = """
mutation($input: CreateCommitOnBranchInput!) {
  createCommitOnBranch(input: $input) { commit { oid url } }
}
"""


class Stats(NamedTuple):
    contributions: int
    commits: int
    pull_requests: int


def render_line(stats: Stats, lang: str, as_of: datetime.date) -> str:
    if lang == "zh":
        return (
            f"过去 12 个月：**{stats.contributions:,}** 次贡献 · **{stats.commits:,}** 次提交"
            f" · **{stats.pull_requests:,}** 个 PR · 更新于 {as_of.isoformat()}"
        )
    return (
        f"**{stats.contributions:,}** contributions in the last 12 months"
        f" · **{stats.commits:,}** commits · **{stats.pull_requests:,}** pull requests"
        f" · updated {as_of.isoformat()}"
    )


def _block_span(text: str) -> tuple[int, int]:
    """Return the offsets just after the start marker and at the end marker."""
    if text.count(MARK_START) != 1 or text.count(MARK_END) != 1:
        raise ValueError(f"expected exactly one {MARK_START} and one {MARK_END}")
    start = text.index(MARK_START) + len(MARK_START)
    end = text.index(MARK_END)
    if end < start:
        raise ValueError(f"{MARK_END} comes before {MARK_START}")
    return start, end


def swap_block(text: str, line: str) -> str:
    start, end = _block_span(text)
    newline = "\r\n" if "\r\n" in text else "\n"
    return text[:start] + newline + line + newline + text[end:]


def same_numbers(old: str, new: str) -> bool:
    def block_without_dates(text: str) -> str:
        start, end = _block_span(text)
        return re.sub(r"\d{4}-\d{2}-\d{2}", "", text[start:end]).strip()

    return block_without_dates(old) == block_without_dates(new)


def encode_addition(path: str, text: str) -> dict:
    return {"path": path, "contents": base64.b64encode(text.encode("utf-8")).decode("ascii")}


def graphql(query: str, variables: dict) -> dict:
    result = subprocess.run(
        ["gh", "api", "graphql", "--input", "-"],
        input=json.dumps({"query": query, "variables": variables}).encode("utf-8"),
        capture_output=True,
        check=False,
    )
    if result.returncode != 0:
        raise RuntimeError(result.stderr.decode("utf-8", "replace").strip() or "gh api graphql failed")
    return json.loads(result.stdout.decode("utf-8"))["data"]


def fetch_stats(login: str) -> Stats:
    user = graphql(STATS_QUERY, {"login": login})["user"]
    if user is None:
        raise RuntimeError(f"no such user: {login}")
    collection = user["contributionsCollection"]
    return Stats(
        contributions=collection["contributionCalendar"]["totalContributions"],
        commits=collection["totalCommitContributions"],
        pull_requests=collection["totalPullRequestContributions"],
    )


def read_text(path: str) -> str:
    with open(path, encoding="utf-8", newline="") as handle:
        return handle.read()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--login", required=True, help="GitHub user whose numbers to show")
    parser.add_argument("--repo", required=True, help="owner/name of the profile repository")
    parser.add_argument("--branch", required=True, help="branch to commit to")
    parser.add_argument("--dry-run", action="store_true", help="print the new lines, commit nothing")
    args = parser.parse_args(argv)

    stats = fetch_stats(args.login)
    today = datetime.datetime.now(datetime.timezone.utc).date()
    additions = []
    changed = False
    for path, lang in FILES.items():
        old = read_text(path)
        new = swap_block(old, render_line(stats, lang, today))
        changed = changed or not same_numbers(old, new)
        additions.append(encode_addition(path, new))
        if args.dry_run:
            sys.stdout.buffer.write(f"{path}: {render_line(stats, lang, today)}\n".encode("utf-8"))

    if args.dry_run:
        return 0
    if not changed:
        print("no change")
        return 0

    head = subprocess.run(
        ["git", "rev-parse", "HEAD"], capture_output=True, check=True, text=True
    ).stdout.strip()
    commit = graphql(
        COMMIT_MUTATION,
        {
            "input": {
                "branch": {"repositoryNameWithOwner": args.repo, "branchName": args.branch},
                "expectedHeadOid": head,
                "message": {"headline": COMMIT_MESSAGE},
                "fileChanges": {"additions": additions},
            }
        },
    )["createCommitOnBranch"]["commit"]
    print(f"committed {commit['oid']} {commit['url']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
