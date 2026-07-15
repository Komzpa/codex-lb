"""merge live main and account refresh claim migration heads

Revision ID: 20260715_050000_merge_live_main_and_refresh_claim_heads
Revises:
- 20260715_000000_live_main_merge
- 20260713_040000_add_account_refresh_claims
Create Date: 2026-07-15 05:00:00.000000
"""

from __future__ import annotations

revision = "20260715_050000_merge_live_main_and_refresh_claim_heads"
down_revision = (
    "20260715_000000_live_main_merge",
    "20260713_040000_add_account_refresh_claims",
)
branch_labels = None
depends_on = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
