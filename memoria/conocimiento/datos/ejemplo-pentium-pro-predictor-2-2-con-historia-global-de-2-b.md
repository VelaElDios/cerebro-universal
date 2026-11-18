---
tipo: "dato"
titulo: "Ejemplo Pentium Pro: predictor (2,2) con historia global de 2 bits y ~95% precisión"
temas: ["ac", "arquitectura-computadores", "historia global", "pentium pro", "prediccion-saltos"]
claves: ["Pentium Pro", "predictor (2", "2)", "BHR 2 bits", "4 conjuntos BHT", "95% precisión"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[arquitectura-computadores]] · [[historia global]] · [[pentium pro]] · [[prediccion-saltos]]

El Pentium Pro (1995) implementa un predictor correlacionado (2,2): BHR de 2 bits (historia de los 2 últimos saltos globales) que selecciona entre 4 tablas BHT. Cada BHT tiene predictores de 2 bits indexados por el PC. Alcanza ~95% de precisión. El BHR se actualiza haciendo shift-in del resultado (T/NT) de cada salto resuelto.

> Ejemplo: el Pentium Pro usa el resultado de los 2 últimos saltos para seleccionar uno de los 4 conjuntos de BHT bits (precisión: ~95%) • Program Counter • Fetch PC • BHR: Registro de desplazamiento de historia global de saltos de 2-bit • Shift in Taken/¬Taken results of each branch
> — `repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4.pdf` (cita sin comprobar)

Relacionado: [[implementacion-bht-para-predictor-de-2-bits-4k-entradas-80-9]] · [[implementacion-predictor-correlacionado-m-n-con-bhr-y-bht]] · [[tabla-historica-de-predictores-en-procesadores-1989-1998]]
