---
tipo: "receta"
titulo: "Desenrollado mínimo de bucle para planificación sin detenciones (secuencia 0,1,0,2)"
temas: ["ac", "desenrollado-bucles", "ilp"]
claves: ["desenrollado", "planificación", "detenciones", "ciclos por resultado"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2012.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[desenrollado-bucles]] · [[ilp]]

La secuencia tiene período 4 (0,1,0,2). Para eliminar detenciones por dependencias de control y datos, hay que desenrollar al menos 4 veces (una época completa). Al desenrollar 4 veces, los saltos B1 y B2 se vuelven predecibles estáticamente (patrón fijo T/NT), B3 solo salta al final. Se pueden reordenar instrucciones entre iteraciones para ocultar latencias de LW y ALU. El cálculo de ciclos por resultado requiere conocer latencias de pipeline (no dadas en el enunciado) y asumir predicción perfecta o predicción con BTB.

> c) Desenrolla el bucle el número mínimo de veces para poder planificarlo sin detenciones. Calcula el número de ciclos por resultado del código resultante.
> — `repo:datos/temarios/AC/examenes/Enero2012.pdf`
