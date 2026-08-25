# Lua scripting configuration limits

- 2MB for bitmaps (one full screen bitmap on X20 consumes 768K)

- 2MB for Lua scripts (this is a large amount)

Avoid using too much ram for bit maps. It is suggested the users use lazy loading = load a bitmap ONLY when needed. Then keep it in memory for the next use, to avoid multiple reads from the SD card or eMMC.
