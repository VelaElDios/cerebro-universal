---
tipo: "dato"
titulo: "Valores de ejemplo para CPU del laboratorio (frecuencia, BW, puntos medidos)"
temas: ["ac", "laboratorio", "mediciones", "roofline"]
claves: ["FRECUENCIA_GHZ", "BW_DRAM", "intensidades", "rendimientos", "I_KNEE", "GFLOPS_MAX"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab3/tarea2_1_pintarRoofLin_conPunto.py"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[laboratorio]] · [[mediciones]] · [[roofline]]

Constantes y datos de ejemplo del script (TODO1 y TODO2):
- FRECUENCIA_GHZ = 4.9 GHz (obtenida con `lscpu`).
- BW_DRAM = 26.68 GB/s (obtenida con benchmark STREAM).
- FLOPSperCYCLE = 32 → GFLOPS_MAX = 4.9 × 32 = 156.8 GFLOPs/s.
- I_KNEE = GFLOPS_MAX / BW_DRAM = 156.8 / 26.68 ≈ 5.88 FLOPs/Byte.
- Puntos medidos (intensidad, rendimiento) para tres patrones:
  1. Acceso Temporal:    (0.3661, 1.1940) GFLOPs/s
  2. Acceso Secuencial:  (0.3006, 1.2000) GFLOPs/s
  3. Acceso Aleatorio:   (0.00885, 0.0825) GFLOPs/s
Estos valores son de ejemplo; el alumno debe sustituirlos por sus propias mediciones.

> FRECUENCIA_GHZ = 4.9     # Tu frecuencia en GHz (de lscpu) ... BW_DRAM = 26.68          # Tus GB/s de la RAM (de STREAM)
> — `repo:datos/temarios/AC/Practicas/Code_Lab3/tarea2_1_pintarRoofLin_conPunto.py` (cita sin comprobar)
