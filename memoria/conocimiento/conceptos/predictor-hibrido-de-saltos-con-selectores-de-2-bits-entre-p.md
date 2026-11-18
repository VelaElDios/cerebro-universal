---
tipo: "concepto"
titulo: "Predictor híbrido de saltos con selectores de 2 bits entre predictor local de 1 bit y predictor local de 3 bits"
temas: ["ac", "pipeline", "prediccion-saltos"]
claves: ["predictor híbrido", "predictor local 1 bit", "predictor local 3 bits", "contador saturado 2 bits", "selector MSB"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2017.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]] · [[prediccion-saltos]]

Diseño del predictor híbrido: (1) Predictor 1 = predictor local de 1 bit por salto (B1, B2). (2) Predictor 2 = predictor local de 3 bits por salto (contador de saturación de 3 bits). (3) Tabla "Contadores" = un contador de saturación de 2 bits por salto. Selección: MSB=1 → Predictor 1; MSB=0 → Predictor 2. Actualización de contadores tras cada predicción según tabla: (Acierto, Acierto) → sin cambio; (Acierto, Fallo) → +1; (Fallo, Acierto) → -1; (Fallo, Fallo) → sin cambio. Estado inicial: Contadores B1:00 B2:00; Predictor1 B1:0 B2:0; Predictor2 B1:000 B2:000.

> Detalla el comportamiento de un predictor híbrido que combina dos predictores locales (llamados “Predictor 1” y “Predictor 2”). El Predictor 1 asocia un predictor de 1 bit a cada instrucción de salto (B1 y B2), mientras que el Predictor 2 asocia un predictor de 3 bits a cada salto. Para seleccionar el predictor a emplear hay una tabla (llamada “Contadores”) que almacena un contador saturado de 2 bits para cada salto. Si el bit más significativo del contador es 1 se emplea el Predictor 1, mientras que si es 0 se emplea el Predictor 2.
> — `repo:datos/temarios/AC/examenes/Junio2017.pdf`

Relacionado: [[bht-con-contadores-de-saturacion-de-2-bits-pregunta-17]] · [[bht-en-predictor-dinamico-de-3-bits-contadores-de-saturacion]]
