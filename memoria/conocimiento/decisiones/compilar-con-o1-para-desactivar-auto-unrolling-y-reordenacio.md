---
tipo: "decision"
titulo: "Compilar con -O1 para desactivar auto-unrolling y reordenación en experimentos de ILP"
temas: ["ac", "compilacion", "experimentacion", "gcc"]
claves: ["-O1", "auto-unrolling", "instruction reordering", "g++", "clang", "tarea4_1_ilp.cpp", "tarea4_1_ilp_opt.cpp"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Practica4.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[compilacion]] · [[experimentacion]] · [[gcc]]

Decisión metodológica explícita: usar `-O1` (no `-O2`/`-O3`) en las tareas 4.1 y 4.2 para que el compilador NO optimice automáticamente (loop unrolling, instruction scheduling, vectorización) y así aislar el efecto de la transformación manual del programador. Comandos dados:
```
g++ -O1 -o ilp_base tarea4_1_ilp.cpp
g++ -O1 -o ilp_opt tarea4_1_ilp_opt.cpp
```
Esto garantiza que cualquier mejora en IPC/cycles provenga exclusivamente del desenrollado manual o del código branchless escrito a mano.

> Compila tanto el código original (tarea4_1_ilp.cpp) como el generado, con el nivel de optimización -O1 (esto evitará que el compilador aplique Auto-Unrolling por su cuenta y enmascare el experimento).
> — `repo:datos/temarios/AC/Practicas/Practica4.pdf`

Relacionado: [[desenrollado-manual-manual-unrolling-con-4-acumuladores-para]] · [[calentamiento-warm-up-para-poblar-tlb-y-evitar-page-faults]] · [[por-que-o1-evita-que-el-compilador-enmascare-la-optimizacion]] · [[optimizacion-ilp-mediante-desenrollado-de-bucle-con-4-acumul]] · [[como-forzar-un-salto-condicional-real-en-gcc-para-medir-pred]]
