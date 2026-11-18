---
tipo: "receta"
titulo: "Bucle RISC-V para calibración IMU con puntero descendente"
temas: ["ac", "ensamblador", "pipeline", "risc-v"]
claves: ["fld", "fmul.d", "fadd.d", "fsd", "addi", "bne", "x10", "x11", "f0", "f4"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2026.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[ensamblador]] · [[pipeline]] · [[risc-v]]

Traducción directa del C a ensamblador RISC-V. x10 apunta a lecturas[N-1] (último elemento), x11 = lecturas[0] - 8 (dirección de parada). El bucle carga double (8 bytes) con fld, multiplica por gain (f0), suma offset (f4), almacena con fsd, decrementa puntero 8 bytes (addi -8) y salta si x10 != x11. Registros FP: f1 temporal carga, f2 resultado mul, f3 resultado add.

> loop: fld f1, 0(x10); fmul.d f2, f1, f0; fadd.d f3, f2, f4; fsd f3, 0(x10); addi x10, x10, -8; bne x10, x11, loop
> — `repo:datos/temarios/AC/examenes/Junio2026.pdf` (cita sin comprobar)

Relacionado: [[analisis-de-dependencias-en-bucle-con-add-d-y-s-d-misma-iter]] · [[antidependencia-war-en-bucle-entre-carga-y-actualizacion-de]] · [[desenrollamiento-de-bucles-4x-con-planificacion-para-elimina]] · [[desenrollamiento-de-bucles-loop-unrolling-4x-con-renombrado]] · [[calculo-de-direcciones-y-offsets-en-bucles-vectoriales-risc]]
