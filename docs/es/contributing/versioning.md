---
translated_from: f9f31073c0e8b5352770d12703868b7972365db6
---

# Versionado

Ethos distribuye actualmente su firmware con números de versión (1.6.x) y ha
anunciado un cambio hacia una identificación basada en el año (por ejemplo, «Ethos26»). Este manual
debe mantener disponible y correcta la documentación de las versiones antiguas mientras se escriben
activamente las nuevas versiones: esta página explica cómo.

## Cómo funciona

El versionado se gestiona con [mike](https://github.com/jimporter/mike), la
herramienta que Material for MkDocs recomienda. `.github/workflows/deploy.yml`
ejecuta `mike deploy` en lugar de publicar directamente en la raíz de `gh-pages`:
cada versión se compila y se confirma en su propia subcarpeta (`/1.6/`,
`/26/`, …), y `manual.rt-rc.com/` redirige a la versión que en ese momento
tenga el alias `latest`. Material muestra automáticamente un desplegable de selección
de versión, leyendo `versions.json` (que mantiene `mike`)
— algo independiente del selector de idioma, con el que se combina limpiamente:
la versión es el segmento externo de la ruta y el idioma (cuando exista más de `en`) es
el interno, por ejemplo `manual.rt-rc.com/26/fr/...`.

Esto reutiliza el mismo mecanismo de «subcarpeta en `gh-pages`» que las [vistas previas
de PR](index.md#pr-previews): las carpetas de versión de `mike` y la carpeta
`pr-preview/` coexisten en la misma rama sin conflictos, ya que
cada una solo toca sus propias rutas.

## Estructura del código fuente: `main` + ramas congeladas

- **`main` siempre refleja el contenido de la versión actual/más reciente del firmware.**
  La edición diaria se realiza aquí exactamente igual que hoy: no
  cambia nada en el flujo de contribución habitual.
- Cuando el manual de una nueva versión de firmware deba empezar a divergir de
  lo que hay en `main`, **cree primero una rama con el nombre de la versión antigua**,
  por ejemplo `1.6`, para congelarla permanentemente. `main` pasa entonces a contener el contenido
  de la nueva versión.
- Una rama congelada no está muerta: puede seguir recibiendo correcciones mediante sus
  propios PR. Simplemente ya no sigue el desarrollo de la nueva versión.

## Crear una nueva versión

Cuando deba comenzar el manual de la siguiente versión (por ejemplo, Ethos26):

1. Desde `main`, cree y publique la rama congelada de la versión que se
   deja atrás:

   ```
   git checkout main && git pull
   git branch 1.6
   git push origin 1.6
   ```

   La copia de `.github/workflows/deploy.yml` en `1.6` ahora despliega permanentemente
   `mike deploy --push --update-aliases 1.6 latest` en cada push a esa
   rama — correcto tal cual, sin necesidad de editarlo, ya que una rama es una instantánea
   completa que incluye su propia configuración de CI.

2. En `main`, edite `.github/workflows/deploy.yml`: cambie la cadena de
   versión en el paso `Deploy version 1.6 with mike` (y su nombre) de
   `1.6` a la etiqueta de la nueva versión (por ejemplo, `26`). Esta es la **única**
   edición necesaria para empezar a desplegar la nueva versión: el siguiente push a
   `main` la publicará en `/26/` y trasladará allí el alias `latest`,
   mientras que `/1.6/` permanecerá exactamente igual que antes.

3. Actualice el contenido de la nueva versión en `main` según lo que haya
   cambiado realmente: secciones de menú nuevas o renombradas, nuevas capturas de pantalla,
   terminología actualizada. El `nav` de `mkdocs.yml` puede diferir libremente entre ramas;
   no hay configuración compartida que deba mantenerse sincronizada.

4. Añada el nombre de la nueva rama a la lista de disparadores `branches:` de
   `.github/workflows/pr-preview.yml` si los PR contra ella también deben obtener vistas
   previas en vivo (las ramas congeladas normalmente no lo necesitan, ya que solo reciben
   PR de corrección ocasionales).

## Capturas de pantalla entre versiones

Las capturas de pantalla se toman de una compilación concreta de Ethos (véase [Flujo de trabajo de
capturas de pantalla](screenshot-pipeline.md)) y pertenecen a la rama cuya interfaz
muestran: al crear una versión, el conjunto de capturas se bifurca de forma natural junto con
todo lo demás, de modo que `1.6/assets/` y (una vez regeneradas para la nueva interfaz)
`docs/en/assets/` de `main` divergen de forma independiente a partir del punto de bifurcación.
