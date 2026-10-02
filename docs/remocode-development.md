# RemocodeBrowser development

## Repository

Fork: `BlueOriginAI/RemocodeBrowser`.
Upstream: `browseros-ai/BrowserOS`.
Local workspace: `/Users/ai/Documents/VibeApp/RemocodeBrowser`.

The `origin` remote is our fork; `upstream` is the source project. Work on local feature branches and send changes to our fork. Do not publish to upstream unless contributing an explicitly scoped change.

## Product mapping

| Build key | Display name | macOS bundle | macOS profile directory |
| --- | --- | --- | --- |
| `browseros` | RemocodeBrowser | `com.remocode.RemocodeBrowser` | RemocodeBrowser |
| `browserclaw` | RemocodeBrowser neo | `com.remocode.RemocodeBrowserNeo` | RemocodeBrowserNeo |

The keys are intentionally retained because the build system, API namespaces, server paths, and Chromium patch payloads use them. User-facing names change without a wholesale rename of those contracts.

## Start with the Agent interface

The main implementation lives in `packages/browseros-agent`:

- `apps/app`: assistant, settings, new tab.
- `apps/claw-app`: agent cockpit and replay UI.
- `apps/server`: TypeScript backend.
- `apps/claw-server-rust`: local MCP/backend for the neo variant.
- `apps/app-onboard` and `apps/claw-onboard`: onboarding.

Read the root `CONTRIBUTING.md` and the relevant app's contributing instructions. The monorepo pins Bun 1.4.2; keep that pin instead of rewriting the lockfile for an older installed Bun.

```sh
cd packages/browseros-agent
bun install --frozen-lockfile
```

Do not launch the existing upstream watch scripts blindly: they currently resolve installed BrowserOS applications and manage ports/profiles. Adapt their app path to our development build first. No existing browser sessions need to be closed for source work.

## Browser build

```sh
cd packages/browseros
uv sync
uv run browseros build --preset debug --product browseros --chromium-src /path/to/chromium/src
```

The full Chromium source and build require roughly 100GB free disk according to upstream. On 2026-10-02 the local disk had about 61GB available, so the full browser build was not started. A ready-to-install RemocodeBrowser binary is not yet available.

macOS branding has a separate bundle and profile name, and the upstream signing team is cleared from branding templates. Configure our signing identity only when preparing our own installer.

## Verification and release boundary

Product descriptors can be checked without downloading Chromium:

```sh
cd packages/browseros
PYTHONPATH=. python3 -m unittest bos_build.products.products_test bos_build.products.doctor_test bos_build.steps.patches.product_user_data_dir_test
```

Before distributing a build, finish the icon set, Windows/Linux profile and installation identities, update/release endpoints, extension signing identities, and cloud/analytics integration review. The extension manifests no longer point at the upstream automatic update feed. Other upstream service URLs remain and are not represented as Remocode-operated services.

Preserve license notices and provide corresponding source as required by AGPL-3.0. There is no separate closed-source license for this fork.
