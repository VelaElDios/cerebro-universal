---
tipo: "decision"
titulo: "Uso de ranura de retardo de 1 ciclo en superescalar para ocultar latencia de salto"
temas: ["ac", "delayed branch", "pipeline", "superscalar"]
claves: ["delay slot", "branch delay", "slot filling", "loop scheduling"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2020.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[delayed branch]] · [[pipeline]] · [[superscalar]]

Decisión de arquitectura: el procesador usa **delayed branch con 1 delay slot** en lugar de predicción de saltos (o además de). Implicaciones para planificación:
- La instrucción en el delay slot **siempre se ejecuta** antes de que el salto surta efecto.
- En bucles, la estrategia típica es colocar en el delay slot la **primera instrucción de la siguiente iteración** (ej. una carga o operación de índice) o la instrucción de **restauración de contador** (como `DADDUI R2, R0, #4` en el ejercicio 3).
- Si no hay instrucción útil, se pone NOP (penaliza CPI).
- En superescalar 3-vías, el delay slot ocupa la tubería Entero/Salto en el ciclo de emisión del salto. La instrucción del delay slot se emite en el **mismo ciclo** que el salto (ya que el salto se resuelve en ID/EX y el delay slot va en EX en el siguiente ciclo, pero en emisión van juntos).
- Al desenrollar bucles, el delay slot del salto final del bloque desenrollado puede rellenarse con código de la siguiente iteración desenrollada o con la restauración de contadores.

> As usual, assume that this processor supports forwarding and delayed branch (with 1 delay slot).
> — `repo:datos/temarios/AC/examenes/January2020.pdf`

Relacionado: [[definicion-de-latencia-de-salto-y-huecos-de-retardo]] · [[alternativas-de-deteccion-de-instruccion-de-salto-en-pipelin]] · [[salto-retardado-delayed-branch-en-planificacion-superescalar]] · [[saltos-retardados-delayed-branches-en-planificacion-estatica]] · [[uso-de-delayed-branch-con-1-delay-slot-en-vliw-para-ocultar]]
