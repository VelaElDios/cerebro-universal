---
tipo: "receta"
titulo: "Cómo obtener los parámetros reales de tu máquina para el Roofline"
temas: ["ac", "arquitectura-computadores", "benchmark", "lscpu", "roofline", "stream"]
claves: ["lscpu", "STREAM", "BW_DRAM", "FRECUENCIA_GHZ"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab3/tarea1_3_pintarRoofLin.py"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[arquitectura-computadores]] · [[benchmark]] · [[lscpu]] · [[roofline]] · [[stream]]

Para usar el script con tu hardware real:
1. Frecuencia CPU: ejecuta `lscpu | grep "CPU MHz"` o `lscpu | grep "Model name"` y usa la frecuencia turbo máxima en GHz.
2. Ancho de banda DRAM: compila y ejecuta el benchmark STREAM (https://www.cs.virginia.edu/stream/):
   - `gcc -O3 -fopenmp stream.c -o stream`
   - `./stream` → toma el valor "Copy" o "Scale" en GB/s (memoria sostenida).
3. Sustituye las dos constantes en el script y vuelve a ejecutar.

> FRECUENCIA_GHZ = 4.9     # Tu frecuencia en GHz (de lscpu)\nBW_DRAM = 26.143         # Tus GB/s de la RAM (de STREAM)
> — `repo:datos/temarios/AC/Practicas/Code_Lab3/tarea1_3_pintarRoofLin.py` (cita sin comprobar)
