"""merge automation prompt and weekly pace heads

Revision ID: 20260706_000000_merge_automation_prompt_and_weekly_pace_heads
Revises:
- 20260630_050000_add_automation_run_prompt_snapshot
- 20260701_000000_add_weekly_pace_smoothing_minutes
Create Date: 2026-07-06 00:00:00.000000
"""

from __future__ import annotations

revision = "20260706_000000_merge_automation_prompt_and_weekly_pace_heads"
down_revision = (
    "20260630_050000_add_automation_run_prompt_snapshot",
    "20260701_000000_add_weekly_pace_smoothing_minutes",
)
branch_labels = None
depends_on = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
