---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Trainer

![Trainer](../assets/model-trainer.png)

Desactivado por defecto. Configure la emisora como **Master** (la emisora del
instructor, que recibe hasta 16 controles del alumno) o como **Slave** (la
emisora del alumno, que envía un número configurable de canales al instructor).

## Modo Master

![Modo Master](../assets/model-trainer-master.png)
![Opciones de trainer](../assets/model-trainer-options.png)

### Modo de enlace

![Opciones del modo de enlace](../assets/model-trainer-link-mode-options.png)

- **Cable trainer** — un cable de audio mono de 3,5 mm entre ambas emisoras.
- **Bluetooth** —

  ![Enlace Bluetooth](../assets/model-trainer-link-mode-bt.png)

  - **Modo** — normal o alta velocidad; utilice alta velocidad para reducir la
    latencia si ambas emisoras lo admiten.

    ![Modo Bluetooth](../assets/model-trainer-link-mode-bt-mode.png)

  - **Nombre local** — el nombre BT que ven los demás dispositivos (por
    defecto `FrSkyBT`, editable).
  - **Dirección local** — la dirección Bluetooth de esta emisora.
  - **Dirección remota** — la dirección de la emisora emparejada, una vez
    enlazada.
  - **Buscar dispositivos** (solo en modo Master) — busca dispositivos
    cercanos:

    ![Buscando](../assets/model-trainer-link-mode-bt-search.png)
    ![Esperando](../assets/model-trainer-link-mode-bt-search-waiting.png)
    ![Seleccionar dispositivo](../assets/model-trainer-link-mode-bt-select-device.png)
    ![Conectado](../assets/model-trainer-link-mode-bt-device-connected.png)

  - **Conectar último dispositivo** / **Reiniciar módulo** — vuelve a
    conectarse al emparejamiento anterior, o borra por completo la
    configuración del módulo Bluetooth.

- **Módulo externo SBUS** — una entrada SBUS en el pin PXX-IN de la bahía del
  módulo externo, para instalar un receptor FrSky con salida SBUS (por ejemplo,
  un Archer RS) como extremo receptor de un enlace inalámbrico, lo que permite
  que **cualquier** emisora FrSky actúe como el lado del alumno (buddy box),
  vinculada a ese receptor.
- **Módulo externo CPPM** — la misma idea mediante una entrada CPPM, para un
  receptor antiguo con salida CPPM.

### Condición activa

![Condición activa](../assets/model-trainer-active-condition.png)

Un interruptor/botón, interruptor de función, interruptor lógico, posición de
trim o fase de vuelo que cede el control al alumno mientras esté activo.

### Canales trainer

![Edición de la condición activa](../assets/model-trainer-active-condition-edit.png)

Se pueden transferir hasta 16 canales del alumno al master mientras la
condición activa sea verdadera. Toque un canal para configurarlo
individualmente:

- **Condición activa** — una excepción por canal, por ejemplo para desactivar
  únicamente la entrada de profundidad del alumno durante parte de una sesión.
- **Modo** — **OFF** (desactivado para uso trainer), **Sumar** (las señales del
  master y del alumno se suman, de modo que ambos pueden actuar sobre el
  control a la vez) o **Reemplazar** (el modo normal: el alumno tiene el
  control total de este canal mientras esté activo).
- **Porcentaje** — escala la entrada del alumno, normalmente 100 %.
- **Destino** — a qué función se asigna el canal del alumno.

Consulte [Guía práctica: recuperación instantánea del control](../how-to/instant-takeback.md)
para ver un ejemplo práctico de cómo el instructor recupera el control al
instante mediante un interruptor, e [Ignorar entrada del trainer](../getting-started/user-interface-and-navigation.md#choosing-a-source)
para excluir el movimiento del stick del alumno de un interruptor lógico que
vigila los sticks del propio instructor.

## Modo Slave

![Modo Slave](../assets/model-trainer-slave-mode.png)

- **Modo de enlace** — las mismas opciones de cable trainer, Bluetooth o módulo
  externo SBUS/CPPM que en Master (con los mismos campos Bluetooth
  **Modo**/**Nombre local**/**Dirección local**/**Dirección remota**).

  ![Modo de enlace en Slave](../assets/model-trainer-slave-link-mode.png)

- **Rango de canales** — qué rango de canales de esta emisora se envía al
  master.

  ![Canales en Slave](../assets/model-trainer-slave-channels.png)
  ![Edición de canal en Slave](../assets/model-trainer-slave-channel-edit.png)
