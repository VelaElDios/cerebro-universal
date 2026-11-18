---
tipo: "concepto"
titulo: "Predicción fija \"siempre no tomado\" con cálculo destino en ID y resolución en EX"
temas: ["ac", "mips-pipeline", "penalizacion", "prediccion-fija", "prediccion-saltos"]
claves: ["siempre no tomado", "penalizacion acierto fallo", "ID EX", "destino salto"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2013.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[mips-pipeline]] · [[penalizacion]] · [[prediccion-fija]] · [[prediccion-saltos]]

Pipeline MIPS: destino salto calculado en ID, sentido resuelto en EX. Predicción "siempre no tomado": si acierto (salto no tomado) → flujo secuencial correcto, 0 penalización. Si fallo (salto tomado) → se han metido 2 instrucciones erróneas (IF e ID del camino secuencial) que hay que vaciar → penalización 2 ciclos. Respuesta c).

> la estrategia de predicción fija 'siempre no tomado': c) No tiene penalización en caso de acierto y 2 ciclos en caso de fallo
> — `repo:datos/temarios/AC/examenes/Enero2013.pdf` (cita sin comprobar)

Relacionado: [[btb-branch-target-buffer-fusion-de-btac-y-bits-de-prediccion]] · [[ejecucion-multicamino-multi-path-execution-como-alternativa]]
