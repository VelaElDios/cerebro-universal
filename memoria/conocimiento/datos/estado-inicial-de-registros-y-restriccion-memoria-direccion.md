---
tipo: "dato"
titulo: "Estado inicial de registros y restricción memoria dirección 0 en examen AC Enero 2014 P3"
temas: ["ac", "arquitectura", "examenes"]
claves: ["R1=10", "R2=0", "R3=0", "R4=4", "R5=5", "R6=6", "R7=7", "R8=8", "R9=9", "dirección 0 prohibida"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2014.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[arquitectura]] · [[examenes]]

Valores iniciales: R1=10, R2=0, R3=0, R4=4, R5=5, R6=6, R7=7, R8=8, R9=9. Restricción crítica: R2=0, por lo que las instrucciones LW* R1,0(R2) y LW* R5,0(R2) intentan acceder a dirección 0, lo cual lanza excepción por acceso ilegal. Los saltos: BEQZ R3,salto1 (R3=0 → salta), BEQZ R6,salto2 (R6=6 ≠ 0 → no salta).

> estado inicial es: R1 10 R2 0 R3 0 R4 4 R5 5 R6 6 R7 7 R8 8 R9 9" y "el acceso a la dirección de memoria 0 está prohibido (cualquier intento de leer o escribir en dicha posición lanzará una excepción por acceso ilegal)
> — `repo:datos/temarios/AC/examenes/Enero2014.pdf` (cita sin comprobar)

Relacionado: [[especulacion-estatica-con-cargas-especulativas-lw-en-mips64]] · [[tres-mecanismos-de-especulacion-evaluados-en-examen-ac-enero]]
