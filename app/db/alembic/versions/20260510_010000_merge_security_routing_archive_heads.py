"""merge live-stack security, routing, and archive heads

Revision ID: 20260510_010000_merge_security_routing_archive_heads
Revises:
    20260510_010000_merge_security_and_traffic_heads
    20260510_000000_add_request_log_slim_summary
Create Date: 2026-05-12
"""

from __future__ import annotations

revision = "20260510_010000_merge_security_routing_archive_heads"
down_revision = (
    "20260510_010000_merge_security_and_traffic_heads",
    "20260510_000000_add_request_log_slim_summary",
)
branch_labels = None
depends_on = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
