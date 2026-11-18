---
tipo: "concepto"
titulo: "Dependencia de datos (RAW): instrucción i produce resultado que usa j"
temas: ["ac", "dependencias", "raw"]
claves: ["dependencia datos", "RAW", "true dependency"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Octubre2010.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[dependencias]] · [[raw]]

Definición canónica de dependencia verdadera (Read After Write - RAW): j lee un valor escrito por i. Es la única dependencia que no se puede eliminar con renombramiento.

> Existe una dependencia de datos entre dos instrucciones i y j (j lógicamente después de i) si a) La instrucción i produce un resultado que usa la instrucción j
> — `repo:datos/temarios/AC/examenes/Octubre2010.pdf`

Relacionado: [[analisis-de-dependencias-en-bucle-con-add-d-y-s-d-misma-iter]]
