---
tipo: "concepto"
titulo: "Superescalar 3-vías con tuberías dedicadas por tipo de instrucción"
temas: ["ac", "functional units", "issue width", "pipeline", "superscalar"]
claves: ["3-way superscalar", "dedicated pipelines", "integer/branch pipe", "memory pipe", "floating-point pipe", "issue constraints"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2020.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[functional units]] · [[issue width]] · [[pipeline]] · [[superscalar]]

Modelo de emisión **3-vías asimétrico** (no simétrico como 3-vías genérico):
- **Tubería 0 (Entero/Salto)**: emite instrucciones enteras (ALU: DADDUI, etc.), saltos condicionales (BEQZ), saltos incondicionales (J). **1 instrucción/ciclo máx**.
- **Tubería 1 (Memoria)**: emite cargas (L.D) y stores (S.D). **1 instrucción/ciclo máx**.
- **Tubería 2 (Punto Flotante)**: emite operaciones FP (ADD.D, MUL.D, DIV.D, SUB.D). **1 instrucción/ciclo máx**.
Restricciones:
- No se pueden emitir 2 instrucciones del mismo tipo en el mismo ciclo (riesgo estructural de tubería).
- El orden de emisión en el ciclo no importa entre tuberías (son paralelas).
- Dependencias RAW entre tuberías se resuelven con **forwarding** (ej: resultado de FP en tubería 2 disponible para store en tubería 1 en ciclo siguiente).
- Saltos tienen **delay slot de 1**: la instrucción en delay slot se emite en la tubería correspondiente en el **mismo ciclo** que el salto (si es entero/salto, compite por tubería 0; si es memoria o FP, va a su tubería).
- Para planificar: construir tabla con columnas `Ciclo | Entero/Salto | Memoria | Punto Flotante` y rellenar respetando dependencias y latencias.

> Assume that we have a 3-way superscalar processor capable of issuing an integer instruction (including branches), a memory instruction, and a floating-point instruction per clock cycle.
> — `repo:datos/temarios/AC/examenes/January2020.pdf`

Relacionado: [[configuracion-vliw-de-6-unidades-funcionales-con-latencias-a]] · [[configuracion-superscalar-4-issue-para-diagramas-de-pipeline]] · [[planificacion-en-superscalar-mips64-4-vias-2-enteros-2-fp-co]] · [[planificacion-en-superescalar-3-vias-entero-salto-memoria-fp]]
