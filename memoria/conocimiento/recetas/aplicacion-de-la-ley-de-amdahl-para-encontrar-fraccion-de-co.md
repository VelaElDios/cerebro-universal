---
tipo: "receta"
titulo: "Aplicación de la ley de Amdahl para encontrar fracción de código FP necesaria para un speedup dado"
temas: ["ac", "ley-amdahl", "punto-flotante", "rendimiento"]
claves: ["speedup", "fracción mejorada", "tiempo original", "amdahl"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2017.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[ley-amdahl]] · [[punto-flotante]] · [[rendimiento]]

Ley de Amdahl: Speedup_global = 1 / [(1 - f) + f/k], donde f = fracción de tiempo en código FP original, k = speedup_FP (4). Queremos Speedup_global = 2. Despejando: 2 = 1 / [(1-f) + f/4] → (1-f) + f/4 = 0.5 → 1 - 0.75f = 0.5 → 0.75f = 0.5 → f = 2/3. El tiempo original en FP = f × 100s = 66.6s (opción c).

> Supongamos que mejoramos una máquina haciendo que todas las instrucciones en punto flotante se ejecuten 4 veces más rápido. Estamos buscando un programa de prueba para medir el rendimiento de esta nueva máquina, que nos dé como resultado una ganancia en velocidad del doble. Si el programa de prueba tarda 100 segundos con el antiguo hardware en punto flotante ¿Qué cantidad de tiempo de ejecución inicial deberían tener las instrucciones en punto flotante?
> — `repo:datos/temarios/AC/examenes/Junio2017.pdf`

Relacionado: [[analisis-de-dependencias-en-bucle-con-add-d-y-s-d-misma-iter]]
