---
tipo: "receta"
titulo: "Análisis de detenciones (stalls) en bucle con media ponderada y cálculo de CPI"
temas: ["ac", "bucles", "cpi", "pipeline"]
claves: ["stalls", "detenciones", "media ponderada", "desenrollado bucle", "salto retardado", "CPI"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2022.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[bucles]] · [[cpi]] · [[pipeline]]

Para analizar stalls en un bucle: 1) Identificar dependencias RAW/WAR/WAW entre instrucciones consecutivas. 2) Considerar latencias de unidades funcionales (carga, FP add, FP mul). 3) Contar ciclos de burbuja insertados por hazard de datos o control. 4) CPI = (ciclos totales) / (instrucciones por iteración). El enunciado distingue "detenciones" (stalls reales en pipeline) de "dependencias" (peligros potenciales). El bucle calcula x̅ = (w1*x1 + w2*x2)/(w1+w2).

> Detalla las detenciones (ojo: NO LAS DEPENDENCIAS) que ocurren en el código al ejecutar cada iteración del bucle original y calcula el valor del CPR.
> — `repo:datos/temarios/AC/examenes/Enero2022.pdf`

Relacionado: [[configuracion-tomasulo-con-especulacion-para-examen-enero-20]]
