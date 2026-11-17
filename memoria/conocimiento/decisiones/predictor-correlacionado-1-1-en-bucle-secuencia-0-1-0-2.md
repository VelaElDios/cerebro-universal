---
tipo: "decision"
titulo: "Predictor correlacionado (1,1) en bucle secuencia 0,1,0,2"
temas: ["ac", "prediccion-saltos"]
claves: ["predictor correlacionado (1", "1)", "BHR 1 bit", "BHT 2 entradas", "historia anterior NT"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2012.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[prediccion-saltos]]

Predictor correlacionado (m=1, n=1): BHR de 1 bit (historia del salto anterior), BHT con 2 entradas (índice = BHR), cada entrada es un predictor de 1 bit inicializado a NT. El salto anterior al primer B1 es NT (dado). Secuencia de saltos dinámicos: B1, B2, B3, B1, B2, B3... (J no se predice). Se simula ciclo a ciclo actualizando BHR tras cada salto. Al ser historia de 1 bit, el predictor usa el resultado del salto inmediatamente anterior para indexar la BHT. Esto permite capturar correlación local entre saltos consecutivos. La tasa de aciertos definitiva depende de si la correlación (B1→B2, B2→B3, B3→B1) es explotable con 1 bit de historia.

> b) Predictor correlacionado (1, 1), considerando que cuando comienza la ejecución del bucle, el salto anterior ha sido no tomado, y el estado inicial de todos los predictores es no tomado.
> — `repo:datos/temarios/AC/examenes/Enero2012.pdf`

Relacionado: [[predictor-de-1-bit-inicializado-a-no-tomado-en-bucle-secuenc]]
