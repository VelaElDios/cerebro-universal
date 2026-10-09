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

## Carpetas

```
config/ias.json         qué IAs hay y cuál hace cada rol (constructor, revisor)
config/entornos.json    qué se instala para cada "necesita" (latex, python-tests...)
scripts/                orquestador y piezas comunes (scripts/cerebro/)
memoria/                lecciones aprendidas (ver memoria/indice.md); en el grafo de Obsidian
                        se ven enlazadas con sus temas y proyectos
proyectos/<nombre>/     spec.md, proyecto.json, bitacora.md, tests, borrador/ y final/
proyectos/_plantilla/   punto de partida para un proyecto nuevo (nunca se ejecuta)
```

## Empezar un proyecto nuevo

1. Copiar `proyectos/_plantilla/` a `proyectos/<nombre>/` (nombre sin espacios).
2. Rellenar `spec.md` y adaptar `verificar.py` (el test que las IAs no pueden tocar).
3. En `proyecto.json`: `nombre`, `temas` (para elegir lecciones), `necesita` (qué instalar),
   `comando_prueba` y, al final, `"estado": "en-construccion"`.

## proyecto.json

| Campo | Para qué |
|---|---|
| `estado` | `en-construccion`, `pausado` o `terminado`. Solo avanzan los que están en construcción. |
| `temas` | Temas del proyecto (`latex`, `python`...): deciden qué lecciones de `memoria/` reciben las IAs. |
| `necesita` | Entornos de `config/entornos.json` a instalar. También se pueden pedir paquetes sueltos con `apt` y `pip`. |
| `comando_prueba` | Lo que se ejecuta dentro de `borrador/` para comprobar el paso (0 = bien). |
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
