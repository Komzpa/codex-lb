# Authentication

This page covers **dashboard** authentication. For protecting the proxy routes that clients call, see [API Keys](api-keys.md).

## Dashboard authentication modes

`codex-lb` supports three dashboard auth modes via environment variables:

- `CODEX_LB_DASHBOARD_AUTH_MODE=standard` — built-in dashboard password with optional TOTP from the Settings page. This is the default.
- `CODEX_LB_DASHBOARD_AUTH_MODE=trusted_header` — trust a reverse-proxy auth header such as Authelia's `Remote-User`, but only from `CODEX_LB_FIREWALL_TRUSTED_PROXY_CIDRS`. Built-in password/TOTP remain available as an optional fallback, and password/TOTP management still requires a fallback password session.
- `CODEX_LB_DASHBOARD_AUTH_MODE=disabled` — fully bypass dashboard auth. Use only behind network restrictions or external auth. Built-in password/TOTP management is disabled in this mode.

`trusted_header` mode also requires:

```bash
CODEX_LB_FIREWALL_TRUST_PROXY_HEADERS=true
CODEX_LB_FIREWALL_TRUSTED_PROXY_CIDRS=172.18.0.0/16
CODEX_LB_DASHBOARD_AUTH_PROXY_HEADER=Remote-User
```

If the trusted header is missing and no fallback password is configured, the dashboard fails closed and shows a reverse-proxy-required message instead of loading the UI.

Ready-to-run Docker commands for both non-default modes are in [Docker deployment — auth mode examples](deployment/docker.md#auth-mode-examples). For Helm, pass the same values through `extraEnv`.

## Cloudflare Access assertions

`trusted_header` mode can cryptographically verify Cloudflare Access instead of
accepting `Remote-User` as the administrator identity. Keep the trusted-proxy
settings above, then configure the exact Access issuer, one or more application
audiences, and the email domains allowed to administer the dashboard:

```bash
CODEX_LB_DASHBOARD_AUTH_MODE=trusted_header
CODEX_LB_FIREWALL_TRUST_PROXY_HEADERS=true
CODEX_LB_FIREWALL_TRUSTED_PROXY_CIDRS=172.18.0.0/16
CODEX_LB_DASHBOARD_ACCESS_JWT_ISSUER=https://your-team.cloudflareaccess.com
CODEX_LB_DASHBOARD_ACCESS_JWT_AUDIENCES=your-access-application-aud
CODEX_LB_DASHBOARD_ACCESS_ALLOWED_EMAIL_DOMAINS=example.com
CODEX_LB_DASHBOARD_ACCESS_JWT_REQUIRED=true
```

Audience and domain settings accept comma-separated lists. Assertions are read
from `Cf-Access-Jwt-Assertion` by default; use
`CODEX_LB_DASHBOARD_ACCESS_JWT_HEADER` only if the proxy sends a different
header. The server fetches the issuer's Access JWKS and verifies the RS256
signature, exact issuer, audience, expiry, and email domain. It removes both the
assertion and `Remote-User` before dispatch and derives the dashboard actor only
from the validated email claim.

`CODEX_LB_DASHBOARD_ACCESS_JWT_REQUIRED=true` fails closed for protected
requests when the assertion is missing, invalid, expired, or cannot be verified.
Read-only health and drain-status probes remain available for orchestration.
Without `REQUIRED=true`, a configured valid assertion is still verified and
used, while requests without a valid assertion can continue only through the
built-in password fallback. Partial Access configuration, or Access settings in
`standard`/`disabled` mode, are rejected at startup.

## First-time remote access

Setting the initial dashboard password from a remote machine requires a one-time bootstrap token — see [Getting Started](getting-started.md#remote-setup-bootstrap-token).

---

*Specs: [admin-auth](https://github.com/Soju06/codex-lb/tree/main/openspec/specs/admin-auth) · [api-firewall](https://github.com/Soju06/codex-lb/tree/main/openspec/specs/api-firewall)*
