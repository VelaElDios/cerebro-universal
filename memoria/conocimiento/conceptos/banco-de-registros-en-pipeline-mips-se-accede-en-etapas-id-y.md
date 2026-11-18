---
tipo: "concepto"
titulo: "Banco de registros en pipeline MIPS: se accede en etapas ID y WB"
temas: ["ac", "mips", "pipeline", "registros"]
claves: ["register bank", "ID stage", "WB stage", "pipeline", "MIPS64"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June 2024.pdf", "repo:datos/temarios/AC/examenes/Junio2025.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[mips]] · [[pipeline]] · [[registros]]

En un pipeline clásico MIPS de 5 etapas (IF, ID, EX, MEM, WB), el banco de registros se lee en la etapa ID (lectura de operandos) y se escribe en la etapa WB (write back). La pregunta confirma que el acceso ocurre en ID y WB, no en IF ni EX ni MEM.

> The register bank in a pipelined processor is used in: d) The ID stage and the WB stage
> — `repo:datos/temarios/AC/examenes/June 2024.pdf` (cita sin comprobar)

Relacionado: [[alternativas-de-deteccion-de-instruccion-de-salto-en-pipelin]] · [[definicion-de-latencia-de-instruccion-de-salto]]

## Ampliación (2026-11-18, )
En el pipeline MIPS clásico de 5 etapas (IF, ID, EX, MEM, WB), el banco de registros se lee en la etapa ID (decodificación/lectura de operandos) y se escribe en la etapa WB (escritura de resultado). La opción correcta es d.
