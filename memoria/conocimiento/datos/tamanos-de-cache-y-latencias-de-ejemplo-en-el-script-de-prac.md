---
tipo: "dato"
titulo: "Tamaños de caché y latencias de ejemplo en el script de práctica AC"
temas: ["ac", "memoria", "rendimiento"]
claves: ["L1=48 KiB", "L2=1280 KiB", "L3=25000 KiB", "latencias ns", "size_kib array"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab3.zip!tarea1_2_pintarLatvsMem.py"]
confianza: "propuesto"
fecha: "2026-11-19"
actualizado: "2026-11-19"
---

Temas: [[ac]] · [[memoria]] · [[rendimiento]]

Valores de referencia incluidos en el script (TODO1 y TODO2) para una máquina concreta:
- Cachés: L1=48 KiB, L2=1280 KiB (1.25 MiB), L3=25000 KiB (~24.4 MiB).
- Working sets probados (KiB): 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144.
- Latencias medidas (ns): 1.12, 1.07, 1.07, 1.05, 1.67, 2.44, 2.80, 3.54, 4.78, 8.71, 11.87, 14.07, 23.86, 50.71, 69.59, 80.99, 85.75.
Observaciones: latencia ~1 ns dentro de L1; salto a ~1.6–3.5 ns en L2; salto a ~11–23 ns en L3; ~80–86 ns en RAM.

> L1 = 48\nL2 = 1280\nL3 = 25000
> — `repo:datos/temarios/AC/Practicas/Code_Lab3.zip!tarea1_2_pintarLatvsMem.py` (cita sin comprobar)

Relacionado: [[calculo-de-speedup-con-ley-de-amdahl-fraccion-mejorada-al-do]] · [[definicion-de-peak-performance-rendimiento-pico]]
