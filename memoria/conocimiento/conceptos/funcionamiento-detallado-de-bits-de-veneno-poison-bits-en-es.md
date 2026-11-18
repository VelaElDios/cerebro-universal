---
tipo: "concepto"
titulo: "Funcionamiento detallado de bits de veneno (poison bits) en especulación"
temas: ["ac", "pipeline", "tomasulo"]
claves: ["poison bit", "dirty", "speculative exception", "deferred exception", "DDIV*"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2024.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]] · [[tomasulo]]

Cuando una instrucción especulativa (marcada con *) causa una excepción (p.ej. división por cero), el registro destino se marca como dirty (poison bit=1) y la ejecución continúa. Si posteriormente una instrucción no especulativa escribe en ese mismo registro (p.ej. DDIV R5, R2, R1), el valor se actualiza y el poison bit se pone a 0. Si el programa termina (o una instrucción no especulativa intenta leer el registro) mientras el poison bit sigue a 1, el registro permanece dirty y la excepción se materializa. En el ejemplo, con R2=1 (branch no tomado) la DDIV no especulativa limpia el bit; con R2=0 (branch tomado) la DDIV no especulativa no se ejecuta y R5 queda dirty al final.

> DDIV* R5, R1, R5               Yes                   No                             R5←dirty (poison bit=1)" y "DDIV    R5, R2, R1             No                    No                             R5←1 (poison bit=0)" y "R5      dirty
> — `repo:datos/temarios/AC/examenes/January2024.pdf` (cita sin comprobar)

Relacionado: [[bits-venenosos-en-carga-especulativa-excepcion-diferida-hast]] · [[comportamiento-de-bits-de-veneno-ante-instruccion-no-especul]]
