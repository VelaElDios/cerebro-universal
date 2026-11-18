---
tipo: "receta"
titulo: "Cálculo de mejora necesaria con la ley de Amdahl (test AC Q3)"
temas: ["ac", "ley-amdahl", "rendimiento"]
claves: ["Amdahl", "speedup", "fracción-mejorable", "CPI"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2025.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[ley-amdahl]] · [[rendimiento]]

Para calcular el factor de mejora `s` de una fracción `f` del tiempo original para conseguir un speedup global `S`:
1. `f = tiempo_mejorable / tiempo_total` (aquí 100 s / 120 s = 5/6).
2. Fórmula de Amdahl: `S = 1 / ((1 - f) + f/s)`.
3. Despejar `s`: `s = f / (1/S - (1 - f))`.
Ejemplo del test: `S=5`, `f=5/6` → `s = (5/6) / (1/5 - 1/6) = (5/6) / (1/30) = 25`. Respuesta: 25 veces.

> Supongamos que un programa tarda en ejecutarse en una máquina 2 minutos, de los cuales 100 segundos corresponden a operaciones de multiplicar. ¿Cuánto tengo que mejorar la velocidad de multiplicación si quiero que el programa se ejecute cinco veces más rápido?
> — `repo:datos/temarios/AC/examenes/Enero2025.pdf`
