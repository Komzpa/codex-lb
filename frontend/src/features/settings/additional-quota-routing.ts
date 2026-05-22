import type { AdditionalQuotaRoutingPolicy, DashboardSettings } from "@/features/settings/schemas";

export function mergeAdditionalQuotaRoutingPolicy(
  policies: DashboardSettings["additionalQuotaRoutingPolicies"],
  quotaKey: string,
  routingPolicy: AdditionalQuotaRoutingPolicy,
) {
  return {
    ...policies,
    [quotaKey]: routingPolicy,
  };
}
