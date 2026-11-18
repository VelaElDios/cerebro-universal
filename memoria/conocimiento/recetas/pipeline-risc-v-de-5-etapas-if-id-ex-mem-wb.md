---
tipo: "receta"
titulo: "Pipeline RISC-V de 5 etapas: IF, ID, EX, MEM, WB"
temas: ["ac", "etapas", "pipeline", "risc-v"]
claves: ["IF búsqueda instrucción", "ID decodificación lectura registros", "EX ejecución cálculo dirección", "MEM acceso memoria datos", "WB escritura registro"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema2-Paralelismo a nivel de instruccion/Tema2-2026-2027.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[etapas]] · [[pipeline]] · [[risc-v]]

Las 5 etapas clásicas del pipeline RISC-V:
1. IF (Instruction Fetch): busca la instrucción en memoria de instrucciones; actualiza PC cada ciclo.
2. ID (Instruction Decode): decodifica y lee dos registros del banco (lectura en segunda mitad del ciclo).
3. EX (Execute): ALU opera o calcula dirección efectiva.
4. MEM (Memory): acceso a memoria de datos (load/store).
5. WB (Write Back): escribe resultado en registro (escritura en primera mitad del ciclo).
El banco de registros permite lectura y escritura en el mismo ciclo al usar mitades de ciclo opuestas. Se usan caches separadas para instrucciones y datos para evitar riesgos estructurales en memoria.

> 1.- IF → Búsqueda de la instrucción en memoria • 2.- ID → Decodificación y lectura de registros • 3.- EX → Ejecución de una operación o cálculo de una dirección • 4.- MEM → Acceso a un operando en la memoria de datos • 5.- WB → Escritura del resultado en un registro
> — `repo:datos/temarios/AC/Tema2-Paralelismo a nivel de instruccion/Tema2-2026-2027.pdf` (cita sin comprobar)

Relacionado: [[definicion-y-proposito-de-la-segmentacion-pipeline]] · [[banco-de-registros-en-pipeline-mips-se-accede-en-etapas-id-y]] · [[parametros-de-pipeline-in-order-5-etapas-para-analisis-de-ha]] · [[definicion-de-latencia-de-resolucion-de-salto-en-pipeline-5]]
