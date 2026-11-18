---
tipo: "concepto"
titulo: "Problema de planificación VLIW con desenrollado de bucle (examen AC enero 2016)"
temas: ["ac", "desenrollado-bucle", "examen", "planificacion", "vliw"]
claves: ["VLIW", "4 operaciones por instrucción", "forwarding", "delayed branch", "loop unrolling", "scheduling"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2016.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[desenrollado-bucle]] · [[examen]] · [[planificacion]] · [[vliw]]

Este es un problema clásico de examen de Arquitectura de Computadores sobre planificación estática en VLIW. El procesador emite paquetes de hasta 4 operaciones por ciclo sin restricciones de tipo (pueden ser cualquier mezcla de carga/almacenamiento, aritmética FP, aritmética entera, salto). Dispone de forwarding (evita paradas por dependencias RAW) y delayed branch (la instrucción tras el salto se ejecuta siempre). El bucle original tiene 10 instrucciones; desenrollado 4 veces da 40 instrucciones que deben colocarse en los huecos de 20 ciclos mostrados, respetando latencias: MEM=2 ciclos (L.D/S.D), EX=2 ciclos (ADD.D/MUL.D/DIV.D), resto=1 ciclo (DADDUI, BNEZ). La solución requiere reordenar instrucciones de distintas iteraciones para llenar huecos de latencia y maximizar ILP.

> Exercise 3. The next code is run in a VLIW processor with 4 operations per instruction, which does not impose restrictions to the type of operations that can be issued per cycle. Consider also that this processor supports forwarding and delayed branch.
> — `repo:datos/temarios/AC/examenes/January2016.pdf`

Relacionado: [[algoritmo-tomasulo-origen-y-objetivo-cpi1]]
