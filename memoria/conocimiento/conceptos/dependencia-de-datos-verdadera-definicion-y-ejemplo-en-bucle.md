---
tipo: "concepto"
titulo: "Dependencia de datos verdadera definición y ejemplo en bucle"
temas: ["ac", "dependencia-datos", "dependencias", "true-dependency"]
claves: ["dependencia verdadera", "data dependency", "RAW", "bucle ejemplo"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema2-Paralelismo a nivel de instruccion/Tema2-2026-2027.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[dependencia-datos]] · [[dependencias]] · [[true-dependency]]

Definición recursiva/transitiva: dependencia directa (i produce, j consume) o transitiva (i→k→j). El ejemplo muestra cadena fld→fadd.d→fsd (f0 y f4) y dependencia de control en bne. Es la única que refleja flujo real de datos y genera riesgo RAW si no hay forwarding.

> Dadas dos instrucciones i y j (j lógicamente después de i), existe una dependencia de datos entre ellas si:     la instrucción i produce un resultado que usa la instrucción j     hay dependencia de datos entre la instrucción i y otra instrucción k, y la instrucción k produce un resultado que usa la instrucción j  Bucle:        fld        f0, 0(x1)         ;f0= array de elementos  fadd.d     f4, f0, f2        ;suma escalar almacenado en f2  fsd        f4, 0(x1)         ;almacena el resultado  addi       x1, x1, -8        ;decrementa puntero (-8)  bne        x1, x2, Bucle     ;salta si x1!=x2
> — `repo:datos/temarios/AC/Tema2-Paralelismo a nivel de instruccion/Tema2-2026-2027.pdf`
