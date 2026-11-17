---
tipo: "decision"
titulo: "Predictor de 1 bit inicializado a no tomado en bucle secuencia 0,1,0,2"
temas: ["ac", "prediccion-saltos"]
claves: ["predictor 1 bit", "inicializado NT", "B1", "B2", "B3", "tasa aciertos definitiva"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2012.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[prediccion-saltos]]

Para cada salto (B1, B2, B3) hay un predictor de 1 bit independiente inicializado a NT (0). Comportamiento en estado estacionario: B1 (BEQZ R2): patrón T,NT,T,NT... (salta cuando R2==0). Predictor 1-bit alterna: falla en cada cambio → 50% aciertos. B2 (BEQZ R4): R4 = R2 & 1 → patrón NT,T,NT,T... (salta cuando R2 impar). Predictor 1-bit alterna → 50% aciertos. B3 (BEQ R1,R3): solo salta en la última iteración (una vez cada N iteraciones). Predictor 1-bit se queda en NT casi siempre → acierta casi siempre salvo en la última iteración → tasa → 100% para bucles largos. Tasa definitiva global: promedio ponderado según frecuencias.

> a) Predictores de 1 bit, inicializados a no tomado.
> — `repo:datos/temarios/AC/examenes/Enero2012.pdf`
