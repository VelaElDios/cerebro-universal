---
tipo: "fuente"
titulo: "January2024 (examenes)"
temas: ["ac"]
claves: []
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2024.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]]

Documento aprendido: `repo:datos/temarios/AC/examenes/January2024.pdf`.

## Resumen
Examen final de Arquitectura de Computadores (enero 2024) con 30 preguntas tipo test y un ejercicio de pipeline MIPS64. El test cubre: organización vs arquitectura, benchmarks (Linpack/TOP500), ley de Amdahl, cálculo de MIPS, renombrado de registros, dependencias en pipeline (RAW/WAR/WAW), Scoreboard, algoritmo Tomasulo (estaciones de reserva), trace scheduling, predicción de saltos (slots de retardo, CPI/IPC, latencia), predicción dinámica, ejecución especulativa, ROB, desambiguación de memoria, VLIW, superscalar, desenrollado de bucles, Itanium, arquitecturas load/store (ARM/RISC-V/Alpha), S
Este trozo contiene dos ejercicios de un examen de Arquitectura de Computadores (enero 2024). El Ejercicio 2 pide planificar una secuencia de instrucciones MIPS64 (cargas, operaciones FP, almacenamientos) en un procesador con algoritmo Tomasulo con especulación, ROB de 4 entradas, latencias dadas (carga/almacén 2 ciclos, multiplicación FP 7, suma FP 3) y reglas de bus CDB. El Ejercicio 3 analiza tres mecanismos de manejo de excepciones en instrucciones especulativas (sin soporte, cooperación HW/SW, bits de veneno) sobre un código con una división especulativa DDIV* que divide por cero, evaluan

## Lo que se sacó de él (17)
- [[arquitecturas-load-store-arm-risc-v-y-alpha]]
- [[calculo-de-speedup-por-desenrollado-de-bucle-en-superscalar]]
- [[configuracion-de-procesador-tomasulo-con-especulacion-del-ej]]
- [[definicion-de-instruccion-especulativa]]
- [[definicion-de-latencia-de-instruccion-de-salto]]
- [[determinar-salto-no-salto-de-bne-tras-instruccion-especulati]]
- [[estructura-del-reorder-buffer-rob-en-tomasulo-con-especulaci]]
- [[funcionamiento-detallado-de-bits-de-veneno-poison-bits-en-es]]
- [[mecanismo-de-cooperacion-hardware-software-para-excepciones]]
- [[primer-procesador-intel-no-compatible-con-x86-itanium]]
- [[problema-de-desambiguacion-de-memoria-memory-disambiguation]]
- [[que-es-una-estacion-de-reserva-en-el-algoritmo-de-tomasulo]]
- [[que-ocurre-cuando-un-salto-mal-predicho-llega-al-tope-del-ro]]
- [[que-representa-un-trace-en-trace-scheduling]]
- [[que-resuelve-el-renombrado-de-registros-register-renaming]]
- [[tres-mecanismos-de-manejo-de-excepciones-para-instrucciones]]
- [[valores-de-registros-y-flujo-de-control-en-ejemplo-ddiv-espe]]
