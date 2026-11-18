---
tipo: "receta"
titulo: "Análisis de dependencias en bucle MIPS con acceso a memoria"
temas: ["ac", "bucle", "dependencias", "mips", "pipeline"]
claves: ["L.D", "ADD.S", "S.D", "DADDUI", "BNEZ", "dependencia entre iteraciones"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2016.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[bucle]] · [[dependencias]] · [[mips]] · [[pipeline]]

En el bucle dado, S.D escribe en memoria (0(R1)) y DADDUI actualiza R1. La siguiente iteración usa R1 actualizado para L.D y S.D → dependencia de datos (RAW) en R1 entre iteraciones consecutivas. Clave para decidir desenrollamiento y planificación.

> Entre las instrucciones S.D y DADDUI... d) Existe una dependencia de datos, a través de R1, entre iteraciones
> — `repo:datos/temarios/AC/examenes/Enero2016.pdf` (cita sin comprobar)
