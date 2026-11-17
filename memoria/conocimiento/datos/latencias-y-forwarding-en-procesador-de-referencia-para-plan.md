---
tipo: "dato"
titulo: "Latencias y forwarding en procesador de referencia para planificación estática"
temas: ["ac", "forwarding", "latencias", "microarquitectura", "pipeline", "riesgos-datos"]
claves: ["FP ALU", "STORE FP", "LOAD FP", "ENTERA", "detenciones ciclos", "forwarding EX MEM ID", "latencia carga entera"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[forwarding]] · [[latencias]] · [[microarquitectura]] · [[pipeline]] · [[riesgos-datos]]

Tabla de riesgos de datos (stall cycles) para el procesador modelo del tema:
| Productor | Consumidor | Stall cycles |
|-----------|------------|--------------|
| FP ALU    | FP ALU     | 3            |
| FP ALU    | STORE FP   | 2            |
| LOAD FP   | FP ALU     | 1            |
| LOAD FP   | STORE FP   | 0            |
| ENTERA    | ENTERA     | 0            |

**Forwarding (adelantamiento)**: Existe desde etapas EX y MEM hacia ID (para saltos), EX y MEM.
**Saltos**: Retardo de 1 ciclo (delayed branch).
**Cargas enteras**: Latencia de 1 ciclo.
**Unidades funcionales**: Completamente segmentadas o replicadas.
Estos parámetros determinan la planificación estática óptima (ej. cuántas instrucciones intercalar entre `fld` y `fadd.d`).

> Instrucción que produce resultado | Instrucción que usa el resultado | Detenciones en ciclos | FP ALU | FP ALU | 3 | FP ALU | STORE FP | 2 | LOAD FP | FP ALU | 1 | LOAD FP | STORE FP | 0 | ENTERA | ENTERA | 0
> — `repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf` (cita sin comprobar)

Relacionado: [[calculo-de-flops-por-ciclo-en-x86-con-avx2-fma]]
