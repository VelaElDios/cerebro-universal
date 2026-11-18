---
tipo: "decision"
titulo: "Efecto de intervalo de iniciación 2 en multiplicador FP sobre código desenrollado"
temas: ["ac", "initiation-interval", "loop-unrolling", "pipeline", "unidad-funcional"]
claves: ["II=2", "fmul.d", "hazard estructural", "desenrollado 4x", "reordenación"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2026.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[initiation-interval]] · [[loop-unrolling]] · [[pipeline]] · [[unidad-funcional]]

Si el multiplicador FP pasa de II=1 a II=2, no se puede iniciar un fmul.d cada ciclo. En el código desenrollado 4x optimizado, si se programaron 4 fmul.d consecutivos (o con 1 ciclo de separación), ahora habrá hazard estructural (stall) cada 2 ciclos. Solución: aumentar distancia entre fmul.d insertando otras instrucciones (fadd.d, fsd, cargas de siguiente iteración) o desenrollar más (8x) para tener más instrucciones independientes entre muls. Si el schedule original ya tenía ≥2 ciclos entre muls, no afecta.

> Supón que, debido a restricciones de diseño, la unidad funcional de multiplicación FP tiene el comportamiento mostrado en la figura adjunta, pasando a tener un intervalo de iniciación de 2 ciclos. Explica si este diseño afecta al código que has diseñado en el apartado b. En caso afirmativo, indica qué cambios introducirías para evitar sus efectos; en caso negativo, justifica razonablemente por qué.
> — `repo:datos/temarios/AC/examenes/Junio2026.pdf` (cita sin comprobar)

Relacionado: [[desenrollado-4x-de-bucle-mips64-fp-con-renombrado-de-registr]] · [[desenrollado-minimo-de-bucle-mips64-para-eliminar-stalls-con]] · [[desenrollado-de-bucle-minimo-para-eliminar-todos-los-stalls]]
