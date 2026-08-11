---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Migrace

První přechod vysílače ze starších samostatných PC nástrojů pro aktualizaci
na Ethos Suite.

1. **Ověřte Ethos ≥ 1.1.4** — jde o minimální verzi, která umí nahrát nový
   bootloader kompatibilní se Suite (formát FRSK) přímo ze [Správce
   souborů](../system-setup/file-manager.md). Pokud je to potřeba, aktualizujte
   nejprve ručně na verzi 1.1.4.
2. **Zálohujte SD card/eMMC** — zkopírujte celý obsah do složky na počítači.
3. **Stáhněte nejnovější bootloader** ze
   [vydání ETHOS-Feedback-Community](https://github.com/FrSkyRC/ETHOS-Feedback-Community/releases)
   a rozbalte jej. Každé vydání obsahuje soubor `components.json` se seznamem
   aktuálních verzí všech komponent — viz [Praktický návod: Nalezení nejnovějšího
   bootloaderu](../how-to/find-latest-bootloader.md), kde je popsáno, jak jej číst.
4. Najděte svůj vysílač v položce `targets` tohoto souboru, kde je uvedena přesná
   verze bootloaderu, kterou je třeba použít, a vyhledejte odpovídající soubor
   mezi přílohami daného vydání.
5. Zapněte vysílač do [režimu bootloaderu](../getting-started/usb-connection-modes.md#bootloader-mode)
   (držte `ENT` a poté zapněte) a připojte jej přes USB.
6. Zkopírujte soubor bootloaderu na SD card/eMMC (obvykle do složky
   `Firmware/`), poté disky odpojte (vysuňte) a odpojte kabel.
7. Zapněte vysílač normálně, přejděte na **System → File Manager**, klepněte na
   právě zkopírovaný soubor `bootloader.frsk` a zvolte **Flash bootloader**.
8. Stáhněte a nainstalujte Ethos Suite — kapitola [Ovládání](operation.md) popisuje
   aktualizaci firmwaru a souborů a další funkce Suite od tohoto bodu dále.
9. Pokud to Ethos Suite neprovede automaticky, může být nutné přejmenovat složku
   `bitmaps/user` na SD card/eMMC na `bitmaps/models` (zde jsou umístěny
   uživatelské obrázky modelů).
