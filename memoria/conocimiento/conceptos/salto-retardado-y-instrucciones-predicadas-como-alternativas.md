---
tipo: "concepto"
titulo: "Salto retardado y instrucciones predicadas como alternativas a predicción"
temas: ["ac", "arquitectura", "compilador", "delay-slot", "instrucciones-predicadas", "prediccion-saltos", "salto-retardado"]
claves: ["salto retardado", "delay slot", "compilador rellena huecos", "cancelación", "instrucciones predicadas", "arquitectura evita saltos"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[arquitectura]] · [[compilador]] · [[delay-slot]] · [[instrucciones-predicadas]] · [[prediccion-saltos]] · [[salto-retardado]]

Dos alternativas a la predicción de saltos: 1) Salto retardado (delayed branch): el compilador rellena los "huecos de retardo" (delay slots) con instrucciones útiles que se ejecutan siempre, independientemente de si el salto se toma o no. Puede ser con cancelación (anular instrucciones en delay slot si salto no tomado) o sin cancelación. 2) Instrucciones predicadas: la arquitectura incluye instrucciones que se ejecutan condicionalmente según un predicado (registro de condición), eliminando la necesidad de saltos condicionales. Ejemplo: arquitectura IA-64 (EPIC/Itanium) usa predicación extensivamente.

> Salto retardado: El compilador rellena los huecos de retardo – con o sin cancelación – Instrucciones predicadas: Si la arquitectura puede evitar los saltos condicionales
> — `repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4.pdf` (cita sin comprobar)

Relacionado: [[planteamiento-general-de-prediccion-de-saltos-con-ejecucion]] · [[taxonomia-de-tecnicas-de-prediccion-de-saltos]] · [[instrucciones-predicadas-convertir-dependencias-de-control-e]] · [[ventajas-e-inconvenientes-de-las-instrucciones-predicadas]] · [[saltos-retardados-delayed-branches-en-planificacion-estatica]]
