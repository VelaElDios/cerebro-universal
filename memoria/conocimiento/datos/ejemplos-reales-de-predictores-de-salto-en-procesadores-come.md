---
tipo: "dato"
titulo: "Ejemplos reales de predictores de salto en procesadores comerciales (PowerPC, UltraSPARC, Pentium, Pentium Pro)"
temas: ["ac", "arquitectura", "ejemplos", "prediccion-saltos", "procesadores"]
claves: ["PowerPC 604", "PowerPC 620", "UltraSPARC", "Pentium", "Pentium Pro", "Core i7", "BTB", "BHT", "PHT", "Yeh's Algorithm"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[arquitectura]] · [[ejemplos]] · [[prediccion-saltos]] · [[procesadores]]

Resumen de implementaciones reales: PowerPC 604 (1994): BTB 64 entradas fully-associative + PHT 512 entradas direct-mapped (two-level). PowerPC 620 (1995): BTB 256 entradas 2-way set-assoc + buffer predicción direct-mapped desacoplado. UltraSPARC: esquema 2-bit simple. Pentium (1994): BTB 256 entradas 4-way set-assoc + predictor 2-bit por entrada (one-level). Pentium Pro (1996): BTB 512 entradas 4-way set-assoc + historial local 4-bit por entrada → mapeado a PHT global (implementa algoritmo de Yeh, two-level adaptativo). Core i7: remite a H&P 5ª ed. pág. 166.

> The PowerPC604: has a 64 entry fully associative Branch Target Buffer for predicting the Branch Target Address and a decoupled direct mapped 512 entry Pattern History Table. The PowerPC620 has a 256-entry two-way set associative Branch Target Buffer for predicting the Branch Target Address and a decoupled direct mapped branch prediction buffer. The UltraSPARC is reported to have a 2-bit branch prediction scheme. The Intel Pentium contains a 256 entry 4-way set associative Branch Target Buffer. Coupled with each Branch Target Buffer entry is a 2-bit branch predictor. The Intel Pentium Pro works with a 512 entry 4-way set associative Branch Target Buffer. Coupled with each Branch Target Buffer entry is in this case a 4-bit local branch history. This is mapped in a second level onto a Global Pattern History Table, thus implementing Yeh's Algorithm
> — `repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4.pdf` (cita sin comprobar)

Relacionado: [[btb-branch-target-buffer-fusion-de-btac-y-bits-de-prediccion]] · [[bht-branch-history-table-tabla-separada-para-bits-de-predicc]] · [[estructura-de-btb-tabla-de-destinos-y-tabla-separada-de-bits]]
