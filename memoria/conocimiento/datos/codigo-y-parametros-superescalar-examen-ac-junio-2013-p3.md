---
tipo: "dato"
titulo: "Código y parámetros superescalar examen AC Junio 2013 P3"
temas: ["ac", "pipeline", "superscalar"]
claves: ["superescalar grado 2", "LW", "DADD", "DSUB", "MEM 2 ciclos", "EX 2 ciclos", "adelantamiento"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2013.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]] · [[superscalar]]

Código completo (7 instrucciones enteras MIPS64):
1. LW   R2, 0(R3)      ; carga R2
2. DADD R4, R2, R5     ; R4 = R2 + R5
3. DSUB R6, R7, R8     ; R6 = R7 - R8
4. LW   R5, 0(R10)     ; carga R5 (sobrescribe R5)
5. DSUB R9, R9, R13    ; R9 = R9 - R13
6. DADD R8, R8, R2     ; R8 = R8 + R2 (sobrescribe R8)
7. DSUB R5, R5, R2     ; R5 = R5 - R2 (sobrescribe R5)

Parámetros máquina:
- Superescalar grado 2: emite hasta 2 instr/ciclo, cualquier tipo
- Etapa EX aritmética (DADD/DSUB): 2 ciclos
- Etapa MEM carga (LW): 2 ciclos
- Adelantamiento (forwarding) implementado: resultado disponible al final de EX/MEM para instrucciones siguientes
- Ventana de instrucciones: "lo suficientemente grande" para ver las 7 a la vez (apartados b y c)

Dependencias RAW verdaderas:
- R2: (1) → (2), (6), (7)
- R5 (valor viejo): (2) lee R5 viejo; (4) escribe R5 nuevo → WAR si (4) antes que (2) lea
- R5 (valor nuevo): (4) → (7)
- R8: (3) lee R8 viejo; (6) escribe R8 nuevo → WAR si (6) antes que (3) lea
- R8 (valor viejo): (3) → (6) lee R8 viejo? No, (6) lee R8 (valor viejo) y R2 → RAW (3)→(6) en R8
- R9: (5) lee y escribe R9 (dependencia interna, no inter-instrucción)

WAW: (2) escribe R4, (4) escribe R5, (6) escribe R8, (7) escribe R5 → WAW en R5 entre (4) y (7)
WAR: (2) lee R5 viejo vs (4) escribe R5 nuevo; (3) lee R8 viejo vs (6) escribe R8 nuevo

> LW R2, 0(R3); DADD R4, R2, R5; DSUB R6, R7, R8; LW R5, 0(R10); DSUB R9, R9, R13; DADD R8, R8, R2; DSUB R5, R5, R2
> — `repo:datos/temarios/AC/examenes/Junio2013.pdf` (cita sin comprobar)

Relacionado: [[bucle-vectorial-de-referencia-para-desenrollado-y-planificac]] · [[analisis-de-dependencias-en-bucle-con-add-d-y-s-d-misma-iter]]
