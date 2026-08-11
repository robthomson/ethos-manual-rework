---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Vistas principales

## Pantalla de inicio

![Pantalla de inicio](../assets/mainview.png)

La pantalla de inicio es lo que se ve cuando no hay ningún menú abierto: un conjunto
de hasta **ocho** pantallas de visualización que usted mismo configura (consulte
[Pantallas](../displays/index.md)), entre las que se navega deslizando el dedo o
paginando con la tecla `PAGE`. Un modelo recién creado comienza con una sola pantalla
que muestra una imagen del modelo, tres widgets de temporizador y los indicadores de
trim/potenciómetros; a partir de ahí, todo lo que contiene es configurable por el usuario.

Normalmente las pantallas comparten las barras superior e inferior descritas más abajo,
pero también se puede configurar una pantalla como pantalla completa, ocultando ambas.

## La barra superior

La barra superior muestra el nombre del modelo a la izquierda (además de la fase de vuelo
activa, si hay alguna configurada) y una fila de iconos de estado a la derecha:

- Registro de datos activo
- Estado del modo entrenador (maestro o esclavo, según corresponda)
- RSSI — enlace de 2,4 GHz
- RSSI — enlace de 900 MHz (si está instalado un módulo de doble banda/largo alcance)
- Volumen del altavoz
- Estado de la batería de la emisora

Al tocar el icono del altavoz o de la batería se accede directamente al panel de ajustes
correspondiente: [General](../system-setup/general.md) (audio) o
[Batería](../system-setup/battery.md).

### Aviso de error

Aparece un triángulo rojo en la barra superior siempre que Ethos detecta un error:
un error en un script Lua, un error de copia de seguridad de la RAM o el uso de una
versión de firmware nightly/inestable son las causas más habituales. El detalle que
hay detrás del aviso siempre se encuentra en **System → Info**, en la misma página que
el tiempo de uso de la emisora y los [registros de errores](../system-setup/information.md).

## La barra inferior

![Barra inferior](../assets/bottombar.png)

En la parte inferior hay cuatro pestañas correspondientes a las secciones principales
—**Inicio**, **Configuración del modelo**, **Configurar pantallas**, **Configuración del
sistema**— con el reloj del sistema a la derecha (tóquelo para acceder directamente a
[Fecha y hora](../system-setup/date-and-time.md)).

## El área de widgets

La parte central de cada pantalla se rellena con **widgets**: imagen del modelo,
temporizadores, lecturas de telemetría, barras de trim/potenciómetros y más, todos
colocados y configurados por usted. Consulte [Pantallas](../displays/index.md) para saber
cómo añadir, mover y configurar widgets, y
[Pantallas adicionales](../displays/additional-displays.md) para añadir más pantallas
además de la única predeterminada.
