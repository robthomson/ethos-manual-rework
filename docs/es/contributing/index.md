---
translated_from: 727b0ba85be63990bda647e617a27dce6b255458
---

# Contribuir

## Por qué existe este manual

El manual anterior ([`ethos-manual`](https://github.com/FrSkyRC/ethos-manual))
se dividió en dos mitades desconectadas por idioma. El árbol en inglés no fue
nunca más que un **banco de generación de capturas de pantalla** — scripts de
shell que controlaban el simulador real de Ethos a través de una API de macros
en Lua para capturar imágenes de la interfaz — sin ninguna fuente Markdown (ni
de ningún otro formato de texto plano) para la prosa real del manual; el texto
en inglés solo existió como una pila de exportaciones en PDF/ODT. El árbol en
francés, en cambio, era una exportación completa de GitBook con contenido real,
pero desarrollado y mantenido de forma independiente, con su propio conjunto
separado de capturas de pantalla pegadas a mano. Los demás idiomas no tenían ni
lo uno ni lo otro. No había una única fuente de verdad *desde* la que traducir,
ni forma de saber cuándo una página traducida se había quedado desfasada
respecto a la (inexistente) fuente en inglés.

Este repositorio empieza de cero con un solo formato para cada página, en cada
idioma: Markdown plano, construido con [MkDocs Material](https://squidfunk.github.io/mkdocs-material/)
(la misma pila utilizada en [wingflight-docs](https://doc.wingflight.org)),
desplegado en GitHub Pages con cada push a `main`.

## Flujo de trabajo

No hay ningún CMS ni editor web delante del contenido — los redactores y
traductores trabajan directamente en git, igual que con cualquier otro cambio
en este repositorio:

1. Crea una rama a partir de `main` (en este repositorio directamente — véase
   la nota sobre los forks más abajo).
2. Edita los archivos `.md` correspondientes dentro de `docs/en/`.
3. Previsualiza localmente con `mkdocs serve` (véase el
   [README](https://github.com/robthomson/ethos-manual-rework) raíz), o
   simplemente abre el pull request y usa la previsualización automática de PR
   descrita más abajo.
4. Abre un pull request.

Las capturas de pantalla a las que hace referencia una página se encuentran
junto a ella en `docs/en/assets/` y son simplemente enlaces de imagen de
Markdown — sin sintaxis especial. Véase
[Screenshot Pipeline](screenshot-pipeline.md) para saber cómo se generan.

### Previsualizaciones de PR {: #pr-previews }

Cada pull request contra `main` obtiene su propia previsualización en vivo,
construida y desplegada automáticamente por `.github/workflows/pr-preview.yml`:
en `manual.rt-rc.com/pr-preview/<número de PR>/`, enlazada mediante un
comentario de bot en el PR y actualizada con cada push. Se elimina
automáticamente cuando el PR se cierra. El sitio principal en sí
(`manual.rt-rc.com`) no se ve afectado — las previsualizaciones conviven junto
a él en una carpeta `pr-preview/` de la rama `gh-pages` que sobrevive a cada
despliegue de producción.

Esto solo funciona para ramas subidas directamente a este repositorio, no para
forks — un PR desde un fork no obtendrá previsualización en vivo (GitHub
retiene deliberadamente el acceso de escritura de `GITHUB_TOKEN` en los flujos
de trabajo `pull_request` activados desde forks, para que un fork no pueda usar
CI para subir contenido arbitrario a `gh-pages`). Quienes contribuyan desde un
fork pueden previsualizar localmente con `mkdocs serve`.

## Versionado

Los manuales de varias versiones de firmware (por ejemplo, 1.6 junto a un
futuro Ethos26) conviven en el mismo repositorio como ramas separadas, cada una
desplegada en su propia ruta `manual.rt-rc.com/<versión>/` con un menú
desplegable de selección de versión — véase
[Versioning](versioning.md) para el esquema completo y cómo crear una nueva.

## Plan de traducción {: #translation-plan }

Los traductores (humanos o IA) trabajan directamente en git, igual que con
cualquier otro cambio — sin CMS, sin aplicación de traducción aparte. Un primer
piloto en francés (un puñado de páginas) validó la mecánica de principio a fin;
así funciona en la práctica.

### Añadir/actualizar una traducción {: #addingupdating-a-translation }

1. Crea una rama, crea/edita `docs/<locale>/<misma ruta que la página en inglés>`,
   traduciendo la prosa. Mantén tal cual el texto literal de código (nombres de
   teclas como `ENT`, `RTN`, nombres de elementos de la interfaz mostrados en
   pantalla).
2. Marca la página con el commit en inglés desde el que se tradujo:

   ```markdown
   ---
   translated_from: <commit sha of docs/en/... at translation time>
   ---
   ```

   Encuentra ese sha con `git log -1 --format=%H -- docs/en/<path>`.
3. **Si la página en inglés tiene un encabezado al que otras páginas enlazan
   mediante ancla** (compruébalo buscando `#that-heading-slug` en todo
   `docs/en/`), no dejes que el slug autogenerado del encabezado traducido
   cambie el destino — fija explícitamente el mismo ID, estable entre idiomas,
   con `attr_list` (ya habilitado):

   ```markdown
   ## Choisir une source {: #choosing-a-source }
   ```

   Omitir esto no rompe la compilación, pero sí rompe silenciosamente el
   desplazamiento hasta el ancla para cualquier otra página aún sin traducir
   que enlace a ese encabezado mediante el mecanismo de reserva.
4. Abre un PR — [previsualízalo](#pr-previews) como cualquier otro cambio,
   incluido el selector de idioma.

### Capturas de pantalla

No hay nada que duplicar de antemano. [`mkdocs-static-i18n`](https://github.com/ultrabug/mkdocs-static-i18n)
recurre al archivo en inglés para *cualquier* recurso del que un idioma no
tenga su propia copia — el `../assets/foo.png` de una página traducida
funciona sin más, sin modificaciones, mostrando la captura en inglés, hasta que
se coloque una versión localizada real con el mismo nombre de archivo en
`docs/<locale>/assets/`, que a partir de entonces sustituye silenciosamente al
recurso de reserva.

**`de` y `fr` ya cuentan con capturas de pantalla localizadas reales** — no
capturadas aquí, sino importadas en bloque del antiguo repositorio
[`ethos-manual`](https://github.com/FrSkyRC/ethos-manual), que resultó tener
conjuntos de capturas por idioma casi completos que el propio equipo de FrSky
ya había capturado (`german/assets/` y, para el francés, `french_LT/assets/`
— el más completo de sus dos conjuntos de recursos en francés, no el más
reducido `french/assets/` que su README describe como «a medio camino»). Los
nombres de archivo coinciden 1:1 con nuestro propio `docs/en/assets/`, por lo
que la importación fue una copia directa: 586 de las 589 capturas actualmente
referenciadas se incorporaron para ambos idiomas en una sola pasada, sin
necesidad del simulador. El puñado que no coincidió (2-3 archivos, en su
mayoría páginas más recientes que las macros del repositorio antiguo nunca
cubrieron) sigue recurriendo al inglés con normalidad.

Para cualquier idioma más allá de `de`/`fr`, o para cerrar ese último pequeño
porcentaje, capturar nuevas imágenes implica el
[screenshot pipeline](screenshot-pipeline.md)
— adaptar/ejecutar el banco de macros real contra el simulador — ya que ese
trabajo no estaba hecho previamente en el proyecto original.

### Seguimiento de desactualización

[Translation Status](translation-status.md) se genera automáticamente antes de
cada compilación (`hooks/i18n_status.py`, conectado mediante la sección
`hooks:` de `mkdocs.yml` — se ejecuta tanto localmente como en las
previsualizaciones de PR y en producción, siempre actualizado, nunca guardado
en git) y compara el marcador `translated_from` de cada idioma con el commit
real del último cambio de cada página en inglés: **al día**, **desactualizada**
(el inglés ha avanzado) o **ausente**. Esa página es la lista de tareas — sin
GitHub Issues, sin rebuscar en los registros de Actions.

### Traducción automatizada (opcional)

`scripts/translate.py` es un script local independiente (no forma parte de la
compilación del sitio ni de CI) que procesa esa misma lista de páginas
ausentes/desactualizadas a través de la API de Claude para producir un primer
borrador de traducción de cada página, sellado automáticamente con el
frontmatter `translated_from:` correcto:

```bash
pip install anthropic pyyaml   # if not already installed
export ANTHROPIC_API_KEY=...   # or use `ant auth login`

python scripts/translate.py --dry-run       # see what's queued, no API calls
python scripts/translate.py --only fr       # translate everything missing/stale for French
python scripts/translate.py --pages model-setup/mixes.md   # just one page
```

Por defecto lee todos los idiomas de la configuración del plugin `i18n` en
`mkdocs.yml` (`--only` lo restringe a algunos concretos), omite todo lo que ya
esté al día salvo que se pase `--force`, y nunca hace commit ni push — solo
escribe archivos en `docs/<locale>/`, igual que si los hubieras editado a mano.
Revisa el diff, haz la comprobación de
[fijación de anclas](#addingupdating-a-translation) para cualquier encabezado
recién traducido y luego abre un PR como de costumbre.

El prompt del sistema proporciona a Claude de antemano el dominio del manual
(firmware de emisoras FrSky Ethos, público aficionado al RC) y una lista de
términos que nunca deben traducirse (nombres de teclas físicas, nombres de
protocolos, nombres de marcas), la misma técnica empleada por el script
`bin/i18n/auto-translate.py` del repositorio hermano
[`rotorflight-lua-ethos-suite`](https://github.com/rotorflight/rotorflight-lua-ethos-suite).
Un glosario de términos establecido durante el piloto en francés está integrado
para `fr`; amplía `GLOSSARIES` en el script del mismo modo cuando otro idioma
tenga unas cuantas páginas traducidas y revisadas.

### Etiquetas de navegación (`nav_translations`)

Las etiquetas de pestañas y de la barra lateral en `nav:` (por ejemplo, "Model
Setup") no adoptan automáticamente el título traducido de la página en un
idioma, salvo que la entrada de navegación no tenga ninguna etiqueta explícita
(por ejemplo, `- how-to/index.md` — en ese caso MkDocs usa el H1 de la propia
página). En todos los lugares donde `nav:` indica una cadena explícita
`Etiqueta: ruta.md`, o nombra una sección (`Model Setup:` como clave de
diccionario con hijos), esa etiqueta permanece en inglés hasta que el mapa
`nav_translations` del idioma en `mkdocs.yml` la cubra — algo que se añade para
un idioma cuando su cobertura de páginas es lo bastante amplia como para que
traducir la interfaz antes que la mayor parte del contenido no resulte
extraño. El mapa de `fr` se completó cuando el francés alcanzó la cobertura
total de páginas; cada etiqueta final se copió literalmente del H1 traducido de
esa página, de modo que el texto de la barra lateral coincide exactamente con
el encabezado de la página.
