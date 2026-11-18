---
tipo: "concepto"
titulo: "Dependencias de nombre antidependencia y salida definición y ejemplo"
temas: ["ac", "antidependencia", "dependencia-salida", "dependencias", "war", "waw"]
claves: ["antidependencia", "anti-dependence", "dependencia de salida", "output dependence", "WAR", "WAW"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema2-Paralelismo a nivel de instruccion/Tema2-2026-2027.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[antidependencia]] · [[dependencia-salida]] · [[dependencias]] · [[war]] · [[waw]]

Dos subtipos sin flujo de datos real, solo colisión de nombre de almacenamiento. Antidependencia (WAR): j escribe un registro que i lee (ej. fld f0 en iteración 2 escribe f0 antes de que fadd.d de iteración 1 lo lea). Dependencia de salida (WAW): ambas escriben mismo registro (ej. fsd f4 en iteraciones consecutivas). Se eliminan con renombre de registros (hardware o compilador).

> Aparecen cuando dos instrucciones usan el mismo registro o posición de memoria, pero no hay flujo de datos entre las instrucciones asociadas con este nombre  Dadas dos instrucciones i y j (j lógicamente después de i), existe una dependencia de nombre si:     la instrucción j escribe sobre un registro o una posición de memoria que lee la instrucción i (Antidependencia)     las dos instrucciones i y j escriben sobre el mismo registro o posición de memoria (Dependencia de salida)  Bucle: fld    f0, 0(x1)  fadd.d f4, f0, f2  fsd    f4, 0(x1)  fld    f0, -8(x1)  fadd.d f4, f0, f2  fsd    f4, -8(x1)
> — `repo:datos/temarios/AC/Tema2-Paralelismo a nivel de instruccion/Tema2-2026-2027.pdf` (cita sin comprobar)

Relacionado: [[dependencia-de-datos-verdadera-definicion-y-ejemplo-en-bucle]] · [[definicion-de-dependencia-de-nombre-waw-y-war]] · [[definicion-de-dependencia-de-nombre-anti-y-salida]] · [[name-dependency-dependencia-de-nombre-incluye-waw-y-war]]
