---
tipo: "receta"
titulo: "Cómo resolver segmentación software (software pipelining) en MIPS64 con salto retardado y adelantamiento"
temas: ["ac", "mips64", "pipeline", "segmentacion-software"]
claves: ["software pipelining", "salto retardado", "adelantamiento", "start-up", "finish-up", "loop unrolling"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2013.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[mips64]] · [[pipeline]] · [[segmentacion-software]]

El problema 1 pide aplicar segmentación software a un bucle MIPS64 de 6 instrucciones (L.S, L.S, MUL.S, DADDUI, S.S, BNE) con la tabla de tiempos dada. Pasos: 1) Identificar latencias: L.S (MEM en ciclo 4), MUL.S (EX1-EX4 = 4 ciclos EX), DADDUI (EX en ciclo 1), S.S (MEM), BNE (EX resuelve salto). 2) Con salto retardado, la instrucción en el slot de retardo se ejecuta siempre. 3) Con adelantamiento, se evitan paradas por dependencias RAW. 4) Construir el kernel segmentado solapando iteraciones: iniciar nueva iteración cada ciclo de iniciación (II) mínimo posible. 5) Añadir código start-up (prologo) para llenar el pipeline y finish-up (epilogo) para vaciarlo. La tabla muestra I1-I6 con huecos (--) indicando burbujas por dependencias; el II mínimo viene dado por la recurrencia más larga (MUL.S 4 ciclos EX → II≥4).

> Aplica segmentación software al siguiente fragmento de código de MIPS64 (incluye el código start-up y finish-up)
> — `repo:datos/temarios/AC/examenes/Enero2013.pdf`

Relacionado: [[algoritmo-tomasulo-origen-y-objetivo-cpi1]] · [[estructura-y-funcionamiento-de-predictor-hibrido-de-torneo-c]]
