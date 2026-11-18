---
tipo: "dato"
titulo: "Tamaños de caché de ejemplo y latencias medidas en el script"
temas: ["ac", "cache-sizes", "hardware", "latency-measurements"]
claves: ["L1=48 KiB", "L2=1280 KiB", "L3=25000 KiB", "latency ns array"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab3/tarea1_2_pintarLatvsMem.py"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[cache-sizes]] · [[hardware]] · [[latency-measurements]]

Valores de referencia incluidos en el script (deben sustituirse por los de la máquina real):
- **Cachés**: L1=48 KiB, L2=1280 KiB (1.25 MiB), L3=25000 KiB (~24.4 MiB).
- **Working sets probados**: 17 puntos de 4 KiB a 256 MiB (262144 KiB).
- **Latencias (ns)**: crecen de ~1 ns en L1 a ~86 ns en RAM, con saltos claros en 48, 1280 y 25000 KiB.

> L1 = 48 ... L2 = 1280 ... L3 = 25000 ... latency_ns = np.array([1.12, 1.07, 1.07, 1.05, 1.67, 2.44, 2.80, 3.54, 4.78, 8.71, 11.87, 14.07, 23.86, 50.71, 69.59, 80.99, 85.75])
> — `repo:datos/temarios/AC/Practicas/Code_Lab3/tarea1_2_pintarLatvsMem.py` (cita sin comprobar)

Relacionado: [[patron-de-salto-de-latencia-en-fronteras-de-cache]] · [[working-set-size-vs-memory-access-latency-experiment]] · [[rango-de-working-set-4-kib-a-256-mib-en-potencias-de-2]]
