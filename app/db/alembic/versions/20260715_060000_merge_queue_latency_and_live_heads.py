"""merge request-log queue latency and live aggregate heads

Revision ID: 20260715_060000_merge_queue_latency_and_live_heads
Revises:
- 20260715_000000_add_request_log_queue_latency
- 20260715_050000_merge_live_main_and_refresh_claim_heads
Create Date: 2026-07-15 06:00:00.000000
"""

from __future__ import annotations

revision = "20260715_060000_merge_queue_latency_and_live_heads"
down_revision = (
    "20260715_000000_add_request_log_queue_latency",
    "20260715_050000_merge_live_main_and_refresh_claim_heads",
)
branch_labels = None
depends_on = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
