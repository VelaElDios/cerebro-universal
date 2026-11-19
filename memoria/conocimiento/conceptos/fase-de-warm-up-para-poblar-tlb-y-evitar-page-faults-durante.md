---
tipo: "concepto"
titulo: "Fase de warm-up para poblar TLB y evitar page faults durante medición"
temas: ["ac", "memoria", "page-fault", "tlb", "warmup"]
claves: ["warm-up", "TLB", "page fault", "physical memory", "translation lookaside buffer"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab3.zip!tarea1_2_mem_latency.cpp"]
confianza: "verificado"
fecha: "2026-11-19"
actualizado: "2026-11-19"
---

Temas: [[ac]] · [[memoria]] · [[page-fault]] · [[tlb]] · [[warmup]]

Antes de la medición real, se ejecuta una pasada completa por el array (`for (i=0; i<n; ++i) p = buf[p];`). Esto sirve para:
1. Forzar la asignación de páginas físicas (touch memory) - las páginas se asignan en la primera escritura/lectura real
2. Poblar la TLB (Translation Lookaside Buffer) con las traducciones de direcciones virtuales a físicas
3. Evitar que los page faults y misses de TLB contaminen la medición de latencia pura de caché/memoria
Sin este warm-up, la primera medición incluiría overhead de asignación de páginas y walks de tabla de páginas.

> Warm-up: asigna páginas en RAM física y puebla la TLB para evitar page faults durante el test.
> — `repo:datos/temarios/AC/Practicas/Code_Lab3.zip!tarea1_2_mem_latency.cpp`
