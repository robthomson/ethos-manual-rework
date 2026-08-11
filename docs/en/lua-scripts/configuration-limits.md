# Configuration Limits

- **2MB** for bitmaps (a single full-screen bitmap on the X20 alone uses
  roughly 768K).
- **2MB** for Lua scripts — a generous budget in practice.

!!! tip "Bitmaps in scripts"
    Avoid holding large amounts of bitmap data in RAM. Prefer **lazy
    loading** — load a bitmap only when it's actually needed, then keep
    it cached in memory for next time rather than re-reading it from the
    SD card/eMMC repeatedly.
