---
tipo: "concepto"
titulo: "WAW corresponde a dependencia de salida"
temas: ["ac", "dependencias", "waw"]
claves: ["WAW", "dependencia de salida", "riesgo WAW"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2015.pdf", "repo:datos/temarios/AC/examenes/Enero2016.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[dependencias]] · [[waw]]

WAW (Write After Write) es una dependencia de salida: dos instrucciones escriben en el mismo registro/ubicación de memoria, y el orden de escritura debe preservarse para que el valor final sea el de la segunda instrucción en orden de programa.

> Un riesgo de tipo WAW… a) Se corresponde con una dependencia de salida b) Se corresponde con una dependencia de datos c) Se corresponde con una antidependencia d) Ninguna es correcta
> — `repo:datos/temarios/AC/examenes/Enero2015.pdf`

Relacionado: [[antidependencia-war-y-dependencia-de-salida-waw-definiciones]]

## Ampliación (2026-11-18, )
WAW (Write After Write): dos instrucciones escriben el mismo registro/memoria; la segunda debe escribir después de la primera para mantener el valor final correcto. Es dependencia de nombre, no de datos real.
