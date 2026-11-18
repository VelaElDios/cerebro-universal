---
tipo: "concepto"
titulo: "Alto ILP requiere bajo grado de dependencia entre instrucciones"
temas: ["ac", "dependencias", "ilp"]
claves: ["paralelismo instruccion", "dependencias", "ILP"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Octubre2010.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[dependencias]] · [[ilp]]

El ILP (Instruction Level Parallelism) se limita por las dependencias verdaderas (RAW), de nombre (WAR, WAW) y de control. Menos dependencias = más instrucciones ejecutables en paralelo.

> Para lograr un alto grado de paralelismo a nivel de instrucción ... b) Es necesario que haya un bajo grado de dependencia entre las instrucciones
> — `repo:datos/temarios/AC/examenes/Octubre2010.pdf` (cita sin comprobar)

Relacionado: [[analisis-de-dependencias-en-bucle-con-add-d-y-s-d-misma-iter]]
