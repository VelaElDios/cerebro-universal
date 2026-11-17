---
tipo: "receta"
titulo: "Evaluación de rendimiento de BTB con política de solo saltos tomados, hit rate 90%, actualización en fallo con penalidad"
temas: ["ac", "btb", "cpi", "penalidad-actualizacion", "prediccion-saltos"]
claves: ["BTB", "solo saltos tomados", "hit rate 90%", "eliminacion si no tomado", "actualizacion en MEM/EX con 1 ciclo penalidad", "IF ID EX MEM WB"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4_Prob.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[btb]] · [[cpi]] · [[penalidad-actualizacion]] · [[prediccion-saltos]]

Pipeline: IF, ID, EX, MEM, WB. Dirección salto fin ID, sentido fin EX. Sin BTB: asumir predicción estática (ej. no tomado) -> penalidad si tomado = ciclos desde IF hasta EX = 2 ciclos (IF, ID, EX) ? O flush pipeline. Ejercicio dice: "dirección conocida al final de ID, sentido al final de EX". Si no se predice, se fetchea secuencial. Si salto tomado, se pierden instrucciones en IF, ID (2 ciclos). Frecuencia: condicionales 20% (60% tomados), incondicionales 5% (100% tomados). Con BTB: Hit 90% en saltos tomados (BTB solo guarda tomados). Si hit y tomado -> dirección disponible fin ID? BTB se consulta en IF? Asumir BTB da target en IF. Si hit y tomado: 0 penalidad. Si hit pero no tomado (solo condicionales): se elimina entrada, 0 penalidad (dice "sin penalización"). Si miss y tomado: actualizar BTB en MEM (cond) o EX (incond) con 1 ciclo penalidad (stall). Calcular CPI medio con y sin BTB. Speedup = CPI_sin / CPI_con.

> Compara el rendimiento del sistema con y sin BTB.
> — `repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4_Prob.pdf`

Relacionado: [[btb-branch-target-buffer-fusion-de-btac-y-bits-de-prediccion]] · [[alternativas-de-deteccion-de-instruccion-de-salto-en-pipelin]]
