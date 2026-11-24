<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/banner-dark.svg">
  <img src="assets/banner-light.svg" width="100%" alt="Freesialuo：出了问题也能继续工作的软件">
</picture>

[English](README.md) · **简体中文**

你好，我是 Freesialuo，北美高校的大三学生。

我做的是出了问题也必须继续工作的软件：用 Rust 和 Go 写自托管服务，用 C# 写游戏里的飞行辅助模组。

可接受带薪工作，具备合法的本地工作身份。联系邮箱：[freesiaxstar@gmail.com](mailto:freesiaxstar@gmail.com)。

<!-- numbers:start -->
过去 12 个月：**1,253** 次贡献 · **572** 次提交 · **145** 个 PR · 更新于 2026-11-24
<!-- numbers:end -->

## 做了什么

<table>
<tr>
<td width="30%" valign="top">

**[CalRelay](https://github.com/freesialuo/CalRelay)**

`Rust` `SQLite` `TypeScript` `Docker`

</td>
<td valign="top">

自托管的日历中枢。接入 ICS 订阅和通过接口推送的事件，输出合并后的日历订阅，并从持久化队列发送提醒。

400 多次提交，经 100 多个 PR 合并，全部要先通过必需的 CI 门禁。有 400 多个 Rust 测试、Kani 有界证明，以及在投递过程中强杀真实服务进程的系统测试。

</td>
</tr>
<tr>
<td width="30%" valign="top">

**[Kairos](https://github.com/freesialuo/kairos)**

`Rust` `WebAssembly` `Cloudflare Workers` `Leptos`

</td>
<td valign="top">

运行在 Cloudflare Workers 上的单用户日历与提醒应用。事件开始前自己醒来，空闲时不占资源。Worker、Durable Object 和浏览器端全部用 Rust 编写。

通行密钥登录，WebAuthn 校验为自行实现。原生、WebAssembly 两套测试之外，还用真实 Chrome 和虚拟通行密钥做端到端验证。

</td>
</tr>
<tr>
<td width="30%" valign="top">

**[Mayday Landing Assist](https://github.com/freesialuo/mayday-landing-assist)**

`C#` `Python` `JAX` `MelonLoader`

</td>
<td valign="top">

游戏 Mayday Airways 的进近与着陆辅助模组。可以只给手飞提示，也可以接管五边，完成拉平、接地和滑跑。玩家一动杆就立刻交还操纵。

控制器由一条可解释的制导律加一个有界的学习修正量组成，在 JAX 写的飞行物理孪生里训练，孪生用实机录制数据校对。

</td>
</tr>
<tr>
<td width="30%" valign="top">

**[DCPortal](https://github.com/freesialuo/dcPortal)**

`Go` `SQLite` `OAuth2` `Docker`

</td>
<td valign="top">

面向私有 Discord Bot 的授权安装门户。用带令牌的入口、安装记录和按服务器生效的黑名单，取代公开的 OAuth2 安装链接。

管理后台里的密钥只能写入，不能读出。80 多个 Go 测试覆盖 OAuth2 流程、存储层和页面。提供公开的容器镜像。

</td>
</tr>
<tr>
<td width="30%" valign="top">

**[88code Reset](https://github.com/Vulpecula-Studio/88code_reset)**

`Go` `Docker` `GitHub Actions`

</td>
<td valign="top">

命令行工具兼 Docker 服务，曾用于按计划重置 88code 上按月计费的订阅额度，支持单个或多个账号。88code 现已停止服务，仓库作为小型定时服务的样例保留。

我 Star 最多的项目：18 个 Star、6 个 fork、10 个发布版本，提供可执行文件和公开的容器镜像。

</td>
</tr>
<tr>
<td width="30%" valign="top">

**[longstitch-go](https://github.com/freesialuo/longstitch-go)**

`Go` `Fyne`

</td>
<td valign="top">

把多张图片拼成一张长图的桌面小工具，带尺寸保护，避免输出过大耗尽内存。

CI 在 Linux、macOS 和 Windows 上运行测试。打标签后自动构建 macOS 和 Windows 版本。

</td>
</tr>
</table>

## 能做什么

- **为故障而设计。** CalRelay 的系统测试会[强杀并重启服务](https://github.com/freesialuo/CalRelay/pull/203)、[让上游订阅停滞](https://github.com/freesialuo/CalRelay/pull/207)、[锁住数据库](https://github.com/freesialuo/CalRelay/pull/217)，并检查已投递的提醒不会重发、[被中断的提醒最终送达](https://github.com/freesialuo/CalRelay/pull/211)。
- **证明测试覆盖不到的地方。** 用 [Kani 做有界模型检查](https://github.com/freesialuo/CalRelay/blob/main/docs/formal-verification.md)，覆盖重复事件的预算和时间窗口，并通过改动代码确认每个证明确实会失败。
- **先建模，再控制。** Landing Assist 把控制权限放在学习模型之外。网络缺失或行为异常时，退回到一条能独立飞完进近的制导律。详见[设计说明](https://github.com/freesialuo/mayday-landing-assist/blob/main/README.zh-CN.md#设计要点)。
- **把安全做进设计里。** Kairos 的[通行密钥不依赖第三方认证服务](https://github.com/freesialuo/kairos/blob/main/docs/2026-11-18-rust-architecture.md)；CalRelay 的[凭据加密存储并支持密钥轮换](https://github.com/freesialuo/CalRelay/blob/main/docs/credential-security.md)，[对外请求有防护](https://github.com/freesialuo/CalRelay/blob/main/docs/remote-fetch.md)；DCPortal 的密钥只写不读。
- **交付。** 容器镜像、多平台的发布版可执行文件，以及每个 PR 都运行的 CI。
- **管理流程，而不只是写代码。** 我对 CalRelay 的每个改动都从 Issue 开始，经过分支、PR、必需的 CI 门禁和我本人的明确批准。我让 AI 编程代理遵守[同一套规则](https://github.com/freesialuo/CalRelay/blob/main/AGENTS.md)。

## 接下来做什么

- 完成 CalRelay 首个版本的验收工作。
- 用实机录制数据校准 Landing Assist 的飞行孪生。
- 寻找带薪工作：实习、兼职或合同均可。后端服务、基础设施和开发者工具是我最擅长的方向。

## 工具箱

- **语言：** Rust、Go、C#、TypeScript、Python
- **平台与数据：** Cloudflare Workers 与 Durable Objects、Docker、SQLite、GitHub Actions、WebAssembly
- **工程实践：** 测试先行、系统与故障测试、有界模型检查、硬件密钥签名提交
