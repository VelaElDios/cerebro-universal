---
tipo: "dato"
titulo: "Parámetros fijos del experimento de branchless (TAMANIO, REPETICIONES, semilla)"
temas: ["ac", "benchmark", "experimentacion"]
claves: ["TAMANIO=32768", "REPETICIONES=1000", "semilla=42", "mt19937", "uniform_int_distribution"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab4/tarea4_2_branchless.cpp"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[benchmark]] · [[experimentacion]]

Valores hard-coded en el benchmark:
- `TAMANIO = 32768` elementos (vector de `int` → 128 KiB, cabe en L2).
- `REPETICIONES = 1000` iteraciones del bucle externo (amortigua ruido de reloj).
- Generador: `std::mt19937` con semilla **42** (reproducible).
- Distribución: `uniform_int_distribution<int>(0, 255)` → umbral 128 divide ~50 %.
- Copia ordenada: `std::sort` ascendente → predictor aprende patrón "todos falsos, luego todos verdaderos".

> constexpr int TAMANIO = 32768; constexpr int REPETICIONES = 1000; std::mt19937 rng(42); std::uniform_int_distribution<int> dist(0, 255);
> — `repo:datos/temarios/AC/Practicas/Code_Lab4/tarea4_2_branchless.cpp` (cita sin comprobar)

Relacionado: [[patron-aleatorio-peor-caso-con-permutacion-fija-de-indices-s]] · [[parametros-fijos-del-benchmark-semilla-accesos-formato-salid]] · [[parametros-del-experimento-tamano-de-datos-bloque-y-repetici]] · [[parametros-fijos-del-experimento-aos-soa-tarea-3-2]]
