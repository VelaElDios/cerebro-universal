---
tipo: "concepto"
titulo: "Tres patrones de acceso a memoria para evaluar localidad de datos"
temas: ["ac", "cache", "localidad", "memoria"]
claves: ["acceso_secuencial", "acceso_temporal", "acceso_aleatorio", "localidad espacial", "localidad temporal", "prefetcher"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab3.zip!tarea2_1_patrones.cpp"]
confianza: "propuesto"
fecha: "2026-11-19"
actualizado: "2026-11-19"
---

Temas: [[ac]] · [[cache]] · [[localidad]] · [[memoria]]

El programa define tres patrones que realizan exactamente el mismo número total de accesos a memoria (N × REPETICIONES = 2²⁶ × 4 = 268.435.456 lecturas):
1. **Secuencial** (`acceso_secuencial`): Recorre el array lineal de principio a fin 4 veces. Aprovecha **localidad espacial** (líneas de caché contiguas) y el **prefetcher** hardware.
2. **Temporal** (`acceso_temporal`): Repite lecturas solo sobre los primeros `BLOQUE` (4096) elementos. Tras la primera pasada, todo cabe en **L1** → **localidad temporal máxima**.
3. **Aleatorio** (`acceso_aleatorio`): Accede a las mismas posiciones pero en orden permutado (semilla fija 42). Rompe localidad espacial y temporal → **peor caso** para caché y prefetcher.

> // PATRÓN 1: ACCESO SECUENCIAL Suma las posiciones v[0] + v[1] + ... + v[67108863] cuatro veces.(Localidad Espacial + Prefetcher)\n// PATRÓN 2: ACCESO TEMPORAL (Localidad Temporal Máxima)\n// PATRÓN 3: ACCESO ALEATORIO (El peor escenario posible)
> — `repo:datos/temarios/AC/Practicas/Code_Lab3.zip!tarea2_1_patrones.cpp` (cita sin comprobar)

Relacionado: [[analisis-de-dependencias-en-bucle-con-add-d-y-s-d-misma-iter]] · [[antidependencia-war-en-bucle-entre-carga-y-actualizacion-de]]
