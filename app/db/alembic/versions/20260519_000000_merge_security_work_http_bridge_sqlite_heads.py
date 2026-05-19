"""merge security work, HTTP bridge, and sqlite recovery heads

Revision ID: 20260519_000000_merge_security_work_http_bridge_sqlite_heads
Revises: 20260518_010000_merge_http_bridge_and_sqlite_recovery_heads,
    20260518_010000_merge_security_work_and_http_bridge_heads
Create Date: 2026-05-19
"""

from __future__ import annotations

revision = "20260519_000000_merge_security_work_http_bridge_sqlite_heads"
down_revision = (
    "20260518_010000_merge_http_bridge_and_sqlite_recovery_heads",
    "20260518_010000_merge_security_work_and_http_bridge_heads",
)
branch_labels = None
depends_on = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
