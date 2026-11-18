---
tipo: "concepto"
titulo: "Definición de dependencia de datos verdadera (RAW)"
temas: ["ac", "pipeline"]
claves: ["dependencia de datos", "RAW", "true dependence"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2016.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]]

La dependencia de datos verdadera (Read After Write) ocurre cuando la instrucción i escribe un registro/memoria que la instrucción j lee posteriormente. Es la única que representa un flujo real de datos.

> Existe una dependencia de datos entre dos instrucciones i y j (j lógicamente después de i) si : La instrucción i produce un resultado que usa la instrucción j
> — `repo:datos/temarios/AC/examenes/Junio2016.pdf` (cita sin comprobar)

Relacionado: [[analisis-de-dependencias-en-bucle-con-add-d-y-s-d-misma-iter]]
