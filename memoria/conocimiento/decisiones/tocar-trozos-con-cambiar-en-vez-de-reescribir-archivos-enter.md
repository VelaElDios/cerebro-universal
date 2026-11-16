---
tipo: "decision"
titulo: "Tocar trozos con CAMBIAR en vez de reescribir archivos enteros"
temas: ["cerebro", "orquestador"]
claves: ["CAMBIAR", "BUSCAR", "POR", "reescribir", "recortado"]
proyectos: []
fuentes: ["scripts/proyecto.py"]
confianza: "verificado"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[cerebro]] · [[orquestador]]

En noviembre de 2026, la memoria de memoria-procesos se atascó 65 pasos: las IAs reescribían capítulos de 800 líneas enteros y en cada paso metían un fallo nuevo. Por eso:

- En archivos de más de 150 líneas se usan bloques `<<<CAMBIAR ruta>>>` con parejas `<<<BUSCAR>>>`/`<<<POR>>>`, que sustituyen solo un trozo exacto.
- Se rechaza un ARCHIVO completo que encoge por debajo del 60 % del actual, porque casi siempre está cortado.

> reescribirlos enteros mete errores en lo que ya estaba bien
> — `scripts/proyecto.py`
