---
tipo: "fuente"
titulo: "June2018 (examenes)"
temas: ["ac"]
claves: []
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2018.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]]

Documento aprendido: `repo:datos/temarios/AC/examenes/June2018.pdf`.

## Resumen
Este trozo contiene el examen final de Arquitectura de Computadores de junio 2018: 30 preguntas tipo test sobre ley de Amdahl, CPI, dependencias, pipeline, planificación estática/dinámica, Scoreboard, Tomasulo, predicción de saltos, ROB, especulación, superscalar, Itanium, GPUs, multihilo, vectores, taxonomía de Flynn y GRID; además de tres ejercicios prácticos: (1) análisis de stalls y desenrollado de bucle en MIPS64 con FP multiplier (3 ciclos) y divider (4 ciclos), (2) simulación paso a paso de Scoreboard vs. Tomasulo básico con latencias dadas, y (3) inicio de ejercicio superscalar de 2 em
Este trozo presenta un ejercicio de arquitectura de computadores (examen AC June 2018) que pide desenrollar 4 veces un bucle vectorial de operaciones en punto flotante (carga, multiplicación, suma, almacenamiento) y planificarlo para minimizar ciclos, dado un procesador con una unidad funcional por tipo de operación FP, dos unidades enteras de latencia 0 y una tabla de latencias entre instrucciones productoras y consumidoras. También pide calcular los ciclos por iteración del código original y el speedup de la versión desenrollada y planificada.

## Lo que se sacó de él (15)
- [[antidependencia-war-siempre-genera-hazard-war]]
- [[bucle-vectorial-de-referencia-para-desenrollado-y-planificac]]
- [[calculo-de-speedup-con-ley-de-amdahl-para-instrucciones-de-p]]
- [[calculo-de-tiempo-de-ejecucion-con-cpi-mixto-y-frecuencia-de]]
- [[como-calcular-ciclos-por-iteracion-del-codigo-original-con-l]]
- [[comparacion-de-eficiencia-entre-pentium-iii-1-ghz-y-pentium]]
- [[comportamiento-de-bit-de-veneno-poison-bit-ante-excepcion-en]]
- [[configuracion-del-procesador-para-el-ejercicio-de-desenrolla]]
- [[desenrollado-4x-y-planificacion-minima-para-bucle-fp-con-lat]]
- [[desenrollado-minimo-de-bucle-mips64-para-eliminar-stalls-con]]
- [[itanium-ia64-primer-procesador-intel-no-compatible-con-x86]]
- [[predictor-correlacionante-m-n-tiene-2-n-bhts]]
- [[simulacion-scoreboard-vs-tomasulo-basico-pasos-de-ejecucion]]
- [[speedup-teorico-del-desenrollado-4x-frente-a-codigo-original]]
- [[tabla-de-latencias-entre-instrucciones-productoras-y-consumi]]
