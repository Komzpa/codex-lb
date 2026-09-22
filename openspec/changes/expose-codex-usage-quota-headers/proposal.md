# Expose refreshed Codex usage quota headers

Extend the authenticated Codex usage endpoint so its response carries the same
fresh aggregate pool headers emitted on Responses requests. Keep the JSON body
API-key-specific for API-key callers and preserve the configured suppression of
upstream quota data.

