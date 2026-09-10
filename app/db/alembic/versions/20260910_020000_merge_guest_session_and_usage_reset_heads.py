"""Merge guest-session and reset-recovery migration heads.

Revision ID: 20260910_020000_merge_guest_session_and_usage_reset_heads
Revises: 20260908_000000_add_guest_session_generation,
    20260910_010000_merge_usage_reset_transition_and_request_log_cost_heads
Create Date: 2026-09-10
"""

from __future__ import annotations

from collections.abc import Sequence

# revision identifiers, used by Alembic.
revision: str = "20260910_020000_merge_guest_session_and_usage_reset_heads"
down_revision: tuple[str, str] = (
    "20260908_000000_add_guest_session_generation",
    "20260910_010000_merge_usage_reset_transition_and_request_log_cost_heads",
)
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    """Join revision tracking after both parents complete."""
    pass


def downgrade() -> None:
    """Restore both parent stamps without changing schema or data."""
    pass
