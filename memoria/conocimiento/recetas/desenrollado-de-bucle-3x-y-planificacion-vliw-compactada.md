---
tipo: "receta"
titulo: "Desenrollado de bucle 3x y planificación VLIW compactada"
temas: ["ac", "loop-unrolling", "planificacion", "vliw"]
claves: ["unroll 3x", "compactacion", "renombrado registros", "eliminacion saltos", "ILP"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2018.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[loop-unrolling]] · [[planificacion]] · [[vliw]]

Desenrollado 3x: replicar cuerpo del bucle 3 veces, ajustar índices y contadores, eliminar 2 de los 3 saltos.
- Original: 10 instrucciones/iteración, 1 salto/iteración.
- Desenrollado 3x: 30 instrucciones (3×10) - 2 saltos - 2×(DADDUI R1,R2,R3) fusionados = ~24 instrucciones útiles + 1 salto final.
- Renombrar registros para evitar dependencias WAR/WAW entre iteraciones: usar F2_1,F4_1,F6_1... F2_3,F4_3,F6_3 y R1_1,R2_1,R3_1... o mantener R1,R2,R3 con actualizaciones acumuladas.

Planificación compactada (software pipelining manual / list scheduling agresivo):
Objetivo: llenar 4 slots/ciclo respetando latencias. Al tener 3 iteraciones independientes, se pueden intercalar operaciones de distintas iteraciones para ocultar latencias.

Esquema típico de ciclos (ejemplo orientativo, la solución exacta requiere tabla ciclo a ciclo):
Ciclo 1: L.D F2_1, L.D F4_1, L.D F2_2, L.D F4_2
Ciclo 2: L.D F2_3, L.D F4_3, DADDUI R1_1, DADDUI R2_1
Ciclo 3: ADD.D F6_1, ADD.D F8_1, ADD.D F6_2, ADD.D F8_2
Ciclo 4: ADD.D F6_3, ADD.D F8_3, MUL.D F10_1, MUL.D F10_2
Ciclo 5: MUL.D F10_3, S.D F10_1, S.D F10_2, DADDUI R1_2
Ciclo 6: S.D F10_3, DADDUI R2_2, DADDUI R3_2, BNEZ R3_3 (salto final)
... (ajustar según dependencias reales)

Mejora: se reducen ciclos totales de ~3×7=21 a ~10-12 ciclos para 3 iteraciones → ~3.5-4 ciclos/iteración efectivos. Ops/ciclo suben de ~1.43 a ~2.5-3.0.

> Desenrolla el bucle original 3 veces y planifícalo para el procesador VLIW del apartado anterior. Compacta el código VLIW lo máximo posible. Se pueden realizar reordenamientos, siempre que no afecten al resultado del programa.
> — `repo:datos/temarios/AC/examenes/Enero2018.pdf`

Relacionado: [[desenrollado-de-bucle-loop-unrolling-3-para-vliw-y-compactac]] · [[desenrollamiento-de-bucle-3x-y-re-planificacion-en-vliw-para]] · [[planificacion-vliw-para-bucle-con-latencias-mem-2-add-d-1-mu]]
