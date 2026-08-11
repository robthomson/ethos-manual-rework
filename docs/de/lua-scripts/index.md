---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Lua-Skripte

Mit Lua-Skripten können Sie eigene [Anzeige-Widgets](../displays/custom-widgets.md)
erstellen, um Informationen darzustellen, die Ethos nicht von Haus aus abdeckt,
sowie (je Modell) eigene [Quellen und Tasks](../model-setup/lua-scripts.md) —
eine Grundlage, die künftig weiter ausgebaut werden soll, hin zu spezialisierten
benutzerdefinierten Funktionen und der Anbindung von Flight Controllern.

Lua selbst ist eine schlanke, einbettbare Allzweck-Skriptsprache, die überall
zum Einsatz kommt, von Spielen bis hin zu Webanwendungen. Ethos bindet sie
genau für diese Art der Anpassung direkt am Sender ein.

!!! warning
    Lua-Skripte verlängern die Startzeit des Senders. Bei einem gut geschriebenen
    Skript sollte die Verzögerung nicht wahrnehmbar sein — ein schlecht
    geschriebenes Skript kann den Start nahezu unbegrenzt verzögern.

- [Lua-Interpreter](lua-interpreter.md) — welche Lua-Version und welche
  Bibliotheken Ethos einbindet.
- [Ethos-Lua-Dokumentation](ethos-lua-documentation.md) — wo die vollständige
  API-Referenz zu finden ist.
- [Fundorte für Beispielskripte](example-script-locations.md) — wo Sie
  funktionsfähige Beispiele finden und herunterladen können.
- [Konfigurationsgrenzen](configuration-limits.md) — Speicherbudgets für
  Bitmaps und Skripte.
- [Grundlegender Widget-Aufbau](basic-widget-layout.md) — die Codestruktur,
  die ein benutzerdefiniertes Widget-Skript benötigt.
