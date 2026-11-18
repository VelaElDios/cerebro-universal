---
tipo: "concepto"
titulo: "Ley de Amdahl aplicada a mejora de disco"
temas: ["ac", "ley-de-amdahl", "rendimiento"]
claves: ["ley de Amdahl", "speedup", "fracción mejorada", "disco duro"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema1-Introduccion/Tema1_ProbSol.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[ley-de-amdahl]] · [[rendimiento]]

La ley de Amdahl modela la aceleración global (speedup) cuando solo una fracción x del tiempo de ejecución se beneficia de una mejora de factor k. La fórmula general es speedup = 1 / ((x/k) + (1-x)). En este ejercicio, k=4 (disco 4× más rápido) y speedup objetivo=3, despejando x se obtiene el 89 % de uso necesario del disco.

> speedup = 3 = T / (xT/4 + (1-x)T) ⟹ x = 0.89 (el disco debe usarse el 89% del tiempo)
> — `repo:datos/temarios/AC/Tema1-Introduccion/Tema1_ProbSol.pdf` (cita sin comprobar)

Relacionado: [[calculo-de-flops-por-ciclo-en-x86-con-avx2-fma]] · [[ley-de-amdahl-aplicada-a-mejora-de-disco-fraccion-de-uso-par]] · [[ley-de-amdahl-para-mejora-de-subsistema-disco-6x-mas-rapido]] · [[como-calcular-la-fraccion-de-uso-requerida-para-un-speedup-o]]
