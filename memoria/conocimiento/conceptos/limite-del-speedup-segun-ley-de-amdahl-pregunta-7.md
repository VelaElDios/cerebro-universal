---
tipo: "concepto"
titulo: "Límite del speedup según ley de Amdahl (pregunta 7)"
temas: ["ac", "amdahl", "rendimiento"]
claves: ["speedup", "ley Amdahl", "fracción tiempo mejora"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Noviembre2012.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[amdahl]] · [[rendimiento]]

La ley de Amdahl establece que el speedup máximo = 1 / ((1 - f) + f/s), donde f es la fracción de tiempo que usa la mejora y s el factor de aceleración de esa parte. Por tanto, el speedup está limitado por la fracción de tiempo que puede beneficiarse de la mejora (f), no por CPI ni frecuencia de reloj.

> El speedup obtenido al utilizar una mejora en un ordenador está limitado por: c) La fracción de tiempo que puede utilizarse la mejora
> — `repo:datos/temarios/AC/examenes/Noviembre2012.pdf` (cita sin comprobar)
