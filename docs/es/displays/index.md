---
translated_from: 155bf1cf224c4b0fd100735316cf652f6baef3e6
---

# Pantallas

![Pantalla de inicio](../assets/display-home.png)

La pantalla de inicio consta de una o más **pantallas de visualización**, cada una construida a partir de **widgets** que usted mismo coloca y configura. Al pulsar `DISP` se abre el editor de la pantalla actual.

Hay disponibles hasta **ocho** pantallas, cada una partiendo de uno de **trece** diseños (con capacidad para hasta **nueve** celdas de widget). Los widgets pueden mostrar telemetría, pero también cualquiera de otras diecisiete categorías de información: estado del modelo/emisora, temporizadores, canales y más. Se accede a las pantallas configuradas deslizando el dedo o con `PAGE` arriba/abajo; las barras superior e inferior permanecen visibles en todas las pantallas, excepto en un diseño a pantalla completa.

## Añadir un widget

![Tipos de widget](../assets/display-widget-types.png)

Cada pantalla es una cuadrícula; al tocar una celda vacía se abre el selector de widgets. Los widgets abarcan desde simples lecturas de texto y numéricas hasta indicadores, gráficos y registros completos de telemetría. Una vez colocado, al tocar de nuevo un widget se abre el mismo menú de opciones que se utiliza para redimensionarlo, moverlo o eliminarlo:

![Opciones de configuración del widget](../assets/display-widget-config-options.png)

Al seleccionar los ajustes propios de un widget se abre un formulario de configuración específico de ese widget. El campo **fuente** —el valor que muestra el widget— utiliza el mismo [selector de fuentes](../getting-started/user-interface-and-navigation.md#choosing-a-source) que el resto de Ethos:

![Cambiar la fuente del widget](../assets/display-change-source.png)

## Tipos de widget {: #widget-types }

**Valor** — una única lectura numérica o de telemetría, mostrada como texto:

![Configuración del widget Valor](../assets/display-widget-value-config.png)

La mayoría de las fuentes también admiten reducirse a un **mín** o **máx** en vivo —tras seleccionar la fuente, manténgala pulsada y elija Min o Max—, lo que resulta útil para cosas como el peor RSSI registrado durante un vuelo:

![Widget Valor mín](../assets/display-widget-value-min.png)
![Widget Valor mín RSSI](../assets/display-widget-value-min-rssi.png)

Una vez colocado, se muestra como una lectura simple en la pantalla:

![Widget Valor de telemetría](../assets/display-widget-value-telemetry.png)

**Bitmap** — muestra una imagen estática (por ejemplo, una foto del modelo) o un conjunto de imágenes que se intercambian según el valor de una fuente (por ejemplo, un icono de batería que cambia con la tensión):

![Configuración del widget Bitmap](../assets/display-widget-bitmap-config.png)
![Tipo de widget Bitmap](../assets/display-widget-bitmap-type.png)

**LiPo** — un indicador de batería específico que lee de un sensor como el FLVSS: tensión total del pack, número de celdas y la tensión de cada celda individual. Al caer por debajo del umbral de **Tensión baja** configurado, la pantalla se vuelve roja; en el ejemplo siguiente, un umbral de 3,3 V se activa en la celda más baja:

![Configuración del widget LiPo](../assets/display-widget-lipo-config.png)
![Widget LiPo](../assets/display-widget-lipo.png)

**Canales** — hasta 8 canales de salida en forma de gráfico de barras, horizontal o vertical:

![Configuración del widget Canales](../assets/display-widget-channels-config.png)
![Widget Canales](../assets/display-widget-channels.png)

**Gráfico de líneas** — traza el valor de una fuente a lo largo del tiempo, reiniciándose con un Reinicio de vuelo:

![Configuración del widget Gráfico de líneas](../assets/display-widget-line-chart-config.png)
![Widget Gráfico de líneas](../assets/display-widget-line-chart.png)

- **Fuente** — lo que se está representando.
- **Condición de pausa** — una fuente que pausa/reanuda el registro (o simplemente toque el widget en funcionamiento, si no dispone de una fuente libre para esto).
- **Periodo de registro** — intervalo de muestreo; 500 ms cubre aproximadamente 6 minutos antes de desplazarse, 1 s aproximadamente 12 minutos.
- **Invertido** — voltea el gráfico verticalmente.
- **Rango automático** — escala el eje vertical para ajustarse automáticamente a los datos; desactivado, utiliza en su lugar valores fijos de **Mín**/**Máx** (por ejemplo, un rango constante de −100 %…+100 %).

Al tocar un gráfico en funcionamiento aparecen **Pausar/reanudar**, **Reiniciar** (borrar y empezar de nuevo), **Configurar widget** o el acceso directo a **Configurar pantallas**:

![Opciones del gráfico de líneas](../assets/display-widget-line-chart-options.png)

**Texto** — muestra el contenido de un archivo de texto Markdown (leído de `documents/user/` — véase el [Gestor de archivos](../system-setup/file-manager.md#top-level-folders)):

![Configuración del widget Texto](../assets/display-widget-text-config.png)
![Widget Texto](../assets/display-widget-text.png)

**Registro de temporizador** — un registro desplazable de los valores pasados de un temporizador elegido, escrito cada vez que ese temporizador se reinicia (útil para llevar el control del uso de los packs de vuelo a lo largo de una sesión); **Invertir** coloca la entrada más reciente en la parte superior:

![Configuración del widget Registro de temporizador](../assets/display-widget-timer-logs-config.png)
![Widget Registro de temporizador](../assets/display-widget-timer-log.png)

Mantenga pulsada una entrada (o el widget) para acceder a **Borrar registros**, editar/reiniciar el temporizador subyacente o saltar a la configuración del widget o de la pantalla:

![Menú de entrada del registro de temporizador](../assets/display-widget-timer-log-menu.png)

**Mapa GPS** — traza la posición GPS en vivo como una ruta, para modelos con un sensor GPS (véase el hilo *FrSky - ETHOS Lua Script Programming* en rcgroups, mensaje n.º 8854, para más detalles sobre este widget en concreto):

![Configuración del widget Mapa GPS](../assets/display-widget-gps-map-config.png)

## Opciones a nivel de pantalla

Más allá de los widgets individuales, cada pantalla tiene sus propios ajustes: tamaño de la cuadrícula del diseño, fondo y qué pantallas se incluyen en el ciclo de `PAGE`:

![Opciones de configuración de la pantalla](../assets/display-screen-config-options.png)

Una pantalla de inicio completamente configurada combina varios widgets en un único diseño de lectura rápida:

![Vista principal](../assets/display-main-view.png)

Véase [Pantallas adicionales](additional-displays.md) para añadir más pantallas además de la predeterminada, y [Widgets personalizados](custom-widgets.md) para widgets basados en scripts Lua más allá del conjunto integrado.
