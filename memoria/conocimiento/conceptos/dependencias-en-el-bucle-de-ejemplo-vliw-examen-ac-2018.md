---
tipo: "concepto"
titulo: "Dependencias en el bucle de ejemplo VLIW (examen AC 2018)"
temas: ["ac", "dependencias", "ilp", "raw", "vliw", "war", "waw"]
claves: ["RAW F2/F4", "RAW F6/F10", "WAW R1/R2/R3", "dependencia memoria 0(R1)/0(R2)", "contador bucle R3"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2018.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[dependencias]] · [[ilp]] · [[raw]] · [[vliw]] · [[war]] · [[waw]]

Cadena de dependencias RAW: L.D F2 → ADD.D F6 → MUL.D F10 → S.D F10 (latencias 2+1+2+2=7 ciclos mínimo); L.D F4 → ADD.D F8 (usa F2 también) → MUL.D F10; DADDUI R1/R2 actualizan punteros para siguiente iteración (WAW entre iteraciones); DADDUI R3 decrementa contador, BNEZ R3 salta (dependencia de control). No hay dependencias WAR/WAW en registros FP dentro de una iteración (registros destino distintos: F2,F4,F6,F8,F10). La memoria 0(R1) y 0(R2) son direcciones distintas si R1≠R2.

> Loop: L.D F2, 0(R1); L.D F4, 0(R2); ADD.D F6, F2, F2; ADD.D F8, F4, F2; MUL.D F10,F4, F6; S.D F10, 0(R1); DADDUI R1, R1, #8; DADDUI R2, R2, #8; DADDUI R3, R3, #-1; BNEZ R3, Loop
> — `repo:datos/temarios/AC/examenes/January2018.pdf` (cita sin comprobar)

Relacionado: [[planificacion-vliw-de-bucle-con-latencias-dadas-examen-ac-en]]
