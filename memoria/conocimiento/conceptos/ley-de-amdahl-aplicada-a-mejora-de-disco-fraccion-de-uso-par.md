---
tipo: "concepto"
titulo: "Ley de Amdahl aplicada a mejora de disco: fracción de uso para speedup global"
temas: ["ac", "disco", "ley-amdahl", "speedup"]
claves: ["Amdahl", "speedup", "fracción tiempo", "mejora componente"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2013.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[disco]] · [[ley-amdahl]] · [[speedup]]

Ley de Amdahl: Speedup_global = 1 / [(1-f) + f/k] donde f = fracción tiempo uso componente mejorado, k = factor mejora componente. Aquí k=4, Speedup_global=3. 3 = 1/[(1-f)+f/4] → 1/3 = 1-f+f/4 = 1 - 3f/4 → 3f/4 = 2/3 → f = 8/9 ≈ 89%. El disco debe usarse el 89% del tiempo.

> Sustituimos el disco duro de un ordenador por otro disco cuatro veces más rápido. Si queremos conseguir que nuestro ordenador sea tres veces más rápido que antes, el nuevo disco debe usarse, aproximadamente: c) El 89% del tiempo
> — `repo:datos/temarios/AC/examenes/Enero2013.pdf` (cita sin comprobar)

Relacionado: [[definicion-de-mips-millones-de-instrucciones-por-segundo-y-c]]
