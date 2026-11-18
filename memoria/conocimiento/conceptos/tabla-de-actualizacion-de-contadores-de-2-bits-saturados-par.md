---
tipo: "concepto"
titulo: "Tabla de actualización de contadores de 2-bits saturados para selector de predictor híbrido"
temas: ["ac", "prediccion-saltos"]
claves: ["contador saturado 2-bits", "selector híbrido", "MSB", "actualización contadores"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4_Prob.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[prediccion-saltos]]

Regla exacta de actualización de los contadores de selección en el predictor híbrido del Ejercicio 11. Cada salto (B1/B2) tiene su propio contador de 2-bits saturado (valores 00,01,10,11). MSB=1 → usa Predictor1 (1-bit); MSB=0 → usa Predictor2 (3-bits). La actualización depende de la pareja (resultado Predictor1, resultado Predictor2): ambos aciertan → contador invariante; P1 acierta y P2 falla → incrementa (+1); P1 falla y P2 acierta → decrementa (-1); ambos fallan → invariante. Saturación en 00 y 11.

> Si el bit más significativo del contador es 1 se selecciona el “Predictor1” en caso contrario el “Predictor2”. Los contadores y bits de predicción están inicializados a 0. Después de cada predicción, además de actualizar los dos predictores, la información de “Contadores” se actualiza según muestra la siguiente tabla: Comportamiento Predictor 1 / Predictor 2 / Acción: Acierto/Acierto→no cambia; Acierto/Fallo→+1; Fallo/Acierto→-1; Fallo/Fallo→no cambia.
> — `repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4_Prob.pdf` (cita sin comprobar)

Relacionado: [[estructura-y-funcionamiento-de-predictor-hibrido-de-torneo-c]] · [[reglas-de-actualizacion-de-contadores-de-seleccion-en-predic]] · [[reglas-de-actualizacion-del-contador-selector-de-2-bits-en-p]] · [[predictor-hibrido-con-selector-de-2-bits-entre-predictor-de]]
