---
tipo: "receta"
titulo: "Desenrollar bucle mínimo para planificar sin detenciones (Ejercicio 3)"
temas: ["ac", "acumulador", "desenrollamiento", "planificacion-estatica", "reduccion"]
claves: ["f2 acumulador inicial cero", "fmul.d latencia 4", "fadd.d latencia 2", "fld->ALU PF 1", "fld->fsd 0", "bne salto"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3_Prob.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[acumulador]] · [[desenrollamiento]] · [[planificacion-estatica]] · [[reduccion]]

Bucle con reducción: f2 = f2 + (f0 * f4) cada iteración. Dependencia en f2 (acumulador) y en f0 (resultado de mul). Latencias: fmul.d 4 ciclos (EX), fadd.d 2 ciclos. Para evitar detenciones, el desenrollamiento debe permitir que la fadd.d de una iteración no espere a la fmul.d de la misma. Mínimo factor 2: desenrollar 2 veces, usar dos acumuladores parciales (f2 y f10) y combinarlos al final. Planificar: carga f0,f4 -> mul f0 -> carga siguiente par -> mul f10 -> add f2,f0 -> add f10,f10 -> ... respetando latencias. Al final, sumar los dos acumuladores. Verificar que el resultado final equivale a la ejecución secuencial original.

> Desenrolla el bucle el número mínimo de veces para poder planificarlo sin detenciones. Supón f2 inicialmente a cero, y ten en cuenta que el resultado obtenido con el nuevo código debe ser el mismo que con el original.
> — `repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3_Prob.pdf`

Relacionado: [[desenrollar-bucle-2x-y-planificar-para-latencias-fp-dadas-ej]] · [[desenrollar-bucle-para-eliminar-dependencias-y-maximizar-ilp]]
