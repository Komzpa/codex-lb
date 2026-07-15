"""merge live queue-latency and oauth device-flow heads

Revision ID: 20260716_010000_merge_live_queue_latency_and_oauth_device_heads
Revises:
- 20260715_060000_merge_queue_latency_and_live_heads
- 20260716_000000_add_oauth_device_flow_slots
Create Date: 2026-07-16 01:00:00.000000
"""

from __future__ import annotations

revision = "20260716_010000_merge_live_queue_latency_and_oauth_device_heads"
down_revision = (
    "20260715_060000_merge_queue_latency_and_live_heads",
    "20260716_000000_add_oauth_device_flow_slots",
)
branch_labels = None
depends_on = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
