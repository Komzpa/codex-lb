# Docker

## Basic run

```bash
docker volume create codex-lb-data
docker network inspect codex-lb-net >/dev/null 2>&1 || docker network create codex-lb-net
docker run -d --name codex-lb \
  --network codex-lb-net \
  -p 2455:2455 -p 1455:1455 \
  -v codex-lb-data:/var/lib/codex-lb \
  ghcr.io/soju06/codex-lb:latest
```

Ports:

- `2455` — dashboard + proxy API
- `1455` — OAuth login callback (needed while adding accounts)

The volume holds everything under `/var/lib/codex-lb/` (database, encryption key, archives) — back it up to preserve your data.

## Docker Compose

For a production-shaped Compose setup (watchtower-friendly tags, external PostgreSQL via env), start from
[`docker-compose.prod.yml`](https://github.com/Soju06/codex-lb/blob/main/docker-compose.prod.yml) — it defines
only the `server` service. The optional `postgres` / `postgres-upgrade` profiles live in the root
[`docker-compose.yml`](https://github.com/Soju06/codex-lb/blob/main/docker-compose.yml) (see [Database](../database.md)):

```bash
cp .env.example .env.local   # required: the compose file references .env.local via env_file — an unedited copy still runs with zero config
docker compose -f docker-compose.prod.yml up -d
```

For PostgreSQL profiles and the Postgres 16 → 18 upgrade runbook, see [Database](../database.md).

## Switching Wi-Fi, hotspots, or VPNs

When a laptop switches from one Wi-Fi network to another—for example, from
home Wi-Fi to a phone hotspot—or when a VPN connects or disconnects, existing
connections may briefly break. Docker can also keep using stale DNS settings:
it may retain a DNS server from the previous network.
If Docker's resolver is stale, codex-lb may report upstream timeouts even though the host browser works.

The portable commands on this page use a user-defined bridge. Its embedded
resolver at `127.0.0.11` avoids placing one Wi-Fi DNS address directly in the
container, but it does not guarantee that Docker refreshes its external
forwarders after a network switch. codex-lb retries only when the transport can
prove that a request failed before it was sent, so it avoids both duplicate
responses and poisoning an individual account's health for a host-wide DNS
problem. The application cannot repair Docker's stale forwarding state.

For laptops that switch networks frequently:

- **Simplest on Linux, macOS, and Windows:** run `uvx codex-lb` directly on the
  host, avoiding Docker's extra DNS layer.
- **Docker Engine on Linux (verified with `systemd-resolved`):** use host
  networking so the container shares a stable resolver address such as the
  `127.0.0.53` stub. If `/etc/resolv.conf` points directly to a DNS server
  supplied by Wi-Fi or other DHCP, that address can still become stale. First
  configure a stable local resolver, use the
  [bridge-listener runbook](https://github.com/Soju06/codex-lb/blob/main/openspec/specs/deployment-networking/context.md#diagnostics-and-recovery),
  or prefer `uvx`.
- **Docker Desktop on macOS or Windows:** Docker Desktop 4.34 and later offers
  opt-in host networking, but its VM-backed implementation differs.
  This setup has not been verified as a reliable fix for DNS recovery after switching networks.

For the verified Linux Docker Engine setup, use this command instead of a
portable bridge command:

```bash
docker volume create codex-lb-data
docker run -d --name codex-lb \
  --network host \
  -v codex-lb-data:/var/lib/codex-lb \
  ghcr.io/soju06/codex-lb:latest
```

Host networking does not use `-p`; codex-lb still listens on ports 2455 and
1455. It also removes Docker's network-namespace isolation. The command is an
opt-in path to a stable host resolver, not a DNS fix by itself.

## Auth mode examples

**Authelia / trusted header**

```bash
docker network inspect codex-lb-net >/dev/null 2>&1 || docker network create codex-lb-net
docker run -d --name codex-lb \
  --network codex-lb-net \
  -p 2455:2455 -p 1455:1455 \
  -e CODEX_LB_DASHBOARD_AUTH_MODE=trusted_header \
  -e CODEX_LB_DASHBOARD_AUTH_PROXY_HEADER=Remote-User \
  -e CODEX_LB_FIREWALL_TRUST_PROXY_HEADERS=true \
  -e CODEX_LB_FIREWALL_TRUSTED_PROXY_CIDRS=172.18.0.0/16 \
  -v codex-lb-data:/var/lib/codex-lb \
  ghcr.io/soju06/codex-lb:latest
```

**Hard override / no app-level dashboard auth**

```bash
docker network inspect codex-lb-net >/dev/null 2>&1 || docker network create codex-lb-net
docker run -d --name codex-lb \
  --network codex-lb-net \
  -p 2455:2455 -p 1455:1455 \
  -e CODEX_LB_DASHBOARD_AUTH_MODE=disabled \
  -v codex-lb-data:/var/lib/codex-lb \
  ghcr.io/soju06/codex-lb:latest
```

For Helm, pass the same values through `extraEnv`. What these modes mean and when to use them is covered in [Authentication](../authentication.md).

---

*Specs: [deployment-installation](https://github.com/Soju06/codex-lb/tree/main/openspec/specs/deployment-installation) · [deployment-networking](https://github.com/Soju06/codex-lb/tree/main/openspec/specs/deployment-networking)*
