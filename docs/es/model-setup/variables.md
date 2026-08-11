---
translated_from: 827e532e2b0324591f0fdbb61a39e61180642b24
---

# Variables

![Variables](../assets/model-vars.png)

Las variables ("Vars") son contenedores con nombre para los valores de configuración propios de un modelo, que pueden referenciarse desde cualquier otro punto de la programación, incluidas las [mezclas](mixes.md). Mantenerlas en su propia sección separa los *datos de configuración* del modelo de su *lógica de programación*: en lugar de rebuscar entre docenas de mezclas para encontrar y retocar un valor, todo reside en un único lugar y con un nombre significativo. Hay 64 Vars disponibles; por defecto no existe ninguna. Se añade una con **+**; tocando una Var existente aparecen las opciones **Editar**/**Mover**/**Copiar**/**Clonar**/**Borrar**.

![Añadir variable](../assets/model-vars-add.png)

Una Var puede contener una constante fija, o ser ajustable dentro de unos límites definidos por el usuario (para evitar que valores erróneos provoquen un accidente), y puede tomar un valor *distinto* en cada condición activa (por ejemplo, en cada fase de vuelo). Los valores se conservan entre sesiones. Una Var puede sustituir a cualquier valor numérico ordinario allí donde esté disponible la [función Opciones](../getting-started/user-interface-and-navigation.md#the-options-feature) (los campos con el icono de hamburguesa).

!!! example
    Un planeador con alerones divididos (cuyas secciones interiores hacen también de flaps de aterrizaje) necesita un único valor compartido de diferencial de alerones para todos los casos en que las cuatro superficies actúan como alerones: una Var que contenga ese único valor, referenciada desde cada mezcla implicada, lo mantiene coherente y hace que solo haya que ajustarlo en un sitio.

## Añadir una Var

![Nueva variable](../assets/model-vars-new_var.png)

- **Valor** — valor actual (solo lectura).
- **Nombre** — editable.
- **Comentario** — texto libre que explica su finalidad.
- **Rango** — límites inferior y superior (con un decimal, dentro de ±500 %) que el valor de la Var nunca podrá sobrepasar.

### Valores

![Valores de la variable](../assets/model-vars-values.png)

- **Fijo** — una única constante, con un decimal.
- **Múltiple/variable** — **Añadir nuevo valor** asocia un valor a cada condición activa. Por ejemplo, `Var12` vale 9 % mientras la fase de vuelo Thermal (FM4) está activa, y −3 % mientras Speed (FM5) está activa, con su Rango limitado a −10 %…+15 % para que ninguno de los dos pueda superar unos límites razonables:

  ![Valores dependientes de la fase de vuelo](../assets/model-vars-fm-dependent.png)
  ![Añadir un valor](../assets/model-vars-add-value.png)

### Acciones

![Acciones de la variable](../assets/model-vars-actions.png)
![Añadir acción](../assets/model-vars-add-action.png)

Las acciones modifican el valor de una Var a lo largo del tiempo, gobernadas por una entrada.

**Trim reasignado** — cede uno de los trims físicos al ajuste de esta Var en lugar de su función normal, normalmente limitado a una condición activa:

![Reasignar un trim](../assets/model-vars-functions-repurpose.png)
![Seleccionar el trim a reasignar](../assets/model-vars-functions-repurpose-select.png)

!!! example
    Reasigne el trim del acelerador para ajustar una Var de compensación de curvatura, pero solo mientras la fase de vuelo Landing (FM3) esté activa, con un Rango de 0–25 % y un paso de 1,0 % por clic. Fuera de esa condición activa, el trim recupera automáticamente su función habitual.

**Acciones aritméticas** — gobernadas por cualquier entrada:

- **Asignar** — fija la Var a un valor concreto.
- **Sumar** / **Restar** / **Multiplicar** / **Dividir** — operación aritmética sobre el valor actual.
- **Porcentaje** — aplica un porcentaje de la entrada que la gobierna.
- **Mín** / **Máx** — limita la Var frente a la entrada que la gobierna.

  ![Acciones de función](../assets/model-vars-functions.png)

!!! example
    `FS3(edge)` asigna directamente 40 % a una Var; `FS1(edge)` suma 2 en cada pulsación (con tope en el máximo del Rango); `FS2(edge)` resta 2 en cada pulsación (con tope en el mínimo del Rango). Aquí es importante la opción **Edge** (pulsación larga sobre el interruptor de función): sin ella, la acción se repetiría continuamente mientras se mantuviera accionado el interruptor, en lugar de ejecutarse una sola vez por pulsación.

  ![Ejemplo resuelto](../assets/model-vars-calc-example.png)
