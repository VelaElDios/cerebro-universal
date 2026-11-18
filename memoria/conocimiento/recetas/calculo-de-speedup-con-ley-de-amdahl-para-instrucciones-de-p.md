---
tipo: "receta"
titulo: "Cálculo de speedup con ley de Amdahl para instrucciones de punto flotante"
temas: ["ac", "amdahl", "rendimiento"]
claves: ["speedup", "punto flotante", "6 veces más rápido", "200 segundos"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2018.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[amdahl]] · [[rendimiento]]

Aplicar ley de Amdahl: Speedup_global = 1 / ((1 - f) + f/k), donde f = fracción de tiempo en PF original, k = 6. Se busca Speedup_global = 2. Despejar f: 2 = 1 / ((1-f) + f/6) → (1-f) + f/6 = 0.5 → 1 - f + f/6 = 0.5 → 5f/6 = 0.5 → f = 0.6. Tiempo en PF original = f * 200s = 120s. Respuesta correcta: b) 120 seconds.

> We improve a computer so that floating point instructions are now executed 6 times faster. We are looking for a test program obtaining a speedup of 2 for the improved version of the computer. Assuming that this program is executed in 200 seconds using the original floating point hardware, the time devoted to run floating point instructions should be…
> — `repo:datos/temarios/AC/examenes/June2018.pdf`
