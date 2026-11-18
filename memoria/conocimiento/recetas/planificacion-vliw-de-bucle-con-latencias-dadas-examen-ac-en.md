---
tipo: "receta"
titulo: "Planificación VLIW de bucle con latencias dadas (examen AC enero 2018)"
temas: ["ac", "bucle", "ilp", "planificacion", "vliw"]
claves: ["VLIW", "4 operaciones por instrucción", "L.D", "ADD.D", "MUL.D", "S.D", "DADDUI", "BNEZ", "latencia MEM 2 ciclos", "latencia EX ADD 1 ciclo", "latencia EX MUL 2 ciclos", "sin salto retardado"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2018.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[bucle]] · [[ilp]] · [[planificacion]] · [[vliw]]

El bucle original tiene 10 instrucciones: 2 cargas (L.D, 2 ciclos MEM), 2 sumas FP (ADD.D, 1 ciclo EX), 1 multiplicación FP (MUL.D, 2 ciclos EX), 1 almacenamiento (S.D, 2 ciclos MEM), 3 enteros (DADDUI, 1 ciclo EX asumido), 1 salto (BNEZ). En VLIW de 4 ops/instrucción sin restricciones de ALU, se deben agrupar en paquetes de hasta 4 ops respetando dependencias RAW (F2/F4 de cargas → ADD.D → MUL.D → S.D; R1/R2/R3 actualizados por DADDUI → siguientes iteraciones). La planificación requiere insertar NOPs o reordenar para cubrir latencias. La tabla del examen tiene 10 ciclos (Cycle1–Cycle10) para rellenar.

> Schedule the next loop for a VLIW processor with four operations per instruction and without restrictions regarding to the type of operations that can be issued to each ALU.
> — `repo:datos/temarios/AC/examenes/January2018.pdf`
