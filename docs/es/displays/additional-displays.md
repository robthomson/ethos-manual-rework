---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Pantallas adicionales

![Opciones de configuración de pantalla](../assets/display-screen-config-options.png)

El modelo predeterminado incluye una pantalla (un mapa de bits del modelo más tres widgets de temporizador), pero se admiten hasta **ocho** pantallas en total. Toque el **+** junto a "Screen1" para añadir otra:

- Elija entre **15** disposiciones, incluidas dos disposiciones dedicadas a la pantalla de inicio y una opción a pantalla completa, con capacidad para hasta 9 widgets — configurados exactamente igual que en la primera pantalla.
- Las pantallas se pueden reordenar o eliminar desde su propio diálogo de edición (toque Screen1, Screen2, etc.).

## Ejemplo práctico

![Vista principal](../assets/display-main-view.png)

Una disposición típica: el mapa de bits del modelo (configurado en [Model Edit → Picture](../model-setup/model-edit.md)) a la izquierda, con la tensión de la batería del receptor, el RSSI y un widget de estado "Throttle ACTIVE" (un widget Lua creado por la comunidad, procedente del hilo de rcgroups *FrSky - ETHOS Lua Script Programming*) apilados a la derecha. Al tocar cualquier widget se abre su configuración, o se salta a la función principal Configurar pantallas.

## Opciones a nivel de pantalla

Más allá de los widgets individuales, cada pantalla tiene sus propios ajustes: tamaño de la cuadrícula de la disposición, fondo y qué pantallas se incluyen en el ciclo de `PAGE`.

Consulte [Pantallas](index.md) para los widgets en sí, y [Widgets personalizados](custom-widgets.md) para añadir widgets programados en Lua más allá del conjunto integrado.
