---
tipo: "concepto"
titulo: "Instrucción especulativa: ejecutada antes de saber si realmente debe ejecutarse"
temas: ["ac", "especulacion", "prediccion-saltos"]
claves: ["instruccion especulativa", "especulacion", "definicion"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2019.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[especulacion]] · [[prediccion-saltos]]

Una instrucción especulativa es aquella que se ejecuta (o se inicia su ejecución) antes de que se sepa con certeza que su ejecución es correcta (p. ej., instrucciones tras un salto predicho tomado). Si la predicción falla, sus efectos deben descartarse (flush) sin alterar el estado arquitectónico.

> A speculative instruction… c) Is an instruction executed before knowing whether it should actually be executed
> — `repo:datos/temarios/AC/examenes/January2019.pdf` (cita sin comprobar)

Relacionado: [[bits-venenosos-en-carga-especulativa-excepcion-diferida-hast]]
