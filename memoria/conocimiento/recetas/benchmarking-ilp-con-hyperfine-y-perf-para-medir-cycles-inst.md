---
tipo: "receta"
titulo: "Benchmarking ILP con hyperfine y perf para medir cycles, instructions e IPC"
temas: ["ac", "benchmarking", "hyperfine", "ipc", "perf"]
claves: ["hyperfine", "perf stat", "cycles", "instructions", "IPC", "benchmarking"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab4/tarea4_1_ilp.cpp"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[benchmarking]] · [[hyperfine]] · [[ipc]] · [[perf]]

**Pasos de benchmarking**:

1. **Instalar herramientas** (Ubuntu/Debian):
   ```bash
   sudo apt install hyperfine linux-tools-common linux-tools-$(uname -r)
   ```

2. **Medir tiempo de ejecución** con hyperfine (ejecuta múltiples runs, calienta caché, da estadísticas):
   ```bash
   hyperfine --warmup 3 './ilp_base' './ilp_opt'
   ```

3. **Medir contadores hardware** con perf (requiere root o kernel.perf_event_paranoid=-1):
   ```bash
   perf stat -e cycles,instructions ./ilp_base
   perf stat -e cycles,instructions ./ilp_opt
   ```

4. **Calcular IPC** (Instructions Per Cycle):
   ```
   IPC = instructions / cycles
   ```

**Qué esperar**:
- Versión base: IPC bajo (~0.5-1.0) por stalls en cadena de dependencia
- Versión optimizada: IPC mayor (~2.0-4.0) al tener 4 cadenas independientes que llenan pipeline
- Speedup teórico máx: 4x (factor de unrolling), real depende de ancho de banda memoria y latencia FP add

**Documentar**: Tabla con cycles, instructions, IPC, time (ms), speedup. Justificar si no se alcanza 4x (memory bound, latencia FP add ~3-4 ciclos, puertos de ejecución limitados).

> Benchmarking: Comparar ambas versiones con hyperfine y perf (cycles, instructions, IPC). Justificar los resultados.
> — `repo:datos/temarios/AC/Practicas/Code_Lab4/tarea4_1_ilp.cpp` (cita sin comprobar)

Relacionado: [[optimizacion-ilp-mediante-desenrollado-de-bucle-con-4-acumul]] · [[calculo-de-flops-por-ciclo-en-x86-con-avx2-fma]]
