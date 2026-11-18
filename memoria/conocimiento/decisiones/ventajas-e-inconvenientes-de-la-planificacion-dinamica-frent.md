---
tipo: "decision"
titulo: "Ventajas e inconvenientes de la planificación dinámica frente a estática"
temas: ["ac", "arquitectura-computadores", "planificacion-dinamica", "tradeoffs"]
claves: ["simplifica compilador", "dependencias desconocidas", "código optimizado para otra UF", "hardware complejo", "interrupciones imprecisas", "riesgos WAR WAW"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[arquitectura-computadores]] · [[planificacion-dinamica]] · [[tradeoffs]]

La planificación dinámica (Marcador y Tomasulo) traslada complejidad del compilador al hardware. Ventajas: 1) Simplifica compilador (no necesita reordenar instrucciones). 2) Maneja dependencias que solo se conocen en tiempo de ejecución (p. ej. aliasing de memoria). 3) Ejecuta bien código compilado para otra microarquitectura. Inconvenientes: 1) Hardware más complejo (logic de detección de riesgos, buffers, buses). 2) Interrupciones imprecisas (estado del procesador no corresponde a secuencia original al producirse excepción). 3) Introduce riesgos de nombre (WAR, WAW) que en orden no existen; el Marcador evita WAW en emisión y WAR en escritura, pero Tomasulo los elimina con renombrado de registros.

> Ventajas: Simplifica el diseño del compilador, Soluciona dependencias desconocidas en tiempo de compilación, Ejecuta eficientemente cualquier código, aunque haya sido optimizado para otra unidad de instrucción segmentada. Inconvenientes: Complica el diseño del hardware, Interrupciones imprecisas, Aparición de nuevos riesgos (WAR y WAW)
> — `repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf` (cita sin comprobar)

Relacionado: [[planificacion-dinamica-de-instrucciones-con-marcador-scorebo]] · [[ventajas-e-inconvenientes-del-algoritmo-tomasulo]] · [[limitacion-de-la-planificacion-estatica-que-motiva-la-planif]] · [[planificacion-estatica-vs-dinamica-de-instrucciones-en-arqui]]
