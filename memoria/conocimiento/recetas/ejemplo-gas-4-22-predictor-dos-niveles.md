---
tipo: "receta"
titulo: "Ejemplo Gas(4,22) predictor dos niveles"
temas: ["ac", "prediccion-saltos", "yeh-patt"]
claves: ["Gas(4", "22)", "BHR 4 bits", "BHT 4 entradas"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[prediccion-saltos]] · [[yeh-patt]]

Gas(4,22) significa:
- G: historia global (un único BHR para todos los saltos).
- a: adaptativo (contadores de 2 bits en BHT).
- s: BHT por conjunto (set), seleccionada por los 2 bits menos significativos del PC (2² = 4 conjuntos).
- m=4: BHR de 4 bits (historia de los 4 últimos saltos globales).
- 2n=2²=4: cada BHT tiene 4 entradas.
Funcionamiento: el BHR global de 4 bits se usa como índice dentro de la BHT correspondiente al conjunto elegido por PC[1:0]. Cada entrada de la BHT es un contador saturado de 2 bits.

> Ejemplo: Gas(4,22) Un BHR de 4 bits contiene la historia de los 4 últimos saltos para indexar la BHT que seleccione los 2 últimos bits de la dirección de la instrucción de salto
> — `repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4.pdf` (cita sin comprobar)

Relacionado: [[notacion-xax-m-2n-para-predictores-adaptativos-de-dos-nivele]] · [[simulacion-de-predictor-correlacionado-de-dos-niveles-2-2-co]] · [[predictor-correlacionante-de-dos-niveles-1-1-con-bhr-global]]
