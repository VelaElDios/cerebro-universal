---
tipo: "concepto"
titulo: "Calentamiento (warm-up) para poblar TLB y evitar page faults"
temas: ["ac", "benchmark", "page-fault", "tlb", "warmup"]
claves: ["warm-up", "calentamiento", "TLB", "page faults", "RAM física"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab3/tarea1_2_mem_latency.cpp"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[benchmark]] · [[page-fault]] · [[tlb]] · [[warmup]]

Antes de medir, se recorre el ciclo completo una vez (`n` accesos). Esto fuerza al SO a: (1) asignar marcos de página físicos (page frames) para todas las páginas virtuales tocadas (demand paging), (2) poblar la TLB (Translation Lookaside Buffer) con las traducciones virtual→físico. Sin este warm-up, los primeros accesos del test medirían latencia de page fault + TLB miss + acceso memoria, contaminando la medida de latencia pura de caché/RAM.

> // Warm-up: asigna páginas en RAM física y puebla la TLB para evitar page faults durante el test.
std::size_t p = 0;
for (std::size_t i = 0; i < n; ++i) p = buf[p];
> — `repo:datos/temarios/AC/Practicas/Code_Lab3/tarea1_2_mem_latency.cpp`

Relacionado: [[construccion-de-permutacion-aleatoria-en-ciclo-para-pointer]]
