---
tipo: "concepto"
titulo: "Bits de veneno (poison bits) en carga especulativa marcan registro destino ante fallo de permiso"
temas: ["ac", "especulacion", "excepciones-diferidas", "poison-bits", "tomasulo"]
claves: ["bits veneno", "carga especulativa", "lw*", "excepción", "permiso acceso", "registro destino"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2026.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[especulacion]] · [[excepciones-diferidas]] · [[poison-bits]] · [[tomasulo]]

La técnica de "poison bits" (bits de veneno) ante una excepción en instrucción especulativa (como fallo de permiso en dirección 0) no lanza la excepción inmediatamente. En su lugar, marca el registro destino (x5) con un bit de veneno. La excepción solo se materializa si/ cuando se intenta usar el valor de ese registro. Aquí x1=0 causa fallo en la carga, por lo que se activa el bit de veneno de x5 (registro destino de la carga), no de x1.

> Considera que en un procesador RISCV se ejecuta la instrucción especulativa lw* x5, 0(x1) haciendo uso de la técnica de Poisson para el manejo de excepciones. Sabemos que x1=0 y que a las direcciones de memoria 0 y 1 no se tiene permiso de acceso. Indica cuál de las siguientes afirmaciones es correcta: ... Siempre se activará el bit de veneno de x5
> — `repo:datos/temarios/AC/examenes/Junio2026.pdf` (cita sin comprobar)

Relacionado: [[bits-venenosos-en-carga-especulativa-excepcion-diferida-hast]] · [[bits-venenosos-en-especulacion-excepcion-no-recuperable-marc]] · [[buffer-de-carga-en-tomasulo-especulativo]]
