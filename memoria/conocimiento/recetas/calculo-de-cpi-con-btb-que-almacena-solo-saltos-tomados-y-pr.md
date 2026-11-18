---
tipo: "receta"
titulo: "Cálculo de CPI con BTB que almacena solo saltos tomados y predice NT si no está"
temas: ["ac", "pipeline", "prediccion-saltos"]
claves: ["BTB", "tasa acierto 95%", "solo saltos tomados", "predicción no tomado", "penalización actualización", "eliminación sin penalidad"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2016.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]] · [[prediccion-saltos]]

Modelo de BTB: hit rate 95% (entrada existe). Solo salta entradas para saltos TOMADOS (condicionales tomados + incondicionales). Políticas: (1) Hit en BTB → predice tomado, salta a dirección BTB. Si al resolver es tomado → OK (0 penalidad). Si al resolver es no tomado → fallo, elimina entrada, penalidad = latencia resolución (condicional: 3 ciclos; incondicional: 1 ciclo). (2) Miss en BTB → predice no tomado. Si al resolver es no tomado → OK (0 penalidad). Si al resolver es tomado → fallo, actualiza BTB con 1 ciclo de penalidad extra + latencia resolución normal. Cálculo CPI_BTB = 1 + Σ(casos_fallo × penalidad_caso). Hay que desglosar por tipo de salto (condicional/incondicional) y si está/ no está en BTB (95%/5% de los saltos que *deberían* estar en BTB, es decir, los tomados).

> b) Calcula el CPI si el sistema dispone de una BTB con las siguientes características (1 punto) : a. Tiene una tasa de aciertos del 95% (entrada encontrada en la BTB). b. Sólo almacena las direcciones de saltos tomados (incluyendo los saltos incondicionales). c. Si un salto condicional no está en BTB se predice como no tomado. d. Si una dirección se encuentra en el BTB pero el salto acaba siendo no tomado, la dirección es eliminada del BTB, sin penalización. e. Si una dirección no se encuentra en el BTB pero el salto finalmente es tomado (incluye los saltos incondicionales), el BTB se actualiza con un ciclo de penalización
> — `repo:datos/temarios/AC/examenes/Junio2016.pdf`

Relacionado: [[actualizacion-de-la-btb-tras-ejecutar-el-salto]] · [[bht-branch-history-table-tabla-separada-para-bits-de-predicc]]
