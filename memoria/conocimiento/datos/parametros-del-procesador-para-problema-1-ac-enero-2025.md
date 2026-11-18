---
tipo: "dato"
titulo: "Parámetros del procesador para Problema 1 (AC Enero 2025)"
temas: ["ac", "cpi", "desenrollamiento-bucles", "pipeline"]
claves: ["etapa ID", "adelantamiento operandos", "salto retardado", "unidad entera 1 ciclo", "L.S/S.S 1 ciclo", "suma FP 2 ciclos", "multiplicación FP 3 ciclos", "MEM/WB compartido"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2025.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[cpi]] · [[desenrollamiento-bucles]] · [[pipeline]]

Definición del modelo de procesador para el Problema 1: Pipeline con resolución de saltos y dependencias en ID, forwarding, unidades FP segmentadas (ADD 2 ciclos, MUL 3 ciclos), L/S 1 ciclo, entero 1 ciclo. Regla de colisión estructural en MEM/WB solo si usan el mismo recurso exacto. Uso de salto retardado (delayed branch) en apartado c.

> El procesador presenta las características habituales: se puede escribir y leer un valor de un registro en el mismo ciclo de reloj, las dependencias se detectan y se resuelven en la etapa ID, soporta adelantamiento de operandos, los saltos condicionales se resuelven completamente en la etapa ID, la unidad funcional de enteros requiere 1 ciclo y la etapa de ejecución de L.S y S.S requiere 1 ciclo. Las unidades funcionales de suma y multiplicación en coma flotante están totalmente segmentas y requieren, respectivamente, 2 y 3 ciclos. Además, en este procesador dos instrucciones pueden coincidir en la etapa MEM o en la etapa WB siempre y cuando ambas instrucciones no estén usando exactamente el mismo recurso.
> — `repo:datos/temarios/AC/examenes/Enero2025.pdf`

Relacionado: [[algoritmo-tomasulo-origen-y-objetivo-cpi1]] · [[alternativas-de-deteccion-de-instruccion-de-salto-en-pipelin]]
