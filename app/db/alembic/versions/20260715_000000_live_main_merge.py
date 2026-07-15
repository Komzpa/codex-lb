"""merge deployed security-lineage and current main migration heads

Revision ID: 20260715_000000_live_main_merge
Revises:
- 20260712_000000_merge_warmup_and_security_lineage_heads
- 20260713_020000_add_model_registry_snapshot
Create Date: 2026-07-15 00:00:00.000000
"""

from __future__ import annotations

revision = "20260715_000000_live_main_merge"
down_revision = (
    "20260712_000000_merge_warmup_and_security_lineage_heads",
    "20260713_020000_add_model_registry_snapshot",
)
branch_labels = None
depends_on = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
