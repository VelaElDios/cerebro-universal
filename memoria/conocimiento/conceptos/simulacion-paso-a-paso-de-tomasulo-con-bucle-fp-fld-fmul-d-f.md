---
tipo: "concepto"
titulo: "Simulación paso a paso de Tomasulo con bucle FP (fld/fmul.d/fsd)"
temas: ["ac", "arquitectura", "fuera-de-orden", "pipeline", "tomasulo"]
claves: ["fld", "fmul.d", "fsd", "buffers carga almacenamiento", "estaciones reserva", "Qi", "renombrado registros"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[arquitectura]] · [[fuera-de-orden]] · [[pipeline]] · [[tomasulo]]

El documento muestra 7 ciclos consecutivos (9-15) de la ejecución de un bucle con tres instrucciones de punto flotante que se repiten: carga (fld), multiplicación doble (fmul.d) y almacenamiento (fsd). El algoritmo Tomasulo gestiona dependencias RAW, WAR y WAW mediante renombrado de registros con etiquetas Qi en las estaciones de reserva y buffers de carga/almacenamiento. Cada iteración usa los mismos registros arquitectónicos (f0, f2, f4) pero las etiquetas Qi (Carga 1, Carga 2, Carga 3, Mult 1, Mult 2) distinguen las instancias dinámicas. El puntero base x1 decrementa 8 bytes por iteración (72→64), típico de array de double en orden inverso.

> Estado de las instrucciones ciclo 9 Instrucción Emisión Ejecución Escritura resultado fld f0, 0(x1) 1 9 fmul.d f4, f0, f2 2 fsd f4, 0(x1) 3
> — `repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf`

Relacionado: [[algoritmo-tomasulo-origen-y-objetivo-cpi1]] · [[buffers-de-carga-y-almacenamiento-en-tomasulo]] · [[ejecucion-paso-a-paso-de-instrucciones-fp-en-tomasulo-ciclos]] · [[secuencia-de-instrucciones-y-dependencias-en-el-ejemplo-toma]] · [[ejecucion-ciclo-a-ciclo-del-ejemplo-tomasulo-fld-fmul-d-fsub]]
