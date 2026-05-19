"""merge opportunistic traffic class with full stack heads

Revision ID: 20260520_000000_merge_opportunistic_full_stack_heads
Revises: 20260515_030000_merge_traffic_class_and_split_sticky_heads,
    20260518_010000_merge_sticky_thresholds_and_http_bridge_heads,
    20260519_000000_merge_routing_policy_http_bridge_sqlite_heads,
    20260519_000000_merge_security_work_http_bridge_sqlite_heads
Create Date: 2026-05-20
"""

from __future__ import annotations

revision = "20260520_000000_merge_opportunistic_full_stack_heads"
down_revision = (
    "20260515_030000_merge_traffic_class_and_split_sticky_heads",
    "20260518_010000_merge_sticky_thresholds_and_http_bridge_heads",
    "20260519_000000_merge_routing_policy_http_bridge_sqlite_heads",
    "20260519_000000_merge_security_work_http_bridge_sqlite_heads",
)
branch_labels = None
depends_on = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
