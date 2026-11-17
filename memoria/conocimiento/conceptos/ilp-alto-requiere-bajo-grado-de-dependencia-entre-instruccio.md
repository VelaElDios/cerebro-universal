---
tipo: "concepto"
titulo: "ILP alto requiere bajo grado de dependencia entre instrucciones"
temas: ["ac", "ilp", "paralelismo instrucción"]
claves: ["ILP", "paralelismo nivel instrucción", "dependencias", "bajo grado"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2012.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[ilp]] · [[paralelismo instrucción]]

El ILP se limita por las dependencias verdaderas (RAW). Cuantas menos dependencias haya en la ventana de instrucciones, más instrucciones independientes pueden emitirse/ejecutarse en paralelo. Las opciones b) y c) son contrarias: lanzar muchas instrucciones dependientes no aumenta ILP.

> Para lograr un alto grado de paralelismo a nivel de instrucción (ILP): a) Es necesario que haya un bajo grado de dependencia entre las instrucciones
> — `repo:datos/temarios/AC/examenes/Enero2012.pdf`
