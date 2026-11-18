---
tipo: "concepto"
titulo: "Dependencias RAW, WAR y WAW en el bucle de producto escalar-vectorial (examen AC 2017/18)"
temas: ["ac", "dependencias", "pipeline", "raw", "war", "waw"]
claves: ["RAW F2", "RAW F4", "RAW F6", "WAR F6", "WAR R1", "WAR R2", "WAW F6"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2018.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[dependencias]] · [[pipeline]] · [[raw]] · [[war]] · [[waw]]

Dependencias en una iteración: RAW (verdaderas): F2: L.D → MUL.D (latencia 1). F4: MUL.D → ADD.D (latencia 3). F6: L.D → ADD.D (latencia 1) y ADD.D → S.D (latencia 2). R1: DADDUI → SLTI (latencia 0) y DADDUI → siguiente L.D (latencia 0). R2: DADDUI → siguiente L.D (latencia 0). WAR (antidependencias): F6: L.D (lectura) antes de ADD.D (escritura) → hazard WAR en pipeline in-order. R1/R2: SLTI/BEQZ leen antes de DADDUI escriban. WAW (salida-salida): F6 escrito por ADD.D y luego por siguiente iteración L.D (si no se renombra). El desenrollado y renombrado de registros (usar F2, F4, F6, F8, F10... para cada iteración) elimina WAR y WAW entre iteraciones.

> L.D F2, 0(R1) ; carga A(i) MUL.D F4, F2, F0 ; cte * A(i) L.D F6, 0(R2) ; carga B(i) ADD.D F6, F4, F6 ; cte * A(i) + B(i) S.D F6, 0(R2) ; almacena B(i)
> — `repo:datos/temarios/AC/examenes/Junio2018.pdf`

Relacionado: [[analisis-de-dependencias-en-bucle-con-add-d-y-s-d-misma-iter]] · [[antidependencia-war-en-bucle-entre-carga-y-actualizacion-de]] · [[antidependencia-entre-iteraciones-en-bucle-con-store-y-actua]]
