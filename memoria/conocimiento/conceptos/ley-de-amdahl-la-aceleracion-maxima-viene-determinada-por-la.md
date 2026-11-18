---
tipo: "concepto"
titulo: "Ley de Amdahl: la aceleración máxima viene determinada por la fracción de tiempo que use la mejora"
temas: ["ac", "amdahl", "rendimiento"]
claves: ["ley de Amdahl", "fracción de tiempo", "aceleración máxima"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2012.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[amdahl]] · [[rendimiento]]

La ley de Amdahl establece que el speedup global está limitado por la fracción del tiempo de ejecución que puede beneficiarse de la optimización. Si una mejora afecta al 35% del tiempo y lo reduce un 15%, el speedup global es 1/(1-0.35+0.35/1.15) ≈ 1.055; si afecta al 10% y lo reduce un 25%, speedup ≈ 1.028. Por tanto, se elige la mejora que actúa sobre mayor fracción de tiempo aunque su factor de mejora sea menor.

> La aceleración máxima del rendimiento obtenida al realizar una mejora viene determinada por la fracción de tiempo que pueda utilizarse dicha mejora
> — `repo:datos/temarios/AC/examenes/Junio2012.pdf`

Relacionado: [[analisis-de-dependencias-en-bucle-con-add-d-y-s-d-misma-iter]]
