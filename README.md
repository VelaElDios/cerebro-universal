# cerebro-universal

Vamos a darle caña a un proyecto que llevo tiempo queriendo hacer en cuanto salió todo el tema de la inteligencia artificial y he visto por ahí que hay gente que ya lo tiene, yo no se como lo habrán hecho los demás, pero yo lo voy a hacer de forma totalmente gratuita y publica, tener un cerebro-universal

## Cómo funciona

Varias IAs gratuitas de empresas distintas construyen proyectos por turnos y todo queda guardado
en este repo, que también es un vault de Obsidian.

En cada ejecución del workflow (`.github/workflows/proyecto.yml`):

1. `scripts/elegir_proyecto.py` elige el proyecto en construcción que lleve más tiempo sin avanzar
   e instala solo lo que ese proyecto necesita (`config/entornos.json`).
2. `scripts/proyecto.py` da UN paso: el **constructor** escribe en `borrador/`, se ejecuta la
   **prueba** (si falla, el constructor lo intenta arreglar), el **revisor** comprueba y corrige,
   y si todo pasa se copia a `final/`.
3. Las IAs reciben las **lecciones de `memoria/`** que encajan con el proyecto y con el error del
   momento. Si en un paso se arregla un fallo, el revisor puede proponer una lección nueva.

## La memoria compartida (para las IAs)

El vault es la memoria de todas las IAs: dé igual cuál esté conectada, lee lo que aprendieron las anteriores
y lo usa igual. Puerta de entrada: [`memoria/CEREBRO.md`](memoria/CEREBRO.md).

- **Ficha de cada proyecto** (`proyectos/<nombre>/estado.md`): qué es, decisiones y convenciones, estado y
  siguiente. La reescribe el revisor en cada paso y es lo primero que lee la siguiente IA.
- **Conocimiento** (`memoria/conocimiento/`): conceptos, recetas (cómo lo hacemos), decisiones (y por qué),
  datos y documentos aprendidos, con cabecera para máquinas y una cita literal comprobada
  (`confianza: "verificado"`). Lo escriben el revisor (bloque `<<<CONOCIMIENTO>>>`) y el proyecto
  `aprendizaje`, que lee la documentación de los proyectos y los temarios del repo privado `cerebro-datos`.
- **Lecciones** (`memoria/lecciones/`): errores ya resueltos.
- **Mapas** (`memoria/temas/` como nodos centrales, `memoria/mapas/cerebro.canvas` como mapa visual y
  `memoria/mapas/grafo.json` para máquinas): se regeneran en cada paso.
- **Datos para entrenar una IA local** (`scripts/cerebro/dataset.py`): cada llamada a una IA y qué pasó
  con ella, comprimido en el repo privado `cerebro-datos` (secrets `DATOS_TOKEN` y `DATOS_REPO`), junto
  con `export/conocimiento.jsonl`.

## Carpetas

```
config/ias.json         qué IAs hay y cuál hace cada rol (constructor, revisor)
config/entornos.json    qué se instala para cada "necesita" (latex, python-tests...)
scripts/                orquestador y piezas comunes (scripts/cerebro/)
memoria/                CEREBRO.md (entrada), conocimiento/, lecciones/, temas/ (nodos del mapa),
                        mapas/ (canvas y grafo.json) e indice.md
proyectos/<nombre>/     spec.md, proyecto.json, bitacora.md, tests, borrador/ y final/
proyectos/_plantilla/   punto de partida para un proyecto nuevo (nunca se ejecuta)
```

## Empezar un proyecto nuevo

1. Copiar `proyectos/_plantilla/` a `proyectos/<nombre>/` (nombre sin espacios).
2. Rellenar `spec.md` y adaptar `verificar.py` (el test que las IAs no pueden tocar).
3. En `proyecto.json`: `nombre`, `temas` (para elegir lecciones), `necesita` (qué instalar),
   `comando_prueba` y, al final, `"estado": "en-construccion"`.

## Trabajar sobre un repo (p. ej. escribir la memoria de un proyecto)

1. Copiar `proyectos/_plantilla/` y poner en `proyecto.json` el repo en `repos` y en `fuentes` qué
   documentos leer (`repo:nombre/...`). Si tiene capturas, `copiar`.
2. Escribir las normas en `spec.md` (qué hay que producir y con qué reglas) y el test en `verificar.py`.
   Un test puede comprobar datos contra las mismas fuentes que leen las IAs con `cerebro.repos.texto_fuentes()`
   (ver `proyectos/memoria-procesos/verificar.py`).
3. `"estado": "en-construccion"`. Cada paso lee la última versión del repo y lo apunta en la bitácora.

## proyecto.json

| Campo | Para qué |
|---|---|
| `estado` | `en-construccion`, `pausado` o `terminado`. Solo avanzan los que están en construcción. |
| `temas` | Temas del proyecto (`latex`, `python`...): deciden qué lecciones de `memoria/` reciben las IAs. |
| `necesita` | Entornos de `config/entornos.json` a instalar. También se pueden pedir paquetes sueltos con `apt` y `pip`. |
| `comando_prueba` | Lo que se ejecuta dentro de `borrador/` para comprobar el paso (0 = bien). |
| `repos` | Opcional. Repos públicos de GitHub que el cerebro lee: `{"saas": "https://github.com/usuario/repo"}`. Se descargan de nuevo en cada paso (siempre la última versión) en `.repos/`, que no se sube. |
| `fuentes` | Opcional. Lo que se pasa a las IAs como única verdad: archivos del proyecto (`fuentes/normas.md`) o de un repo (`repo:saas/README.md`, `repo:saas/docs/**/*.md`, y `repo:saas/@arbol` para la lista de archivos). Admiten `*` y `**`. |
| `copiar` | Opcional. Archivos de un repo que se copian solos a `borrador/` (p. ej. capturas): `[{"desde": "repo:saas/docs/capturas/**/*.png", "a": "figs/capturas"}]`. Las IAs reciben la lista con lo que muestra cada imagen (su texto alternativo en los Markdown del repo). |
| `protegidos` | Opcional. Patrones de archivos de `borrador/` que las IAs no pueden escribir ni borrar (plantilla, imágenes...), p. ej. `figs/*`. |
| `reintentar_si` | Opcional. Expresión regular: si la prueba falla, el constructor solo reintenta cuando el fallo la cumple (p. ej. un error de compilación). Útil cuando la prueba falla durante muchos pasos porque falta trabajo. |
| `archivo_principal` | Opcional. Si no existe todavía, la prueba falla sin ejecutarse. |
| `pasos` / `max_pasos` | Freno: al llegar al máximo el proyecto se pausa. |
| `max_intentos` | Veces que el constructor puede arreglar su paso si la prueba falla. |
| `max_archivos_por_paso` | Archivos que puede escribir cada IA por respuesta. |
| `roles` | Opcional. Cambia qué IAs hacen cada rol solo en este proyecto. |
| `ultima_ejecucion` | Lo escribe el orquestador; sirve para rotar entre proyectos. |

## Reglas

- Repo público: nada de claves ni datos personales en ningún archivo (las claves van en los secrets de GitHub).
- No editar `borrador/` ni `final/` a mano: para dar instrucciones, añadir al final de la bitácora
  una entrada `## Revisión humana (Javier)`.
- Los tests van fuera de `borrador/`.
- Lecciones de `memoria/` con `estado: "propuesta"`: revisarlas y pasarlas a `"confirmada"` (o borrarlas).
