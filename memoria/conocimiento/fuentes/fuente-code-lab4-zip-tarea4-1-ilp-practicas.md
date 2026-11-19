---
tipo: "fuente"
titulo: "Code Lab4.zip!tarea4 1 ilp (Practicas)"
temas: ["ac"]
claves: []
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab4.zip!tarea4_1_ilp.cpp"]
confianza: "verificado"
fecha: "2026-11-19"
actualizado: "2026-11-19"
---

Temas: [[ac]]

Documento aprendido: `repo:datos/temarios/AC/Practicas/Code_Lab4.zip!tarea4_1_ilp.cpp`.

## Resumen
Este trozo es el código base de una práctica de Arquitectura de Computadores (Tarea 4.1) que ilustra cómo una cadena de dependencias de datos secuencial (acumulación en una sola variable) limita el ILP al provocar stalls en el pipeline. El enunciado guía al alumno para optimizarlo mediante desenrollado manual de 4 vías con 4 acumuladores independientes (acc1..acc4), rompiendo la dependencia y permitiendo explotar múltiples ALUs. Se compila con -O1 para evitar auto-unrolling del compilador y se valida con hyperfine/perf comparando ciclos, instrucciones e IPC.

## Lo que se sacó de él (6)
- [[dependencia-raw-en-acumulacion-secuencial-limita-ilp-en-pipe]]
- [[metodologia-de-benchmarking-ilp-con-hyperfine-y-perf-en-prac]]
- [[optimizacion-ilp-mediante-desenrollado-de-4-vias-con-acumula]]
- [[parametros-fijos-de-la-practica-ilp-n-100m-elementos-vector]]
- [[reduccion-final-de-acumuladores-parciales-tras-desenrollado]]
- [[uso-de-flag-o1-para-evitar-auto-unrolling-del-compilador-en]]
