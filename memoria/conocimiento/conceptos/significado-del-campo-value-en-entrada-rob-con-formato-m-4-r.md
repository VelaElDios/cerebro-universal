---
tipo: "concepto"
titulo: "Significado del campo Value en entrada ROB con formato M(4+R3)"
temas: ["ac", "tomasulo"]
claves: ["ROB", "Reorder Buffer", "value field", "memory address calculation"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January 2025.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[tomasulo]]

La notación M(4+R3) indica una dirección de memoria efectiva: contenido de la entrada #4 del ROB (que es un valor producido por otra instrucción) más el registro R3. El valor final será el dato leído de esa dirección de memoria. Opción correcta: (b) The value read from the memory address that results from adding the value produced by the instruction in ROB entry #4 to the content of the R3 register.

> In the “Value” field of a ROB entry we have: “M(4+R3)”. This means that the value produced by the instruction in this ROB entry will be...
> — `repo:datos/temarios/AC/examenes/January 2025.pdf`

Relacionado: [[bits-venenosos-en-carga-especulativa-excepcion-diferida-hast]] · [[contenido-de-una-estacion-de-reserva-en-tomasulo-test-ac-q11]] · [[nomenclatura-del-campo-value-en-entradas-del-rob-tomasulo-co]] · [[estructura-de-tabla-rob-de-4-entradas-para-volcado-en-ciclo]] · [[buffer-de-reordenamiento-rob-en-tomasulo-con-especulacion-ca]]
