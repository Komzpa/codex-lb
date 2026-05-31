import { beforeEach, describe, expect, it, vi, type Mock } from "vitest";

import { getAuthSession } from "@/features/auth/api";

let registeredUnauthorizedHandler: (() => void) | null = null;

vi.mock("@/features/auth/api", () => ({
  getAuthSession: vi.fn(),
  loginPassword: vi.fn(),
  logout: vi.fn(),
  verifyTotp: vi.fn(),
}));

vi.mock("@/lib/api-client", () => ({
  setUnauthorizedHandler: (handler: (() => void) | null) => {
    registeredUnauthorizedHandler = handler;
  },
}));

describe("useAuthStore unauthorized handler", () => {
  beforeEach(() => {
    vi.resetModules();
    vi.clearAllMocks();
    registeredUnauthorizedHandler = null;
  });

  it("preserves bootstrap state on 401 handling", async () => {
    const { useAuthStore } = await import("@/features/auth/hooks/use-auth");

    useAuthStore.setState({
      authenticated: true,
      initialized: true,
      bootstrapRequired: true,
      bootstrapTokenConfigured: true,
      error: "boom",
    });

    expect(registeredUnauthorizedHandler).not.toBeNull();
    registeredUnauthorizedHandler?.();

    const next = useAuthStore.getState();
    expect(next.authenticated).toBe(false);
    expect(next.initialized).toBe(true);
    expect(next.error).toBeNull();
    expect(next.bootstrapRequired).toBe(true);
    expect(next.bootstrapTokenConfigured).toBe(true);
  });

  it("refreshes before clearing pending totp state on 401 handling", async () => {
    const { useAuthStore } = await import("@/features/auth/hooks/use-auth");
    (getAuthSession as Mock).mockResolvedValue({
      authenticated: false,
      passwordRequired: true,
      totpRequiredOnLogin: false,
      totpConfigured: true,
      bootstrapRequired: false,
      bootstrapTokenConfigured: false,
      authMode: "standard",
      passwordManagementEnabled: true,
      passwordSessionActive: false,
    });

    useAuthStore.setState({
      authenticated: true,
      initialized: true,
      passwordRequired: true,
      totpRequiredOnLogin: true,
      passwordSessionActive: true,
    });

    expect(registeredUnauthorizedHandler).not.toBeNull();
    registeredUnauthorizedHandler?.();
    await new Promise((resolve) => setTimeout(resolve, 0));

    const next = useAuthStore.getState();
    expect(getAuthSession).toHaveBeenCalledTimes(1);
    expect(next.authenticated).toBe(false);
    expect(next.totpRequiredOnLogin).toBe(false);
    expect(next.passwordSessionActive).toBe(false);
    expect(next.passwordRequired).toBe(true);
    expect(next.initialized).toBe(true);
  });

  it("preserves fresh pending totp state when session still requires it", async () => {
    const { useAuthStore } = await import("@/features/auth/hooks/use-auth");
    (getAuthSession as Mock).mockResolvedValue({
      authenticated: false,
      passwordRequired: true,
      totpRequiredOnLogin: true,
      totpConfigured: true,
      bootstrapRequired: false,
      bootstrapTokenConfigured: false,
      authMode: "standard",
      passwordManagementEnabled: true,
      passwordSessionActive: true,
    });

    useAuthStore.setState({
      authenticated: false,
      initialized: true,
      passwordRequired: true,
      totpRequiredOnLogin: true,
      passwordSessionActive: true,
    });

    expect(registeredUnauthorizedHandler).not.toBeNull();
    registeredUnauthorizedHandler?.();
    await new Promise((resolve) => setTimeout(resolve, 0));

    const next = useAuthStore.getState();
    expect(getAuthSession).toHaveBeenCalledTimes(1);
    expect(next.authenticated).toBe(false);
    expect(next.totpRequiredOnLogin).toBe(true);
    expect(next.passwordSessionActive).toBe(true);
    expect(next.passwordRequired).toBe(true);
    expect(next.initialized).toBe(true);
  });
});
