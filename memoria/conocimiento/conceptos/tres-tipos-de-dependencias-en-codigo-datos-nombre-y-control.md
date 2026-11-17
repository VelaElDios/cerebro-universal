---
tipo: "concepto"
titulo: "Tres tipos de dependencias en código: datos, nombre y control"
temas: ["ac", "analisis-compilador", "dependencias", "riesgos"]
claves: ["dependencia de datos", "dependencia de nombre", "antidependencia", "dependencia de salida", "dependencia de control"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema2-Paralelismo a nivel de instruccion/Tema2-2026-2027.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[analisis-compilador]] · [[dependencias]] · [[riesgos]]

Taxonomía fundamental para el análisis de dependencias. (1) Dependencias de datos (verdaderas): flujo real de valores (productor→consumidor). (2) Dependencias de nombre: reutilizan el mismo registro/posición sin flujo de datos; se subdividen en antidependencia (j escribe, i lee → WAR) y dependencia de salida (i y j escriben → WAW). (3) Dependencias de control: orden relativo a instrucciones de salto. Determinan los riesgos posibles y el límite superior de paralelismo explotable.

>  Tipos de dependencias:   Dependencias de datos   Dependencias de nombre     Antidependencia     Dependencia de salida     Dependencias de control
> — `repo:datos/temarios/AC/Tema2-Paralelismo a nivel de instruccion/Tema2-2026-2027.pdf`
