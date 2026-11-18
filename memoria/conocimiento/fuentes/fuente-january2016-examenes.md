---
tipo: "fuente"
titulo: "January2016 (examenes)"
temas: ["ac"]
claves: []
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2016.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]]

Documento aprendido: `repo:datos/temarios/AC/examenes/January2016.pdf`.

## Resumen
Este trozo contiene el examen final de Arquitectura de Computadores de enero 2016: 30 preguntas tipo test (unidades 1-8 y 5-8) y tres ejercicios. El test cubre CPI/tiempo ejecución, ley de Amdahl, arquitectura vs organización, VLIW, dependencias de datos (RAW, WAW, WAR), renombrado de registros, algoritmo Tomasulo, planificación estática/dinámica, predicción de saltos (dos niveles, gselect, BTAC), Tomasulo especulativo con bits de veneno, buffer de reordenación (ROB), superescalar CPI ideal, etapa commit, ARM, disipación potencia, Pentium II/Celeron/Xeon, multicore, taxonomía Flynn (GPU=SIMD),
Este trozo contiene el Ejercicio 3 de un examen de arquitectura de computadores (enero 2016). Plantea un problema de planificación VLIW: un bucle con instrucciones de punto flotante (carga, almacenamiento, ADD.D, MUL.D, DIV.D) e enteras (DADDUI, BNEZ) que debe desenrollarse 4 veces y planificarse en un procesador VLIW de 4 operaciones/ciclo con forwarding y salto retardado. Se dan latencias: 2 ciclos en MEM para carga/almacenamiento, 2 ciclos en EX para aritmética, 1 ciclo para el resto. Se pide el diagrama de ciclos 1-20 y las operaciones por ciclo alcanzadas.

## Lo que se sacó de él (17)
- [[calculo-de-operaciones-por-ciclo-ipc-en-planificacion-vliw]]
- [[calculo-de-tiempo-de-ejecucion-a-partir-de-instrucciones-cpi]]
- [[caracteristicas-clave-de-procesadores-vliw]]
- [[como-resolver-planificacion-vliw-con-desenrollado-y-latencia]]
- [[definicion-de-dependencia-de-datos-raw-entre-instrucciones]]
- [[delayed-branch-en-vliw-y-su-efecto-en-planificacion]]
- [[dependencia-entre-iteraciones-en-bucle-con-s-d-y-daddui-sobr]]
- [[dependencias-en-fragmento-de-codigo-fp-mips-l-d-add-s-add-s]]
- [[diferencia-entre-arquitectura-y-organizacion-de-computadores]]
- [[eliminacion-de-dependencias-de-nombre-mediante-renombrado-de]]
- [[factor-de-mejora-necesario-segun-ley-de-amdahl-para-un-speed]]
- [[forwarding-en-vliw-estatico-y-latencias-efectivas]]
- [[parametros-de-temporizacion-vliw-examen-enero-2016]]
- [[planificacion-estatica-vs-dinamica-de-codigo]]
- [[problema-de-planificacion-vliw-con-desenrollado-de-bucle-exa]]
- [[valores-iniciales-de-registros-del-bucle-examen-enero-2016]]
- [[waw-hazard-corresponde-a-dependencia-de-salida]]
