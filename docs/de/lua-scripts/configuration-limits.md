# Grenzen der LUA-Skript-Konfiguration

- 2MB für Bitmaps (ein Vollbild-Bitmap auf X20 verbraucht 768K)

- 2MB für LUA-Skripte (dies ist eine große Menge)

Vermeiden Sie es, zu viel Speicherplatz für Bitmaps zu verwenden. Es wird vorgeschlagen, dass die Benutzer „lazy loading“ verwenden = eine Bitmap NUR bei Bedarf laden. Dann wird sie für die nächste Verwendung im Speicher gehalten, um mehrfaches Lesen von der SD-Karte oder eMMC zu vermeiden.
