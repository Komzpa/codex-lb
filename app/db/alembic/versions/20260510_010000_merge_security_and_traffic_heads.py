"""merge security authorization and traffic routing heads

Revision ID: 20260510_010000_merge_security_and_traffic_heads
Revises:
    20260425_000000_add_account_security_work_authorized
    20260510_010000_merge_routing_policy_and_traffic_heads
Create Date: 2026-05-10
"""

from __future__ import annotations

revision = "20260510_010000_merge_security_and_traffic_heads"
down_revision = (
    "20260425_000000_add_account_security_work_authorized",
    "20260510_010000_merge_routing_policy_and_traffic_heads",
)
branch_labels = None
depends_on = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
