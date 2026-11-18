---
tipo: "concepto"
titulo: "Banco de registros en pipeline MIPS de 5 etapas: acceso en ID (lectura) y WB (escritura)"
temas: ["ac", "banco-registros", "mips", "pipeline", "registros"]
claves: ["register bank", "ID stage", "WB stage", "pipeline", "MIPS64", "IF", "ID", "EX", "MEM", "WB", "lectura", "escritura", "registro"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June 2024.pdf", "repo:datos/temarios/AC/examenes/Junio2025.pdf", "repo:datos/temarios/AC/examenes/June2025.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[banco-registros]] · [[mips]] · [[pipeline]] · [[registros]]

Temas: [[ac]] · [[mips]] · [[pipeline]] · [[registros]] · [[banco-registros]]

En un pipeline clásico MIPS de 5 etapas (IF, ID, EX, MEM, WB), el banco de registros se lee en la etapa **ID** (Instruction Decode / Register Fetch, decodificación/lectura de operandos) y se escribe en la etapa **WB** (Write Back, escritura de resultado). El acceso ocurre en ID y WB, **no en IF, EX ni MEM**.

> The register bank in a pipelined processor is used in: d) The ID stage and the WB stage
> — `repo:datos/temarios/AC/examenes/June 2024.pdf` (cita sin comprobar)

> The register bank in a 5-stage pipelined MIPS processor is used in:
> — `repo:datos/temarios/AC/examenes/June2025.pdf`

## Ampliación (2026-11-18)
En el pipeline MIPS clásico de 5 etapas (IF, ID, EX, MEM, WB), el banco de registros se lee en la etapa ID (decodificación/lectura de operandos) y se escribe en la etapa WB (escritura de resultado). La opción correcta es d.

Relacionado: [[alternativas-de-deteccion-de-instruccion-de-salto-en-pipelin]] · [[definicion-de-latencia-de-instruccion-de-salto]] · [[banco-de-registros-en-pipeline-mips-se-accede-en-etapas-id-y]] · [[pipeline-risc-v-de-5-etapas-if-id-ex-mem-wb]] · [[definicion-de-latencia-de-resolucion-de-salto-en-pipeline-5]] · [[mips64-usa-caches-separadas-para-instrucciones-y-datos-harva]]
<<<CONTRADICCION>>
no

> The register bank in a pipelined processor is used in: d) The ID stage and the WB stage
> — `repo:datos/temarios/AC/examenes/June 2024.pdf` (cita sin comprobar)
> The register bank in a 5-stage pipelined MIPS processor is used in:
> — `repo:datos/temarios/AC/examenes/June2025.pdf`

Fusionada con: Etapas de uso del banco de registros en pipeline MIPS de 5 etapas
