---
tipo: "dato"
titulo: "Latencias de unidades funcionales VLIW examen enero 2023: Integer FU, Adder FP FU, Multiplier FP FU, MEM stage"
temas: ["ac", "pipeline", "vliw"]
claves: ["Integer FU", "Adder FP FU", "Multiplier FP FU", "MEM stage", "cycles", "latencia"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2023.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]] · [[vliw]]

Tabla a rellenar en el ejercicio 3a. Las latencias esperadas (típicas en este tipo de exámenes) son: Integer FU (DADDUI) = 1 ciclo; Adder FP FU (ADD.D) = 4 ciclos; Multiplier FP FU (MUL.D) = 6 ciclos; MEM stage (L.D, S.D) = 2 ciclos (1 para dirección + 1 para acceso). El procesador usa forwarding y salto retardado, por lo que las latencias determinan los NOPs necesarios entre instrucciones dependientes en el código original.

> FU= Functional unit Number of cycles Integer FU Adder FP FU Multiplier FP FU MEM stage of the memory access instructions
> — `repo:datos/temarios/AC/examenes/January2023.pdf`

Relacionado: [[configuracion-vliw-de-6-unidades-funcionales-con-latencias-a]]
