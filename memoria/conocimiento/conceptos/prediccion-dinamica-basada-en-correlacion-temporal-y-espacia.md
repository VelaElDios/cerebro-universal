---
tipo: "concepto"
titulo: "Predicción dinámica basada en correlación temporal y espacial"
temas: ["ac", "arquitectura", "correlacion", "dinamica", "prediccion-saltos"]
claves: ["predicción dinámica", "correlación temporal", "correlación espacial", "historia ejecución", "hardware", "coste hardware"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[arquitectura]] · [[correlacion]] · [[dinamica]] · [[prediccion-saltos]]

La predicción dinámica usa hardware que analiza la historia de ejecución. Dos tipos de correlación: 1) Temporal: el modo en que se resolvió un salto predice cómo se resolverá en su próxima ejecución (historia individual del salto). 2) Espacial: varios saltos se resuelven de forma altamente correlacionada (un camino de ejecución preferido, historia global). Las prestaciones dependen de la precisión (mejora con mejores predictores) y del coste del fallo (depende de longitud y organización del cauce). Suele ser más efectiva que la estática pero con mayor coste y complejidad hardware.

> El hardware realiza una predicción basada en la historia – Correlación Temporal – The way a branch resolves may be a good predictor of the way it will resolve at the next execution – Correlación Espacial – Several branches may resolve in a highly correlated manner (a preferred path of execution)
> — `repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4.pdf` (cita sin comprobar)

Relacionado: [[taxonomia-de-tecnicas-de-prediccion-de-saltos]] · [[predictor-dinamico-de-un-bit-funcionamiento-y-limitacion-en]] · [[predictor-correlacionado-o-de-dos-niveles-m-n-correlacion-es]]
