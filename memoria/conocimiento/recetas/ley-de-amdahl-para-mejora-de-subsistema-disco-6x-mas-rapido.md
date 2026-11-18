---
tipo: "receta"
titulo: "Ley de Amdahl para mejora de subsistema (disco 6x más rápido, objetivo 3x global)"
temas: ["ac", "ley-amdahl", "rendimiento"]
claves: ["Ley de Amdahl", "fracción uso", "speedup global", "speedup componente"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2022.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[ley-amdahl]] · [[rendimiento]]

Ley de Amdahl: Speedup_global = 1 / ((1 - f) + f/k), donde f = fracción de tiempo usando el disco, k = speedup del disco (6). Queremos Speedup_global = 3. 3 = 1 / ((1-f) + f/6) → 1/3 = 1 - f + f/6 = 1 - (5/6)f → (5/6)f = 2/3 → f = (2/3)×(6/5) = 4/5 = 0.8. El disco debe usarse el 80% del tiempo. Opción correcta: "El disco debe utilizarse el 80% del tiempo".

> Si se sustituye el disco duro de un ordenador por otro disco seis veces más rápido que el actual, calcula el uso que debería hacerse de este dispositivo si se quiere conseguir que el ordenador funcione tres veces más rápido.
> — `repo:datos/temarios/AC/examenes/Enero2022.pdf`

Relacionado: [[calculo-de-mips-pico-a-partir-de-mezcla-de-instrucciones-y-f]]
