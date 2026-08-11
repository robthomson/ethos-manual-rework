---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Een redundante ontvangeropstelling testen

Redundantie is alleen zinvol als deze daadwerkelijk wordt getest vóór het vliegen —
hierbij wordt aangenomen dat een [redundante ontvanger](../model-setup/rf-system.md#redundant-receivers)
al is geconfigureerd.

!!! note "Schermafbeeldingen in afwachting"
    Deze pagina heeft nog geen schermafbeeldingen uit de simulator — zie [Screenshot
    Pipeline](../contributing/screenshot-pipeline.md).

## A. Test in de praktijk

Met de hoofdontvanger op 2,4 GHz en de redundante ontvanger op 900 MHz start je een
[Range Check](../model-setup/rf-system.md#range-check) en loop je van het
model weg tot 2,4 GHz uitvalt (voorbij de melding RSSI Critical). De
redundante 900 MHz-ontvanger moet op dat moment de besturing overnemen.

## B. Test op de werkbank

1. **Controleer de normale opstelling** — beide ontvangers gebonden, beide groene LED's aan,
   besturing reageert normaal.
2. **Bind de hoofdontvanger aan een ander Model ID** — maak een tijdelijk
   testmodel aan (bijv. "TestRx") met een ander Model ID en bind de
   *hoofdontvanger* daaraan. Schakel terug naar het te testen model: de LED van de
   hoofdontvanger moet nu **rood** zijn (elders gebonden), de LED van de
   redundante ontvanger blijft **groen** — en de besturing moet nog steeds werken,
   wat aantoont dat de redundante ontvanger het model op zichzelf vliegbaar houdt.
3. **Bind de hoofdontvanger opnieuw** aan zijn normale Model ID. Controleer of beide
   LED's weer groen zijn en de besturing functioneert voordat je de test
   als voltooid beschouwt.
