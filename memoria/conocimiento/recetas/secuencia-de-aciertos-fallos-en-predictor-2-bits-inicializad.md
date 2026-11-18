---
tipo: "receta"
titulo: "Secuencia de aciertos/fallos en predictor 2 bits (inicializado fuertemente no tomado) para bucle de 6 iteraciones"
temas: ["ac", "prediccion-saltos", "predictor-2-bits"]
claves: ["predictor 2 bits", "fuertemente no tomado", "BNEZ", "historial saltos"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2022.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[prediccion-saltos]] · [[predictor-2-bits]]

El bucle se ejecuta 6 veces (R2=6,5,4,3,2,1 → tomado; R2=0 → no tomado). Predictores 2 bits: estados 00=fuertemente no tomado, 01=débilmente no tomado, 10=débilmente tomado, 11=fuertemente tomado. Inicio: 00. Iter 1: salto tomado → predicción NT (fallo) → estado 01. Iter 2: tomado → predicción NT (fallo) → estado 10. Iter 3: tomado → predicción T (acierto) → estado 11. Iter 4: tomado → predicción T (acierto) → 11. Iter 5: tomado → predicción T (acierto) → 11. Iter 6: tomado → predicción T (acierto) → 11. Iter 7 (salida): no tomado → predicción T (fallo) → estado 10. Secuencia para las 6 evaluaciones del salto B1 (iteraciones 1-6): F F A A A A → "FFAAAA". Opción d.

> Tenemos un predictor de 1 nivel de 2 bits inicializado a fuertemente no tomado. Indica la secuencia de Aciertos (A) y Fallos (F) del predictor para el salto B1 del siguiente código: inicio: DADDIU R2, R0, #6 DADDIU R4, R0, #1 bucle: DADDIU R2, R2, #-1 ;salto B1 BNEZ R2, bucle
> — `repo:datos/temarios/AC/examenes/Enero2022.pdf`

Relacionado: [[bht-branch-history-table-tabla-separada-para-bits-de-predicc]] · [[btb-con-predictores-de-4-bits-campos-de-cada-entrada]] · [[secuencia-de-aciertos-fallos-en-predictor-de-2-bits-iniciali]] · [[como-analizar-predictores-de-salto-1-bit-4-bit-correlacionad]] · [[predictor-de-1-bit-en-bucle-de-3-iteraciones-t-t-nt-produce]]
