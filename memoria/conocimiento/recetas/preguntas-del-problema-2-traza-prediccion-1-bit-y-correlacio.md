---
tipo: "receta"
titulo: "Preguntas del Problema 2: Traza predicción 1-bit y correlacionado (1,1)"
temas: ["ac", "branch-prediction", "prediccion-saltos", "tasa-acierto"]
claves: ["comportamiento real T/NT", "predictor 1 bit bits predicción acierto S/N", "predictor 2 niveles BHR BTHs predicción acierto", "tasa acierto final"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2025.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[branch-prediction]] · [[prediccion-saltos]] · [[tasa-acierto]]

Metodología: Simular 18 ejecuciones de salto (6 iteraciones x 3 saltos). Para cada salto: 1. Determinar T/NT real según valores R3, R1. 2. Predictor 1-bit: Leer bit asociado al salto -> Predicción T/NT. Comparar -> Acierto S/N. Actualizar bit = Real. 3. Predictor 2-niveles (1,1): Leer BHR (1 bit) -> Indexar BTH del salto -> Leer bit -> Predicción. Comparar -> Acierto. Actualizar BTH[BHR] = Real. Actualizar BHR = Real (shift left, insert real outcome). Calcular tasa acierto = Aciertos / 18.

> a) (0,25 puntos) Indica el comportamiento real (T/NT) de las instrucciones de salto ejecutadas... b) (0,75 puntos) Detalla el comportamiento de un predictor de un nivel que asigna 1 bit a cada instrucción de salto... Indica al final la tasa de acierto de este predictor. c) (1 punto) Detalla el comportamiento de un predictor de saltos correlacionado de dos niveles (1, 1)... Indica al final la tasa de acierto de este predictor.
> — `repo:datos/temarios/AC/examenes/Enero2025.pdf` (cita sin comprobar)
