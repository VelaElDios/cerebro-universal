---
tipo: "fuente"
titulo: "tarea4 1 ilp (Code_Lab4)"
temas: ["ac"]
claves: []
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab4/tarea4_1_ilp.cpp"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]]

Documento aprendido: `repo:datos/temarios/AC/Practicas/Code_Lab4/tarea4_1_ilp.cpp`.

## Resumen
Este trozo contiene el código base de la práctica 4.1 de Arquitectura de Computadores sobre Paralelismo a Nivel de Instrucción (ILP). El programa evalúa cómo una cadena de dependencias secuencial (sumA += v[i]) limita el rendimiento del pipeline al estancar las ALUs. La tarea del alumno es optimizarlo mediante desenrollado de bucle manual (unrolling factor 4) con 4 acumuladores independientes para romper la cadena de dependencias, compilando con -O1 para evitar que el compilador optimice automáticamente, y comparando rendimiento con hyperfine y perf.

## Lo que se sacó de él (7)
- [[benchmarking-ilp-con-hyperfine-y-perf-para-medir-cycles-inst]]
- [[optimizacion-ilp-mediante-desenrollado-de-bucle-con-4-acumul]]
- [[parametros-fijos-del-experimento-ilp-n-100m-tipo-double-valo]]
- [[por-que-o1-evita-que-el-compilador-enmascare-la-optimizacion]]
- [[romper-cadena-de-dependencias-para-exponer-ilp-en-pipeline-s]]
- [[uso-de-double-en-lugar-de-float-para-acumulacion-en-experime]]
- [[verificacion-de-correccion-numerica-entre-version-base-y-opt]]
