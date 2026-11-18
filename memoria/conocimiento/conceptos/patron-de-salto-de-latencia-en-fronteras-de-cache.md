---
tipo: "concepto"
titulo: "Patrón de salto de latencia en fronteras de caché"
temas: ["ac", "arquitectura-computadores", "cache-hierarchy", "memory-latency"]
claves: ["latency jump", "cache boundary", "working set", "L1 L2 L3 miss penalty"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab3/tarea1_2_pintarLatvsMem.py"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[arquitectura-computadores]] · [[cache-hierarchy]] · [[memory-latency]]

El objetivo pedagógico de la gráfica es observar cómo la latencia de acceso salta bruscamente cuando el working set supera el tamaño de cada nivel de caché:
- Dentro de L1 (≤48 KiB en el ejemplo): latencia ~1 ns.
- Al superar L1 y entrar en L2 (48–1280 KiB): latencia sube a ~2–14 ns.
- Al superar L2 y entrar en L3 (1280–25000 KiB): latencia sube a ~23–70 ns.
- Al superar L3 y entrar en RAM (>25000 KiB): latencia ~80–86 ns.
Estos saltos reflejan el *miss penalty* de cada nivel. La gráfica de escalones (`where='post'`) hace visible que la latencia se mantiene constante dentro de un nivel y salta en la frontera.

> Análisis: Verificar los saltos de latencia.
> — `repo:datos/temarios/AC/Practicas/Code_Lab3/tarea1_2_pintarLatvsMem.py`

Relacionado: [[working-set-size-vs-memory-access-latency-experiment]] · [[como-graficar-latencia-vs-working-set-con-jerarquia-de-cache]] · [[tamanos-de-cache-de-ejemplo-y-latencias-medidas-en-el-script]]
