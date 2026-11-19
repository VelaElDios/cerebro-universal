---
tipo: "decision"
titulo: "Uso de flag -O1 para evitar auto-unrolling del compilador en prácticas ILP"
temas: ["ac", "compilacion", "metodologia", "optimizacion"]
claves: ["-O1", "-O2", "-O3", "auto-unrolling", "loop unrolling", "compiler optimization"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab4.zip!tarea4_1_ilp.cpp"]
confianza: "propuesto"
fecha: "2026-11-19"
actualizado: "2026-11-19"
---

Temas: [[ac]] · [[compilacion]] · [[metodologia]] · [[optimizacion]]

Decisión pedagógica: compilar con -O1 en lugar de -O2/-O3 para que el compilador NO realice desenrollado automático de bucles (loop unrolling) ni vectorización automática. Si se usara -O2/-O3, GCC/Clang transformarían el bucle base en algo similar a la versión optimizada manualmente, anulando la diferencia de rendimiento que se quiere medir y demostrando erróneamente que la optimización manual no aporta nada. -O1 habilita optimizaciones básicas (inline, constant propagation) pero no loop unrolling agresivo ni vectorización.

> Generar ambos ejecutables usando el flag de optimización -O1 (evita que el auto-unrolling del compilador enmascare la prueba)
> — `repo:datos/temarios/AC/Practicas/Code_Lab4.zip!tarea4_1_ilp.cpp` (cita sin comprobar)

Relacionado: [[optimizacion-ilp-mediante-desenrollado-de-4-vias-con-acumula]]
