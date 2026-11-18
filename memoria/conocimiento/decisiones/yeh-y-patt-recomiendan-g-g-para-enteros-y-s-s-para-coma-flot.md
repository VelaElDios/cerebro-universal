---
tipo: "decision"
titulo: "Yeh y Patt recomiendan G/g para enteros y S/s para coma flotante"
temas: ["ac", "prediccion-saltos", "yeh-patt"]
claves: ["G/g", "S/s", "códigos enteros", "códigos coma flotante"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[prediccion-saltos]] · [[yeh-patt]]

Basándose en sus experimentos, Yeh y Patt determinaron que la mejor configuración depende del tipo de código:
- G/g (historia global + BHT global): funciona mejor en códigos enteros, donde los saltos tienen correlación global.
- S/s (historia local por conjunto + BHT por conjunto): funciona mejor en códigos de coma flotante, donde los saltos muestran comportamiento local por dirección.
Esta decisión de diseño influyó en predictores posteriores como el Alpha 21264 que combina ambos enfoques.

> Experimentos de Yeh y Patt Usar G/g (global) en códigos enteros y S/s (local) en códigos de coma flotante
> — `repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4.pdf` (cita sin comprobar)

Relacionado: [[predictor-alpha-21264-tournament-branch-prediction-combina-l]] · [[predictor-gselect-concatenacion-vs-gshare-xor-para-indexar-b]] · [[notacion-xax-m-2n-para-predictores-adaptativos-de-dos-nivele]]
