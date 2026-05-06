import { render, screen } from "@testing-library/react";
import { describe, expect, it, vi } from "vitest";

import { AccountListItem } from "@/features/accounts/components/account-list-item";
import { createAccountSummary } from "@/test/mocks/factories";

describe("AccountListItem", () => {
  it("renders neutral quota track when secondary remaining percent is unknown", () => {
    const account = createAccountSummary({
      usage: {
        primaryRemainingPercent: 82,
        secondaryRemainingPercent: null,
      },
    });

    render(<AccountListItem account={account} selected={false} onSelect={vi.fn()} />);

    expect(screen.getByTestId("mini-quota-track")).toHaveClass("bg-muted");
    expect(screen.queryByTestId("mini-quota-fill")).not.toBeInTheDocument();
  });

  it("renders quota fill when secondary remaining percent is available", () => {
    const account = createAccountSummary({
      usage: {
        primaryRemainingPercent: 82,
        secondaryRemainingPercent: 73,
      },
    });

    render(<AccountListItem account={account} selected={false} onSelect={vi.fn()} />);

    expect(screen.getByTestId("mini-quota-fill")).toHaveStyle({ width: "73%" });
  });

  it("marks burn-first accounts in the list", () => {
    const account = createAccountSummary({ routingPolicy: "burn_first" });

    render(<AccountListItem account={account} selected={false} onSelect={vi.fn()} />);

    expect(screen.getByText("Burn first")).toBeInTheDocument();
  });

  it("marks preserved accounts in the list", () => {
    const account = createAccountSummary({ routingPolicy: "preserve" });

    render(<AccountListItem account={account} selected={false} onSelect={vi.fn()} />);

    expect(screen.getByText("Preserve")).toBeInTheDocument();
  });

  it("marks normal accounts in the list", () => {
    const account = createAccountSummary({ routingPolicy: "normal" });

    render(<AccountListItem account={account} selected={false} onSelect={vi.fn()} />);

    expect(screen.getByText("Normal")).toBeInTheDocument();
  });
});
