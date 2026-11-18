---
tipo: "concepto"
titulo: "Definición de procesador VLIW"
temas: ["ac", "ilp", "vliw"]
claves: ["VLIW", "compilador", "empaquetado", "instrucción larga"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2016.pdf", "repo:datos/temarios/AC/examenes/January2020.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[ilp]] · [[vliw]]

VLIW (Very Long Instruction Word): el compilador detecta paralelismo en tiempo de compilación y empaqueta operaciones independientes en una instrucción muy ancha. El hardware es simple (sin lógica de despacho dinámico), pero requiere recompilar para cada microarquitectura.

> Los procesadores VLIW son aquellos que: b) El compilador empaqueta múltiples operaciones en una única instrucción
> — `repo:datos/temarios/AC/examenes/Enero2016.pdf` (cita sin comprobar)

## Ampliación (2026-11-18, )
En VLIW (Very Long Instruction Word) el compilador agrupa operaciones independientes en una única instrucción larga (palabra de instrucción muy larga) que se ejecuta en paralelo en múltiples unidades funcionales. El hardware no necesita lógica compleja de despacho dinámico ni renombrado; la planificación es estática en tiempo de compilación. La opción correcta es b).
