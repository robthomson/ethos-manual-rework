# Estructura de un widget Lua

Todos los scripts de Lua, incluidos los widgets, utilizan manejadores (también conocidos como módulos de código) para realizar tareas específicas como el procesamiento de datos en segundo plano, controlar/dibujar la pantalla, configurar widgets, leer o guardar configuraciones, capturar y evaluar eventos, etc.

## init(función)

La función del controlador init se utiliza para registrar el widget durante el inicio del transmisor. Utiliza el método system.registerWidget() para declarar el widget. También especifica qué controladores adicionales se utilizan en el script.

Un ejemplo de un manejador de inicialización para un widget podría ser:

local function init()

system.registerWidget({

key = "unique",

name = “Example”,

create = create,

configure = configure,

wakeup = wakeup,

paint = paint,

read = read,

write = write,

})

end

Tenga en cuenta que 'key' es un identificador único para su widget. Las diversas funciones enumeradas se utilizan en el ciclo de vida del widget.

## Método system.registerWidget()

El método system.registerWidget() puede tener los siguientes parámetros:

## clave (cadena)

El widget debe tener una clave única que no tenga más de 7 caracteres.

## nombre (cadena o función)

El nombre de una función no tiene argumentos y devuelve el nombre del widget como una cadena. El nombre del widget puede ser simplemente una cadena o el resultado de una función. Por ejemplo, el nombre puede estar en un idioma diferente según la configuración regional.

## crear (función)

La función ‘create handler’ se usa al crear el widget. No tiene argumentos y cuando termine devolverá la tabla del widget que luego se utilizará en todas las otras funciones. Inicialice sus variables aquí y almacene su estado en la tabla que devuelve el widget.

### destruir (función, opcional)

La función destruir se usa cuando se borra un widget.

## configurar (función)

La función ‘configurar manejador’ se activa cuando el usuario entra en la configuración del widget. Toma la tabla creada por el widget anterior y sólo sus argumentos y no devuelve nada. De esta forma, puede crearse el formato de la configuración y cambiarse dentro de la tabla.

### 	Construir (función, opcional)

El manejador de construir se llama en cada cambio de diseño cuando el widget se construye en la pantalla de inicio, y después de la creación y configuración.

## wakeup (función)

La función ‘wakeup handler’ funciona en cada ciclo. Por ejemplo cada 50ms. Maneja el contenido de la tabla y sus argumentos, pero no devuelve nada.

La función wakeup() debería comprobar si algo ha cambiado. En caso afirmativo, se necesita un refresco por lo que se debe llamar a la función invalidateWindow(). Esto hará que se llame a la función paint(). Debe asegurarse de que esta función sea rápida, idealmente que no tenga que hacer nada durante el mayor tiempo posible.

## evento (función)

La función ‘event handler’ se usa cuando se recibe un evento. ETHOS ofrece la posibilidad de capturar cualquier evento en un widget, a través de esta función.

## pintar (función)

La función ‘paint’ dibuja el widget. Maneja el contenido de la tabla y sus argumentos y no devuelve nada. También debe usarse cuando se necesita una actualización, y es llamada automáticamente siempre que se llama a lcd.invalidate(). Puede ser muy lenta, así que se debe llamar sólo si algo ha cambiado.

### menu (función, opcional)

El manejador de menú opcional se llama cuando se crea un menú contextual, para permitir agregar más opciones al menú. El manejador debe devolver una tabla de pares { nombre, función }.

## leer (function)

Esta función ‘read handler’ es opcional. En ETHOS es posible utilizar el almacenamiento como se desee.

## escribir (función)

La función ‘write handler’ también es opcional. En ETHOS es posible utilizar el almacenamiento como se desee.

### persistente (booleano, opcional)

Manejador de datos persistentes opcional.

### titulo (booleano, opcional)

Manejador de título opcional. El título del widget se fuerza ENCENDIDO / APAGADO.

Los scripts Lua se almacenan en la carpeta scripts/ de la tarjeta SD o eMMC, preferiblemente organizadas en carpetas.

Consulte el hilo de rcgroups 'FrSky ETHOS Lua Script Programming' para más información.
