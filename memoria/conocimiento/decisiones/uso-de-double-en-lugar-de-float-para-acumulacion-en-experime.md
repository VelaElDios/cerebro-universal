---
tipo: "decision"
titulo: "Uso de double en lugar de float para acumulación en experimento ILP"
temas: ["ac", "floating-point", "precision"]
claves: ["double", "float", "precision", "accumulation", "floating point"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab4/tarea4_1_ilp.cpp"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[floating-point]] · [[precision]]

**Decisión de diseño**: El código usa `double` (64-bit) para el vector y los acumuladores, aunque los literales son `1.0f` y `0.0f` (float).

**Razones probables**:
1. **Precisión en acumulación masiva**: Sumar 100M veces 1.0 en `float` (24 bits mantisa ≈ 7 dígitos) pierde precisión al superar ~16M (2^24). En `double` (53 bits mantisa ≈ 15 dígitos) no hay pérdida hasta ~9×10^15.
2. **Latencia FP add similar**: En x86 moderno, `addsd` (double) y `addss` (float) tienen misma latencia (~3-4 ciclos) y throughput (0.5-1/ciclo).
3. **Ancho de banda memoria**: `double` usa 2× ancho de banda vs `float`, haciendo el test más memory-bound y realista para cargas HPC.

**Nota**: Los literales `1.0f`/`0.0f` se convierten implícitamente a double. No hay penalización runtime.

> std::vector<double> v(N, 1.0f); double sumA = 0.0f;
> — `repo:datos/temarios/AC/Practicas/Code_Lab4/tarea4_1_ilp.cpp` (cita sin comprobar)

Relacionado: [[optimizacion-ilp-mediante-desenrollado-de-bucle-con-4-acumul]] · [[parametros-fijos-del-experimento-ilp-n-100m-tipo-double-valo]] · [[verificacion-de-correccion-numerica-entre-version-base-y-opt]]
