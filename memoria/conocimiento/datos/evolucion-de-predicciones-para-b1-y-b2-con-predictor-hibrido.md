---
tipo: "dato"
titulo: "Evolución de predicciones para B1 y B2 con predictor híbrido en la secuencia completa"
temas: ["ac", "prediccion-saltos"]
claves: ["tabla evolución", "B1 R2=0 T P2 N MISS", "B2 N P2 N HIT", "contadores invariantes 00"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2017.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[prediccion-saltos]]

La tabla resuelta muestra 20 ejecuciones de salto (10 B1 + 10 B2). Observaciones clave:
- Los contadores selectores (Counters) permanecen en 00 00 durante toda la simulación (MSB=0 → siempre se usa Predictor 2).
- Predictor 2 (3 bits) empieza en 000 y alterna entre 000 y 001 para B1 (por el patrón T,N,T,N...), y se mantiene en 000 para B2 hasta la última iteración donde pasa a 001.
- Predictor 1 (1 bit) alterna entre 1 y 0 para B1 siguiendo el resultado real (T→1, N→0), y se mantiene en 0 para B2 hasta la última iteración donde pasa a 1.
- Predictor 2 falla siempre en B1 cuando el resultado es Taken (predice NT porque su estado es 000 o 001 con MSB=0), y acierta en Not Taken. En B2 acierta siempre en Not Taken y falla en el Taken final.
- Como P1 acierta en Taken (B1) y P2 falla, la regla "Hit/Miss → Increment" intentaría subir el contador, pero P1 falla en Not Taken y P2 acierta → "Miss/Hit → Decrement", compensándose y dejando el contador en 00.

> B1 (R2=0)         T          P2          N           MISS       00 00              1 0              001 000 B2                N          P2          N           HIT        00 00              1 0              001 000 B1 (R2=1)         N          P2          N           HIT        00 00              0 0              000 000 B2                N          P2          N           HIT        00 00              0 0              000 000
> — `repo:datos/temarios/AC/examenes/June2017.pdf`

Relacionado: [[resultados-reales-de-saltos-b1-y-b2-en-bucle-mips64-secuenci]] · [[reglas-de-actualizacion-del-contador-selector-de-2-bits-en-p]] · [[predictor-hibrido-con-selectores-por-salto-1-bit-vs-2-bit-y]] · [[simulacion-paso-a-paso-del-predictor-hibrido-con-contadores]] · [[secuencia-de-aciertos-fallos-en-predictor-2-bits-inicializad]]
