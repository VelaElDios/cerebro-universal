---
tipo: "concepto"
titulo: "Procesador A: MIPS64 superscalar 5 etapas, 4 emisiones/ciclo (2 int + 2 FP)"
temas: ["ac", "pipeline", "saas"]
claves: ["superscalar", "MIPS64", "issue width", "integer instructions", "floating-point instructions"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2021.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]] · [[saas]]

Características del procesador superscalar del enunciado:
- **Arquitectura**: MIPS64, pipeline de 5 etapas clásico (IF, ID, EX, MEM, WB).
- **Ancho de emisión**: 4 instrucciones/ciclo **máximo**.
- **Restricción de tipos**: de esas 4, **exactamente 2 deben ser enteras** (incluyen accesos a memoria L.D/S.D y saltos BNE) y **2 deben ser de punto flotante** (ADD.D, MUL.D, DIV.D, etc.).
- **Implicación para scheduling**: al desenrollar 8× el bucle (40 instrucciones: 8 L.D, 8 ADD.D, 8 S.D, 8 DADDUI, 8 BNE), hay 24 instrucciones enteras (8 L.D + 8 S.D + 8 DADDUI + 8 BNE = 32? Wait: L.D y S.D son memoria → enteras; DADDUI entero; BNE entero. Total enteras = 8+8+8+8 = 32. FP = 8 ADD.D. Pero el límite es 2 enteras + 2 FP por ciclo. Como solo hay 8 ADD.D (FP), el cuello de botella son las FP: se necesitan al menos 4 ciclos para emitir las 8 ADD.D a 2/ciclo. Las 32 enteras caben en 16 ciclos a 2/ciclo. El scheduling compacto debe entrelazar respetando latencias y límites de tipo por ciclo.

> Processor A. It is a MIPS64 5-stage superscalar processor, capable of issuing 4 instructions per cycle: two integer instructions (including memory accesses and branches) and two floating-point instructions.
> — `repo:datos/temarios/AC/examenes/January2021.pdf`

Relacionado: [[alternativas-de-deteccion-de-instruccion-de-salto-en-pipelin]]
