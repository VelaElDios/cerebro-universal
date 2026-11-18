---
tipo: "receta"
titulo: "Reglas de actualización del selector híbrido de 2 bits"
temas: ["ac", "prediccion-saltos"]
claves: ["actualización selector", "tabla Hit/Miss", "saturación 2 bits"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2019.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[prediccion-saltos]]

Algoritmo de actualización del selector tras cada predicción de salto:
1. Evaluar acierto/fallo de Predictor 1 y Predictor 2.
2. Aplicar delta al selector:
   - (Hit, Hit) → 0
   - (Hit, Miss) → +1
   - (Miss, Hit) → -1
   - (Miss, Miss) → 0
3. Saturar a 2 bits (rango 0-3).
4. Próxima predicción: si selector ≥ 2 → Predictor 1; else → Predictor 2.
Inicialización: selector = 1, bits de predicción = 1.

> After each prediction, the Selector value is updated according to this table: Predictor 1 Hit Predictor 2 Hit Does not change; Predictor 1 Hit Predictor 2 Miss +1; Predictor 1 Miss Predictor 2 Hit -1; Predictor 1 Miss Predictor 2 Miss Does not change
> — `repo:datos/temarios/AC/examenes/June2019.pdf` (cita sin comprobar)

Relacionado: [[selector-de-2-bits-para-predictor-hibrido-de-saltos]] · [[reglas-de-actualizacion-del-contador-selector-de-2-bits-en-p]] · [[reglas-de-actualizacion-de-contadores-de-seleccion-en-predic]]
