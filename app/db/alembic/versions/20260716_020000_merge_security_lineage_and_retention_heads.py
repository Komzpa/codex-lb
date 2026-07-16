"""merge retention and live queue/oauth heads

Revision ID: 20260716_020000_merge_security_lineage_and_retention_heads
Revises: 20260716_010000_add_dashboard_retention_settings, 20260716_010000_merge_live_queue_latency_and_oauth_device_heads
Create Date: 2026-07-16 02:00:00.000000
"""

from __future__ import annotations

revision = "20260716_020000_merge_security_lineage_and_retention_heads"
down_revision = (
    "20260716_010000_add_dashboard_retention_settings",
    "20260716_010000_merge_live_queue_latency_and_oauth_device_heads",
)
branch_labels = None
depends_on = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
