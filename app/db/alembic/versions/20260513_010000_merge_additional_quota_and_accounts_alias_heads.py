"""merge additional quota routing and accounts alias heads

Revision ID: 20260513_010000_merge_additional_quota_and_accounts_alias_heads
Revises: 20260509_010000_add_additional_quota_routing_policies, 20260513_000000_add_accounts_alias
Create Date: 2026-05-13
"""

from __future__ import annotations

revision = "20260513_010000_merge_additional_quota_and_accounts_alias_heads"
down_revision = (
    "20260509_010000_add_additional_quota_routing_policies",
    "20260513_000000_add_accounts_alias",
)
branch_labels = None
depends_on = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
