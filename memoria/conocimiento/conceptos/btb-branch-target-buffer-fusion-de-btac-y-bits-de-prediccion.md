---
tipo: "concepto"
titulo: "BTB (Branch Target Buffer): fusión de BTAC y bits de predicción en una sola estructura"
temas: ["ac", "arquitectura", "btb", "prediccion-saltos"]
claves: ["BTB", "Branch Target Buffer", "MC6860", "Pentium", "R8000", "dirección destino", "bits predicción"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[arquitectura]] · [[btb]] · [[prediccion-saltos]]

El BTB combina en una sola tabla: dirección destino del salto (como BTAC) + bits de predicción. En fase de captura se busca la instrucción en el BTB; si hay hit → se salta a la dirección destino guardada usando los bits de predicción para decidir tomado/no tomado. Es más compacto que tener BTAC+BHT separados. Ejemplos históricos: MC6860 (1993, 256 entradas × 2 bits), Pentium original 1994 (256×2), R8000 (1994, 1K×1), Pentium 1996 (512×2).

> La BTB almacena la dirección destino de los últimos saltos tomados y los bits de predicción de ese salto. La BTAC con bits de predicción se denomina BTB. MC6860 (1993) 256 x 2 bits Pentium (1994) 256 x 2 bits R8000 (1994) 1K x 1 bit Pentium (1996) 512 x 2 bits
> — `repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4.pdf` (cita sin comprobar)

Relacionado: [[bht-branch-history-table-tabla-separada-para-bits-de-predicc]]
