---
tipo: "concepto"
titulo: "Estructura de BTB: tabla de destinos y tabla separada de bits de predicción"
temas: ["ac", "prediccion-saltos"]
claves: ["BTB", "Branch Target Buffer", "tabla destinos", "bits predicción", "BHT"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2016.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[prediccion-saltos]]

El Branch Target Buffer (BTB) típicamente tiene dos estructuras: una caché de direcciones de destino (indexada por PC del salto) y una tabla separada de bits de predicción (BHT) para saltos condicionales. Esto permite predecir tanto si se toma como a dónde.

> Una BTB: c) Almacena en una tabla la dirección de destino de los últimos saltos y en otra los bits de predicción de todas las instrucciones de salto condicional
> — `repo:datos/temarios/AC/examenes/Junio2016.pdf` (cita sin comprobar)

Relacionado: [[actualizacion-de-la-btb-tras-ejecutar-el-salto]] · [[bht-branch-history-table-tabla-separada-para-bits-de-predicc]]
