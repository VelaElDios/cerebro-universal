---
tipo: "concepto"
titulo: "Cómo trabaja el cerebro (constructor, prueba, revisor)"
temas: ["cerebro", "orquestador"]
claves: ["proyecto.py", "constructor", "revisor", "borrador", "final"]
proyectos: []
fuentes: ["README.md", "../../README.md"]
confianza: "verificado"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[cerebro]] · [[orquestador]]

En cada ejecución del workflow, `scripts/elegir_proyecto.py` elige el proyecto en construcción que lleva más tiempo sin avanzar, y `scripts/proyecto.py` da UN paso:

1. El **constructor** escribe en `borrador/`.
2. Se ejecuta la **prueba** (`comando_prueba`). Si falla por un error de verdad (cumple `reintentar_si`), el constructor lo intenta arreglar.
3. El **revisor**, una IA de otra empresa, comprueba, corrige lo evidente, deja tareas y reescribe la ficha del proyecto (`estado.md`).
4. Si todo pasa, se copia a `final/`.

Las IAs reciben las lecciones, el conocimiento y el mapa del cerebro que encajan con el proyecto. Los proyectos de tipo `aprender` (como `aprendizaje`) no construyen nada: leen documentos y guardan conocimiento.

> el **constructor** escribe en `borrador/`
> — `README.md`

## Ampliación (2026-11-16, )
El orquestador ejecuta un workflow por proyecto. Primero `elegir_proyecto.py` selecciona el proyecto con `estado: "en-construccion"` cuya `ultima_ejecucion` sea más antigua e instala los entornos definidos en `config/entornos.json` según el campo `necesita`. Luego `proyecto.py` ejecuta un único paso: el constructor escribe archivos en `borrador/`, se lanza `comando_prueba` dentro de `borrador/`; si falla (código ≠ 0), el constructor reintenta hasta `max_intentos` (filtrado por `reintentar_si` si existe). Si pasa, el revisor valida y corrige; si todo está bien, el contenido de `borrador/` se copia a `final/`. Las IAs reciben lecciones de `memoria/` relevantes por `temas` y error actual.
