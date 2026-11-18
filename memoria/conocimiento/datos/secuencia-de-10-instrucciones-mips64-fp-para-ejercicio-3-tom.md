---
tipo: "dato"
titulo: "Secuencia de 10 instrucciones MIPS64 FP para ejercicio 3 Tomasulo"
temas: ["ac", "especulacion", "mips64", "tomasulo"]
claves: ["L.S F1", "0(R2)", "MUL.S F1", "F1", "F0", "L.S F2", "4(R2)", "ADD.S F2", "F1", "F2", "S.S F2", "8(R2)", "L.S F1", "4(R2)", "MUL.S F1", "F1", "F0", "L.S F2", "8(R2)", "ADD.S F2", "F1", "F2", "S.S F2", "12(R2)"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January 2025.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[especulacion]] · [[mips64]] · [[tomasulo]]

Código exacto del ejercicio 3 (10 instrucciones): 1) L.S F1,0(R2) 2) MUL.S F1,F1,F0 3) L.S F2,4(R2) 4) ADD.S F2,F1,F2 5) S.S F2,8(R2) 6) L.S F1,4(R2) 7) MUL.S F1,F1,F0 8) L.S F2,8(R2) 9) ADD.S F2,F1,F2 10) S.S F2,12(R2). Hay dependencias RAW (F1, F2), reuso de registros (F1, F2), y accesos a memoria solapados. La simulación debe considerar latencias dadas y recursos (unidades funcionales, CDB) aunque el número de estaciones de reserva no se especifica en el trozo (está en la figura no incluida).

> L.S      F1, 0(R2) MUL.S    F1, F1, F0 L.S      F2, 4(R2) ADD.S    F2, F1, F2 S.S      F2, 8(R2) L.S      F1, 4(R2) MUL.S    F1, F1, F0 L.S      F2, 8(R2) ADD.S    F2, F1, F2 S.S      F2, 12(R2)
> — `repo:datos/temarios/AC/examenes/January 2025.pdf`
