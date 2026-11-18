---
tipo: "receta"
titulo: "Cálculo de tiempo de ejecución con CPI y mezcla de instrucciones"
temas: ["ac", "pipeline", "rendimiento"]
claves: ["CPI", "frecuencia reloj", "tiempo ejecución", "mezcla instrucciones"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2018.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]] · [[rendimiento]]

Para calcular el tiempo de ejecución: 1) Calcular ciclos totales = Σ (Instrucciones_i × CPI_i). 2) Tiempo = Ciclos totales / Frecuencia_reloj. En el ejemplo: Ciclos = (4e9×1) + (2e9×2) + (1e9×4) = 4e9 + 4e9 + 4e9 = 12e9 ciclos. Tiempo = 12e9 / 600e6 = 20 segundos. La respuesta correcta es b) 20 sg.

> Supongamos que medimos el código del programa para un compilador concreto y obtenemos los siguientes valores: Número de instrucciones (en miles de millones) A 4 B 2 C 1 ... frecuencia de reloj de la máquina es de 600Mhz. ¿Cuál será el tiempo de ejecución?
> — `repo:datos/temarios/AC/examenes/Junio2018.pdf` (cita sin comprobar)

Relacionado: [[algoritmo-tomasulo-origen-y-objetivo-cpi1]] · [[analisis-de-dependencias-en-bucle-con-add-d-y-s-d-misma-iter]] · [[calculo-de-tiempo-de-ejecucion-con-cpi-mixto-y-frecuencia-de]] · [[calculo-de-tiempo-de-ejecucion-con-cpi-frecuencia-e-instrucc]] · [[calculo-de-tiempo-de-ejecucion-con-cpi-y-frecuencia]]
