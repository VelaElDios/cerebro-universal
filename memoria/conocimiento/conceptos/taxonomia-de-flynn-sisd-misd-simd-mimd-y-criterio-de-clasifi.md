---
tipo: "concepto"
titulo: "Taxonomía de Flynn (SISD, MISD, SIMD, MIMD) y criterio de clasificación"
temas: ["ac", "flynn", "mimd", "misd", "simd", "sisd", "taxonomia"]
claves: ["Flynn", "1972", "flujos de instrucciones", "flujos de datos", "SISD", "MISD", "SIMD", "MIMD"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema1-Introduccion/Tema1 2026-27.pdf (trozo 3 de 5)"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[flynn]] · [[mimd]] · [[misd]] · [[simd]] · [[sisd]] · [[taxonomia]]

Clasificación clásica (1972) según número de flujos de instrucciones (control) y flujos de datos:
- SISD (Single Instruction, Single Data): monoprocesador secuencial tradicional.
- MISD (Multiple Instruction, Single Data): varios flujos de control sobre un mismo dato; raro, ejemplos históricos o procesadores tensoriales especializados.
- SIMD (Single Instruction, Multiple Data): una instrucción opera sobre múltiples datos vectoriales; procesadores vectoriales, extensiones multimedia (MMX, SSE, AVX, NEON), GPUs.
- MIMD (Multiple Instruction, Multiple Data): múltiples flujos de control y datos; multiprocesadores (memoria compartida), multicomputadores (memoria distribuida), clusters.
La tabla del documento muestra la correspondencia con arquitecturas reales.

> Taxonomía de Flynn • Flynn, M. “Some Computer Organizations and Their Effectiveness.” IEEE Transactions on Computers, September 1972 • Clasificación muy usada, ¿está obsoleta? • Criterio empleado: número de flujos de instrucciones y de datos
> — `repo:datos/temarios/AC/Tema1-Introduccion/Tema1 2026-27.pdf (trozo 3 de 5)` (cita sin comprobar)

Relacionado: [[taxonomia-de-flynn-clasificacion-por-flujos-de-instrucciones]] · [[clasificacion-de-multiprocesadores-en-taxonomia-de-flynn]] · [[procesadores-superscalar-son-maquinas-sisd]]
