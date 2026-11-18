---
tipo: "concepto"
titulo: "Comportamiento de la BTB en caso de acierto (test AC Q14)"
temas: ["ac", "btac", "btb", "prediccion-saltos"]
claves: ["BTB", "branch-target-buffer", "acierto", "direccion-destino"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2025.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[btac]] · [[btb]] · [[prediccion-saltos]]

La **BTB (Branch Target Buffer)** fusiona la **BTAC (Branch Target Address Cache)** y los **bits de predicción** en una sola estructura cacheada por la dirección del salto (PC).
- **Acierto en BTB**: la entrada contiene la **dirección de destino predicha** y los bits de predicción. El fetch puede continuar inmediatamente desde esa dirección.
- **Fallo en BTB**: hay que calcular la dirección de destino (sumar offset al PC) y, si se toma, asignar una entrada en la BTB.
Por tanto, en acierto, **la BTB proporciona directamente la dirección de destino**.

> Un procesador emplea predicción de saltos apoyada en una BTB. En caso de acierto en la BTB… La BTB proporcionará la dirección de destino del salto actual
> — `repo:datos/temarios/AC/examenes/Enero2025.pdf` (cita sin comprobar)
