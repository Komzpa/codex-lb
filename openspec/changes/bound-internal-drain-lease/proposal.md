# Bound internal drain leases

The internal deployment drain can otherwise remain active indefinitely when
its caller exits before issuing the matching stop request. Bound operator-started
drains so abandoned deploy attempts recover automatically without weakening the
unbounded process-shutdown path.
