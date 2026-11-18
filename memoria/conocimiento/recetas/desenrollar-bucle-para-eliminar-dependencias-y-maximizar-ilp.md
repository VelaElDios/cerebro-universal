---
tipo: "receta"
titulo: "Desenrollar bucle para eliminar dependencias y maximizar ILP (Ejercicio 2)"
temas: ["ac", "dependencias-datos", "desenrollamiento", "planificacion-estatica", "recurrencia"]
claves: ["A[i]=A[i-3]+A[i", "latencia ALU PF->ALU PF 3", "ALU PF->fsd 2", "fld->ALU PF 1", "fld->fsd 0", "unidades segmentadas"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3_Prob.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[dependencias-datos]] · [[desenrollamiento]] · [[planificacion-estatica]] · [[recurrencia]]

El bucle tiene una recurrencia de distancia 3: A[i] depende de A[i-3]. Latencias: fld->fadd.d (ALU PF) 1 ciclo, fadd.d->fsd 2 ciclos, fadd.d->fadd.d (ALU PF->ALU PF) 3 ciclos. Para eliminar stalls, desenrollar al menos 3 veces (factor 3) para romper la cadena de dependencias entre iteraciones consecutivas. Tras desenrollar, renombrar registros (f2,f4,f6,f8,f10,f12...) y planificar instrucciones de distintas iteraciones intercaladas: cargas tempranas, sumas cuando operandos listos, stores tras latencia 2. Al ser UF segmentadas, se puede iniciar una fadd.d cada ciclo si no hay conflictos estructurales. El desenrollamiento 3x permite tener 3 sumas en vuelo simultáneo.

> Desenrolla tantas veces como sea necesario, elimina dependencias y planifica para maximizar el ILP. Ignora el retardo del salto. Asume que las unidades funcionales están segmentadas.
> — `repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3_Prob.pdf`

Relacionado: [[desenrollar-bucle-2x-y-planificar-para-latencias-fp-dadas-ej]] · [[desenrollar-bucle-minimo-para-planificar-sin-detenciones-eje]] · [[desenrollado-de-bucle-8-veces-para-superscalar-con-latencias]]
