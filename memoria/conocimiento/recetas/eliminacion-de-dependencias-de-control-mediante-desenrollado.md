---
tipo: "receta"
titulo: "Eliminación de dependencias de control mediante desenrollado y eliminación de saltos intermedios"
temas: ["ac", "dependencia-control", "desenrollado-bucle", "eliminacion-saltos", "paralelismo-instruccion"]
claves: ["desenrollado-bucle", "loop-unrolling", "eliminacion-saltos", "branch-elimination", "dependencia-control", "riesgo-control"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema2-Paralelismo a nivel de instruccion/Tema2-2026-2027.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[dependencia-control]] · [[desenrollado-bucle]] · [[eliminacion-saltos]] · [[paralelismo-instruccion]]

El ejemplo muestra un bucle con un salto condicional (beqz) en medio del cuerpo. Al desenrollar una iteración y replicar las instrucciones de carga/cálculo/almacenado antes del salto, se elimina el salto intermedio y se reduce la frecuencia de riesgos de control. La versión transformada ejecuta dos iteraciones de trabajo por cada salto de bucle restante, mejorando ILP y reduciendo penalización de predicción errónea.

> Eliminando saltos intermedios. Otras técnicas… (pendientes de ver)
> — `repo:datos/temarios/AC/Tema2-Paralelismo a nivel de instruccion/Tema2-2026-2027.pdf` (cita sin comprobar)
