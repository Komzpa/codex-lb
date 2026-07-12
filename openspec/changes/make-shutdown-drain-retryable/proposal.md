# Make shutdown drain retryable for Codex clients

Single-replica deployments reject new work briefly while the old process drains and the replacement becomes ready. The current generic 503 body gives clients no stable signal or delay hint, so bounded retries can be exhausted before the replacement is reachable.

Return an explicit `server_draining` error code and `Retry-After` header for shutdown-drain rejections. This lets Codex distinguish a planned transient rollout from overload or a terminal service error.
