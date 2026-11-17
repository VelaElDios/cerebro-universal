---
tipo: "fuente"
titulo: "Tema2 2026 2027 (Tema2-Paralelismo a nivel de instruccion)"
temas: ["ac"]
claves: []
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema2-Paralelismo a nivel de instruccion/Tema2-2026-2027.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]]

Documento aprendido: `repo:datos/temarios/AC/Tema2-Paralelismo a nivel de instruccion/Tema2-2026-2027.pdf`.

## Resumen
Este trozo cubre la introducción al Tema 2 de Arquitectura de Computadores (curso 2026/2027): repaso de la ISA RISC-V (RV64G, registros, formato de instrucciones) y repaso de segmentación (pipeline de 5 etapas IF/ID/EX/MEM/WB, incremento ideal de velocidad, fórmula de speedup con detenciones, y los tres tipos de riesgos —estructurales, de datos RAW/WAW/WAR y de control— con sus técnicas de mitigación: adelantamiento, detección de riesgos de carga-uso y resolución anticipada de saltos en ID).
Este trozo cubre los fundamentos de segmentación en coma flotante (latencias, intervalos de iniciación, riesgos estructurales y de datos), la formulación del CPI como CPIideal + detenciones, y un catálogo de técnicas estáticas y dinámicas para reducir detenciones. Introduce el concepto de ILP y su relación con el CPI, las limitaciones del paralelismo en bloques básicos (15 % saltos, 5-7 instrucciones/bloque) y la necesidad de explotar paralelismo a nivel de bucle. Finalmente, define y ejemplifica los tres tipos de dependencias: de datos (verdaderas), de nombre (antidependencia y dependencia de
Este trozo final del Tema 2 cierra la clasificación de dependencias y sus riesgos asociados (RAW, WAR, WAW, control), y presenta tres técnicas clave para mitigarlas: renombrado de registros (estático o dinámico) para dependencias de nombre, desenrollado de bucles / eliminación de saltos para dependencias de control, y dos estrategias genéricas para dependencias de datos (mantener la dependencia evitando el riesgo, o eliminarla transformando el código). También muestra el índice del tema con las secciones 2.0–2.3 ya cubiertas.

## Lo que se sacó de él (25)
- [[adelantamiento-forwarding-para-riesgos-raw]]
- [[avance-del-temario-tema-2-secciones-2-02-3-completadas]]
- [[definicion-de-latencia-e-intervalo-de-iniciacion-en-pipeline]]
- [[definicion-y-proposito-de-la-segmentacion-pipeline]]
- [[dependencia-de-datos-verdadera-definicion-y-ejemplo-en-bucle]]
- [[dependencias-de-nombre-antidependencia-y-salida-definicion-y]]
- [[dos-estrategias-genericas-para-tratar-dependencias-de-datos]]
- [[eliminacion-de-dependencias-de-control-mediante-desenrollado]]
- [[isa-base-risc-v-rv64g-caracteristicas-principales]]
- [[limitacion-del-adelantamiento-hazard-load-use-load-use-penal]]
- [[limitaciones-del-paralelismo-en-bloques-basicos-y-solucion-a]]
- [[organizacion-del-banco-de-registros-en-risc-v-rv64g]]
- [[pipeline-risc-v-de-5-etapas-if-id-ex-mem-wb]]
- [[problemas-en-segmentacion-de-coma-flotante-riesgos-estructur]]
- [[relacion-ilp-y-cpi-en-procesadores-segmentados]]
- [[renombrado-de-registros-para-eliminar-dependencias-de-nombre]]
- [[riesgos-de-datos-en-risc-v-raw-waw-war]]
- [[riesgos-estructurales-causas-y-ejemplo-banco-de-registros]]
- [[speedup-ideal-vs-real-en-pipeline-y-formula-con-detenciones]]
- [[tabla-de-latencia-e-intervalo-de-iniciacion-por-unidad-funci]]
- [[tecnicas-avanzadas-estaticas-y-dinamicas-para-reducir-detenc]]
- [[tecnicas-estaticas-basicas-para-reducir-detenciones-en-pipel]]
- [[tipos-de-dependencia-y-riesgos-asociados-en-segmentacion]]
- [[tipos-de-riesgos-en-pipeline-estructurales-datos-control]]
- [[tres-tipos-de-dependencias-en-codigo-datos-nombre-y-control]]
