# Example Script Locations

Official example scripts are published at
[github.com/FrSkyRC/ETHOS-Feedback-Community](https://github.com/FrSkyRC/ETHOS-Feedback-Community/tree/main/lua)
(`/lua/examples/task` and `/lua/examples/source` in particular). Most
examples are Lua widgets (configured under [Configure
Screens](../displays/custom-widgets.md)); the **`servo`** example
specifically demonstrates a **System Tool** — a script that appears after
**Info** in the System menu rather than as a display widget.

## Downloading a script

1. Open the repository link above in a browser and navigate to the
   folder, then the `main.lua` file, you want.
2. Click the file to view it, then **Raw**.
3. Right-click the page → **Save Page as…**, saving it as `main.lua`.
4. To avoid clashing with other scripts' `main.lua`, move it into a
   folder named to match — the source folder's own name is a sensible
   choice.

For any other files a script needs (images, etc.): click the file, click
**Download**, then right-click and **Save Image as…** (or equivalent) to
save it alongside the script.

Scripts are installed under `scripts/` on the SD card/eMMC — see [File
Manager](../system-setup/file-manager.md#top-level-folders).

See also the *FrSky ETHOS Lua Script Programming* thread on rcgroups for
community scripts and discussion beyond the official examples.
