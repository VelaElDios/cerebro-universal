---
tipo: "receta"
titulo: "Secuencia de instrucciones y dependencias en el ejemplo Tomasulo del tema 3"
temas: ["ac", "ilp", "simulacion", "tomasulo"]
claves: ["fld", "fmul.d", "fsd", "dependencias RAW", "bucle"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[ilp]] · [[simulacion]] · [[tomasulo]]

El código simulado consta de dos iteraciones idénticas de tres instrucciones:
1. `fld f0, 0(x1)` — carga en f0 desde memoria [x1]
2. `fmul.d f4, f0, f2` — multiplica f0 * f2 → f4 (depende de f0 de la carga y de f2 que ya está listo)
3. `fsd f4, 0(x1)` — almacena f4 en memoria [x1] (depende del resultado de fmul.d)

La primera iteración se emite en ciclos 1-3; la segunda en ciclos 6-8. El registro f2 nunca cambia de Qi (siempre tiene valor listo), mientras que f0 y f4 reciben etiquetas Qi de las unidades que los producirán (Carga 1, Mult 1, Carga 2, Mult 2).

> fld       f0, 0(x1)                        1                           fmul.d    f4, f0, f2                       2                           fsd       f4, 0(x1)                        3
> — `repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf`

Relacionado: [[algoritmo-tomasulo-origen-y-objetivo-cpi1]] · [[buffers-de-carga-y-almacenamiento-en-tomasulo]]
