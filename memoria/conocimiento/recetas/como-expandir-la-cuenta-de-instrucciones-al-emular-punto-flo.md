---
tipo: "receta"
titulo: "Cómo expandir la cuenta de instrucciones al emular punto flotante con enteras"
temas: ["ac", "emulacion-punto-flotante", "evaluacion-rendimiento", "expansion-instrucciones"]
claves: ["emulación punto flotante", "instrucciones enteras", "expansión código", "MNFP"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema1-Introduccion/Tema1_ProbSol.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[emulacion-punto-flotante]] · [[evaluacion-rendimiento]] · [[expansion-instrucciones]]

Para cada instrucción FP original, multiplicar por el número de instrucciones enteras que la implementan.
- Multiplicación FP: 1 → 30 enteras.
- Suma FP: 1 → 20 enteras.
- División FP: 1 → 50 enteras.
- Instrucciones enteras nativas: 1 → 1 (sin cambio).

Ejemplo (Ejercicio 3b): Programa de 300M instrucciones en MFP (10% mult, 15% add, 5% div, 70% enteras):
- MFP: 30M mult + 45M add + 15M div + 210M enteras = 300M total.
- MNFP: 30M×30 + 45M×20 + 15M×50 + 210M×1 = 900M + 900M + 750M + 210M = 2760M instrucciones enteras.

> La máquina MNFP (máquina sin punto flotante) no tiene hardware de punto flotante y por ello debe emular las operaciones en punto flotante utilizando enteras.
> — `repo:datos/temarios/AC/Tema1-Introduccion/Tema1_ProbSol.pdf`

Relacionado: [[pointer-chasing-en-std-list-vs-acceso-contiguo-en-std-vector]] · [[valores-de-referencia-cpi-por-clase-de-instruccion-en-maquin]] · [[como-calcular-cpi-medio-y-mips-nativo-con-mezcla-de-instrucc]] · [[latencias-tipicas-de-unidades-funcionales-fp-en-ejercicios-d]]
