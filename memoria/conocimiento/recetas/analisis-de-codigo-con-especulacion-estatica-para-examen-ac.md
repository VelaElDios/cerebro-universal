---
tipo: "receta"
titulo: "Análisis de código con especulación estática para examen AC"
temas: ["ac", "arquitectura", "examenes", "prediccion-saltos"]
claves: ["LW*", "BEQZ", "DADDI", "DADD", "SW", "especulación estática", "análisis flujo control"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2014.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[arquitectura]] · [[examenes]] · [[prediccion-saltos]]

Flujo de control con valores iniciales: R3=0 → BEQZ R3,salto1 SALTA a Salto1 (se salta DADDI R1,R4,#8). R6=6 ≠ 0 → BEQZ R6,salto2 NO SALTA, ejecuta DADDI R5,R7,#-1 (R5=7-1=6). Luego DADD R8,R1,R5, SW R8,0(R2) (escritura en dir 0 → excepción), DADDI R9,R0,#1 (R9=1). Las dos LW* son especulativas: primera en ruta de salto no tomado (se salta), segunda en ruta de salto tomado (se ejecuta). Ambas acceden a dir 0.

> LW*   R1, 0(R2)                ; Carga especulativa\n                 BEQZ R3, salto1\n                 DADDI R1, R4, #8\n     Salto1:     LW*   R5, 0(R2)                ; Carga especulativa\n                 BEQZ R6, salto2\n                 DADDI R5, R7, #-1\n     Salto2:     DADD R8, R1, R5\n                 SW    R8, 0(R2)\n                 DADDI R9, R0, #1
> — `repo:datos/temarios/AC/examenes/Enero2014.pdf` (cita sin comprobar)

Relacionado: [[estado-inicial-de-registros-y-restriccion-memoria-direccion]] · [[tres-mecanismos-de-especulacion-evaluados-en-examen-ac-enero]]
