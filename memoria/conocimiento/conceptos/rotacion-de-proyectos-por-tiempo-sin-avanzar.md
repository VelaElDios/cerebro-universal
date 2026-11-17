---
tipo: "concepto"
titulo: "Rotación de proyectos por tiempo sin avanzar"
temas: ["cerebro", "orquestador"]
claves: ["elegir_proyecto.py", "ultima_ejecucion", "config/entornos.json", "necesita"]
proyectos: []
fuentes: ["../../README.md"]
confianza: "propuesto"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[cerebro]] · [[orquestador]]

El orquestador no ejecuta todos los proyectos a la vez. En cada run del workflow, `scripts/elegir_proyecto.py` escanea los proyectos con `"estado": "en-construccion"` y selecciona el que tenga `ultima_ejecucion` más antigua (el que más tiempo lleva sin avanzar). Luego instala únicamente los entornos listados en su campo `necesita` (mapeados en `config/entornos.json` a paquetes apt/pip/latex/etc.). Tras el paso, el orquestador actualiza `ultima_ejecucion` con la fecha/hora actual. Así se rota de forma justa entre proyectos activos.

> `scripts/elegir_proyecto.py` elige el proyecto en construcción que lleve más tiempo sin avanzar e instala solo lo que ese proyecto necesita (`config/entornos.json`). Y: `ultima_ejecucion` Lo escribe el orquestador; sirve para rotar entre proyectos.
> — `../../README.md` (cita sin comprobar)

Relacionado: [[como-trabaja-el-cerebro-constructor-prueba-revisor]] · [[campos-de-proyecto-json-y-su-proposito]] · [[estructura-de-la-memoria-compartida-cerebro-md-estado-md-con]]
