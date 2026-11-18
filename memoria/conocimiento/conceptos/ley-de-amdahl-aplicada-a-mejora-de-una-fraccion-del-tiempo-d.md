---
tipo: "concepto"
titulo: "Ley de Amdahl aplicada a mejora de una fracción del tiempo de ejecución"
temas: ["ac", "ley-amdahl", "rendimiento"]
claves: ["Amdahl", "speedup", "fracción mejorada"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2018.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[ley-amdahl]] · [[rendimiento]]

La ley de Amdahl: Speedup_global = 1 / ((1 - f) + f/k), donde f es la fracción del tiempo original que se mejora y k el factor de mejora de esa parte. Aquí f = 200/300 = 2/3. Queremos Speedup_global = 2. Despejando k: 2 = 1 / (1/3 + (2/3)/k) → 1/2 = 1/3 + 2/(3k) → 1/6 = 2/(3k) → k = 4. Hay que mejorar la suma 4 veces (respuesta c).

> Supongamos que un programa tarda en ejecutarse en una máquina 300 segundos, de los cuales 200 corresponden a operaciones de suma. ¿Cuánto tengo que mejorar la velocidad de la suma si quiero que el programa se ejecute el doble de rápido?
> — `repo:datos/temarios/AC/examenes/Enero2018.pdf`

Relacionado: [[aplicacion-de-la-ley-de-amdahl-para-acelerar-una-fraccion-de]] · [[aplicacion-de-la-ley-de-amdahl-para-speedup-global-mejorando]] · [[calculo-de-mejora-necesaria-con-ley-de-amdahl-ejemplo-multip]]
