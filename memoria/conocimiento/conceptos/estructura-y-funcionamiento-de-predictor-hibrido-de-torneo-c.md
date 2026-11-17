---
tipo: "concepto"
titulo: "Estructura y funcionamiento de predictor híbrido de torneo con predictor local 2-bit y global (1,2)"
temas: ["ac", "prediccion-saltos", "predictor-global", "predictor-hibrido", "predictor-local", "selector-2-bits", "torneo"]
claves: ["predictor local 2 bits 1 entrada", "predictor global (1", "2) BHT 2 entradas indexadas por LSB dirección", "selector contador 2 bits saturado incrementa si tomado decrementa si no tomado", "local si selector 0/1 global si 2/3", "actualiza solo predictor usado"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4_Prob.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[prediccion-saltos]] · [[predictor-global]] · [[predictor-hibrido]] · [[predictor-local]] · [[selector-2-bits]] · [[torneo]]

Bloques: 1) Predictor Local: tabla indexada por PC (o parte), cada entrada contador 2 bits. 2) Predictor Global: Registro Historia Global (1 bit) -> indexa BHT de 2 contadores 2 bits. 3) Selector: Tabla indexada por PC, cada entrada contador 2 bits (0-3). 4) Mux: selector MSB decide salida. Inicialización: BHTs local y global a "débilmente no tomado" (01). Selector a 0. Direcciones: B1=0x654 (LSB=0), B2=0x623 (LSB=1). Secuencia datos: 3,2,5,4,6 (5 elementos). Simular paso a paso llenando tabla de evolución.

> Se hace uso de un predictor híbrido de Torneo con predictor local 2-bits de 1 entrada para cada salto y, un predictor global (1,2) en el que las tablas BHT tienen 2 entradas indexadas por el bit de menor peso de la dirección de salto de la instrucción. El selector es un contador de 2 bits saturado que incrementa su valor cuando el salto se toma y decrementa cuando el salto no se toma. El predictor local se usa cuando el selector vale 0 o 1 y el predictor global cuando vale 2 o 3. Ante un salto sólo se actualiza el predictor empleado en la predicción.
> — `repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4_Prob.pdf`

Relacionado: [[bht-branch-history-table-tabla-separada-para-bits-de-predicc]] · [[btb-branch-target-buffer-fusion-de-btac-y-bits-de-prediccion]]
