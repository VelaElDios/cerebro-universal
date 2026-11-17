---
tipo: "concepto"
titulo: "Ley de Amdahl aplicada a optimización de compilador para coma flotante (Ejercicio 8)"
temas: ["ac", "coma-flotante", "compiladores", "ley-amdahl", "speedup"]
claves: ["speedup máximo", "fracción mejorada", "compilador M", "k veces más rápido"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema1-Introduccion/Tema1 2026-27.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[coma-flotante]] · [[compiladores]] · [[ley-amdahl]] · [[speedup]]

Aplicación de la Ley de Amdahl: Speedup_global = 1 / [(1 - f) + f/k]
Donde:
- f = fracción del tiempo en la parte mejorada (coma flotante) = 0.90
- k = factor de mejora de esa parte (k veces más rápido)
- Speedup máximo (k → ∞) = 1 / (1 - f) = 1 / 0.10 = 10x

Respuesta inciso a): El speedup máximo teórico es 10x (cuando k tiende a infinito, el tiempo en FP tiende a 0).
Para un k finito: Speedup = 1 / [0.10 + 0.90/k]

> A partir de un compilador C se ha obtenido otro compilador mejorado M que obtiene código para las instrucciones de coma flotante k veces más rápido que el original. a) Si usando el compilador C, el 90% del tiempo total de ejecución es dedicado a instrucciones en coma flotante, ¿cuál es la máxima aceleración (speedup) que se puede obtener?
> — `repo:datos/temarios/AC/Tema1-Introduccion/Tema1 2026-27.pdf`

Relacionado: [[determinar-si-es-posible-alcanzar-un-speedup-objetivo-mejora]]
