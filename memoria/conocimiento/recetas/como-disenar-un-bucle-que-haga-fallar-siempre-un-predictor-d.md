---
tipo: "receta"
titulo: "Cómo diseñar un bucle que haga fallar siempre un predictor de 1 bit"
temas: ["ac", "prediccion-saltos", "predictores-1-bit"]
claves: ["predictor 1 bit", "fallo siempre", "bucle", "predicción estática"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4_Prob.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[prediccion-saltos]] · [[predictores-1-bit]]

Un predictor de 1 bit predice la próxima ocurrencia igual a la anterior. Para que falle siempre, el salto debe alternar su sentido (tomado/no tomado) en cada iteración. Ejemplo en C: `for (int i=0; i<N; i++) if (i%2==0) ...;` donde el salto del `if` se toma en iteraciones pares y no en impares (o viceversa). Así el predictor siempre espera lo contrario a lo que ocurre.

> Escribe un bucle (en C, por ejemplo) que contenga un salto tal que al aplicar un predictor de 1 bit, la predicción de ese salto dentro del bucle siempre falle.
> — `repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4_Prob.pdf`

Relacionado: [[alternativas-de-deteccion-de-instruccion-de-salto-en-pipelin]] · [[bht-branch-history-table-tabla-separada-para-bits-de-predicc]]
