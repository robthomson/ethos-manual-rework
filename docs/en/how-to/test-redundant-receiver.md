# Test a Redundant Receiver Setup

Redundancy is only worth having if it's actually tested before flying —
this assumes a [redundant receiver](../model-setup/rf-system.md#redundant-receivers)
is already configured.

!!! note "Screenshots pending"
    This page doesn't have simulator screenshots yet — see [Screenshot
    Pipeline](../contributing/screenshot-pipeline.md).

## A. Real-world test

With the main receiver on 2.4GHz and the redundant one on 900MHz, start a
[Range Check](../model-setup/rf-system.md#range-check) and walk away from
the model until 2.4GHz drops out (past the RSSI Critical alert). The
900MHz redundant receiver should take over control at that point.

## B. Bench test

1. **Confirm normal setup** — both receivers bound, both green LEDs on,
   controls responding normally.
2. **Bind the main receiver to another Model ID** — create a throwaway
   test model (e.g. "TestRx") with a different Model ID, and bind the
   *main* receiver to it. Switch back to the model under test: the main
   receiver's LED should now be **red** (bound elsewhere), the redundant
   receiver's LED stays **green** — and controls should still work,
   proving the redundant receiver alone is keeping the model flyable.
3. **Rebind the main receiver** back to its normal Model ID. Confirm both
   LEDs are green again and controls are functioning before considering
   the test complete.
