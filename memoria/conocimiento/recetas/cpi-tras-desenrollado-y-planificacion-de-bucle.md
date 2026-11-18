---
tipo: "receta"
titulo: "CPI tras desenrollado y planificación de bucle"
temas: ["ac", "bucles", "cpi", "optimizacion", "pipeline"]
claves: ["CPI", "cycles per instruction", "bucle desenrollado", "planificación"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2022.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[bucles]] · [[cpi]] · [[optimizacion]] · [[pipeline]]

CPI_final = (ciclos_ejecución_cuerpo_desenrollado + ciclos_salto) / (instrucciones_útiles_por_iteración_original * factor_desenrollado). En planificación ideal sin stalls, CPI tiende a 1/grado_superscalar si hay suficiente ILP. Para bucle desenrollado k veces con salto retardado: CPI = (ciclos_cuerpo_k_iteraciones) / (k * instr_originales).

> Calcula el valor del CPR para el bucle resultante (tras desenrollar y planificar).
> — `repo:datos/temarios/AC/examenes/Enero2022.pdf`

Relacionado: [[desenrollado-de-bucle-minimo-para-planificacion-sin-detencio]] · [[analisis-de-detenciones-stalls-en-bucle-con-media-ponderada]]
