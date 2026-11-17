---
tipo: "concepto"
titulo: "Problemas en segmentación de coma flotante: riesgos estructurales RAW WAW y finalización fuera de orden"
temas: ["ac", "coma-flotante", "riesgos", "segmentacion"]
claves: ["riesgo estructural", "riesgo RAW", "riesgo WAW", "finalización fuera de orden", "excepciones"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema2-Paralelismo a nivel de instruccion/Tema2-2026-2027.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[coma-flotante]] · [[riesgos]] · [[segmentacion]]

Cuatro problemas principales al segmentar FP con unidades de latencia variable: (1) riesgos estructurales por compartir divisor o puerto de escritura en MEM; (2) penalización RAW amplificada porque las etapas EX son largas (p.ej., 6 ciclos en multiplicador); (3) riesgos WAW al escribir resultados fuera de orden; (4) finalización fuera de orden complica el tratamiento preciso de excepciones.

>    Aparecen riesgos estructurales (acceso a división, escritura MEM)           Mayor penalización de los riesgos RAW (etapas EX largas)           Pueden aparecer riesgos WAW           Finalización fuera de orden (tratamiento de excepciones)
> — `repo:datos/temarios/AC/Tema2-Paralelismo a nivel de instruccion/Tema2-2026-2027.pdf`

Relacionado: [[tabla-de-latencia-e-intervalo-de-iniciacion-por-unidad-funci]]
