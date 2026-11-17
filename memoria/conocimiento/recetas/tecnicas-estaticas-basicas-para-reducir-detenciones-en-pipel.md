---
tipo: "receta"
titulo: "Técnicas estáticas básicas para reducir detenciones en pipeline"
temas: ["ac", "compilador", "optimizacion", "segmentacion"]
claves: ["replicación unidades funcionales", "segmentación unidades funcionales", "adelantamiento forwarding", "salto retardado delayed branch"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema2-Paralelismo a nivel de instruccion/Tema2-2026-2027.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[compilador]] · [[optimizacion]] · [[segmentacion]]

Tres recetas de compilador/arquitectura estática: (1) Riesgos estructurales → replicar la unidad (varias ALU) o segmentarla más (pipeline más profundo). (2) RAW → forwarding/adelantamiento: mover el resultado directamente de la etapa productora a la consumidora sin esperar a WB. (3) Control → delayed branch: rellenar la ranura de retardo del salto con instrucción útil (o NOP) decidida en tiempo de compilación.

> Técnicas básicas (estáticas) para reducir:  • Detenciones por riesgos estructurales: replicación o segmentación de las unidades funcionales  • Detenciones por riesgos de datos RAW: adelantamientos  • Detenciones por riesgos de control: saltos retardados
> — `repo:datos/temarios/AC/Tema2-Paralelismo a nivel de instruccion/Tema2-2026-2027.pdf`

Relacionado: [[problemas-en-segmentacion-de-coma-flotante-riesgos-estructur]]
