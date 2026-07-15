"""merge warm-up threshold and security-lineage heads

Revision ID: 20260712_000000_merge_warmup_and_security_lineage_heads
Revises:
- 20260711_030000_add_limit_warmup_idle_threshold
- 20260711_030000_detach_security_lineage_markers
Create Date: 2026-07-12 00:00:00.000000
"""

from __future__ import annotations

revision = "20260712_000000_merge_warmup_and_security_lineage_heads"
down_revision = (
    "20260711_030000_add_limit_warmup_idle_threshold",
    "20260711_030000_detach_security_lineage_markers",
)
branch_labels = None
depends_on = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
