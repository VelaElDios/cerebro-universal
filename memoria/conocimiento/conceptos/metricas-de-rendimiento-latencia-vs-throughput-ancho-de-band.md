---
tipo: "concepto"
titulo: "Métricas de rendimiento: Latencia vs Throughput (Ancho de banda)"
temas: ["ac", "ancho-de-banda", "latencia", "rendimiento", "throughput"]
claves: ["latencia", "tiempo de respuesta", "throughput", "ancho de banda", "productividad"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema1-Introduccion/Tema1 2026-27.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[ancho-de-banda]] · [[latencia]] · [[rendimiento]] · [[throughput]]

Dos métricas fundamentales:
1. **Latencia (tiempo de respuesta)**: tiempo entre inicio y fin de una tarea individual (ejecutar un programa, una instrucción, transmitir un paquete). Se mide en segundos.
2. **Throughput / Ancho de banda / Productividad**: tasa de trabajo completado por unidad de tiempo (programas/segundo, instrucciones/segundo, bits/segundo).
En arquitectura, mejorar latencia no siempre mejora throughput (p. ej., pipeline profundo reduce latencia por instrucción pero aumenta throughput). Los benchmarks Top500 usan FLOPS (throughput), Green500 usa MFLOPS/W (eficiencia energética).

> Latencia o tiempo de respuesta: tiempo transcurrido entre el comienzo y el final de un evento... Productividad o ancho de banda (throughput / bandwidth): cantidad de trabajo realizado en un tiempo determinado
> — `repo:datos/temarios/AC/Tema1-Introduccion/Tema1 2026-27.pdf` (cita sin comprobar)

Relacionado: [[definicion-de-mflops-millones-de-operaciones-de-punto-flotan]] · [[definicion-de-mips-millones-de-instrucciones-por-segundo]]
