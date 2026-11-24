<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/banner-dark.svg">
  <img src="assets/banner-light.svg" width="100%" alt="CosmoDz: software that keeps working when things go wrong">
</picture>

**English** · [简体中文](README.zh-CN.md)

Hi, I'm CosmoDz, a third-year university student in North America.

I build software that has to keep working when things go wrong: self-hosted services in Rust and Go, and flight-assist mods for games in C#.

Open to paid work. Authorized to work locally. Reach me at [freesiaxstar@gmail.com](mailto:freesiaxstar@gmail.com).

<!-- numbers:start -->
**1,253** contributions in the last 12 months · **572** commits · **145** pull requests · updated 2026-11-24
<!-- numbers:end -->

## What I've built

<table>
<tr>
<td width="30%" valign="top">

**[CalRelay](https://github.com/freesialuo/CalRelay)**

`Rust` `SQLite` `TypeScript` `Docker`

</td>
<td valign="top">

A self-hosted calendar hub. It takes in ICS feeds and events pushed over an API, publishes merged calendar subscriptions, and sends reminders from a durable queue.

400+ commits through 100+ merged pull requests, all behind a required CI gate. More than 400 Rust tests, bounded proofs with Kani, and system tests that kill the real server in the middle of a delivery.

</td>
</tr>
<tr>
<td width="30%" valign="top">

**[Kairos](https://github.com/freesialuo/kairos)**

`Rust` `WebAssembly` `Cloudflare Workers` `Leptos`

</td>
<td valign="top">

A single-user calendar and reminder app on Cloudflare Workers that wakes itself before an event and sleeps when idle. The Worker, the Durable Object and the browser app are all Rust.

Passkey sign-in with WebAuthn verification written in-house. Tested natively, under WebAssembly, and end to end in real Chrome with a virtual passkey.

</td>
</tr>
<tr>
<td width="30%" valign="top">

**[Mayday Landing Assist](https://github.com/freesialuo/mayday-landing-assist)**

`C#` `Python` `JAX` `MelonLoader`

</td>
<td valign="top">

An approach and landing assistant mod for the game Mayday Airways. It shows hand-flying cues, or flies the final approach through flare, touchdown and rollout, and gives control back on any stick input.

The controller is a readable guidance law plus a bounded learned correction. It is trained in a JAX twin of the flight physics that is checked against in-game recordings.

</td>
</tr>
<tr>
<td width="30%" valign="top">

**[DCPortal](https://github.com/freesialuo/dcPortal)**

`Go` `SQLite` `OAuth2` `Docker`

</td>
<td valign="top">

A gated install portal for private Discord bots. It replaces a public OAuth2 install link with token-protected entry, install records, and a per-server blacklist.

Secrets are write-only in the admin console. 80+ Go tests cover the OAuth2 flow, the store and the pages. Ships as a public container image.

</td>
</tr>
<tr>
<td width="30%" valign="top">

**[88code Reset](https://github.com/Vulpecula-Studio/88code_reset)**

`Go` `Docker` `GitHub Actions`

</td>
<td valign="top">

A command-line tool and Docker service that resets monthly subscription quotas on 88code on a schedule, for one account or many.

My most starred project: 18 stars, 6 forks and 10 releases, with binaries and a public container image.

</td>
</tr>
<tr>
<td width="30%" valign="top">

**[longstitch-go](https://github.com/freesialuo/longstitch-go)**

`Go` `Fyne`

</td>
<td valign="top">

A small desktop app that stitches several images into one long picture, with a size guard so a huge output cannot exhaust memory.

Tested on Linux, macOS and Windows in CI. Tagged releases build the macOS and Windows apps automatically.

</td>
</tr>
</table>

## What I can do

- **Design for failure.** CalRelay's system tests [kill and restart the server](https://github.com/freesialuo/CalRelay/pull/203), [stall an upstream feed](https://github.com/freesialuo/CalRelay/pull/207) and [lock the database](https://github.com/freesialuo/CalRelay/pull/217). They check that delivered reminders are not sent twice and that [interrupted ones still arrive](https://github.com/freesialuo/CalRelay/pull/211).
- **Prove what tests cannot.** I use [bounded model checking with Kani](https://github.com/freesialuo/CalRelay/blob/main/docs/formal-verification.md) for recurrence budgets and time windows, and I mutate the code to confirm each proof can fail.
- **Model a system before controlling it.** Landing Assist keeps control authority outside the learned model, so a missing or misbehaving network falls back to a guidance law that can fly the approach alone. The [design notes](https://github.com/freesialuo/mayday-landing-assist#design-notes) explain how.
- **Build security in.** [Passkeys with no third-party auth service](https://github.com/freesialuo/kairos/blob/main/docs/2026-11-18-rust-architecture.md) in Kairos, [encrypted credentials with key rotation](https://github.com/freesialuo/CalRelay/blob/main/docs/credential-security.md) and [guarded outbound requests](https://github.com/freesialuo/CalRelay/blob/main/docs/remote-fetch.md) in CalRelay, write-only secrets in DCPortal.
- **Ship.** Container images, release binaries for several platforms, and CI that runs on every pull request.
- **Run a process, not only write code.** Every change I make to CalRelay goes from an issue to a branch, a pull request, a required CI gate and my explicit sign-off. I hold AI coding agents to the [same rules](https://github.com/freesialuo/CalRelay/blob/main/AGENTS.md).

## What I'm doing next

- Finishing the first-release acceptance work for CalRelay.
- Calibrating the Landing Assist flight twin with recorded in-game data.
- Looking for paid work: an internship, part-time or contract. Backend services, infrastructure and developer tooling are where I am strongest.

## Toolbox

- **Languages:** Rust, Go, C#, TypeScript, Python
- **Platforms and data:** Cloudflare Workers and Durable Objects, Docker, SQLite, GitHub Actions, WebAssembly
- **Practices:** test-first development, system and failure testing, bounded model checking, hardware-key commit signing
