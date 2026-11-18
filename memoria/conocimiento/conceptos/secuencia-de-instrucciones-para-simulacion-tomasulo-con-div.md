---
tipo: "concepto"
titulo: "Secuencia de instrucciones para simulación Tomasulo con DIV.D, ADD.D, MUL.D, S.D, L.D"
temas: ["ac", "tomasulo"]
claves: ["DIV.D", "ADD.D", "MUL.D", "S.D", "L.D", "emisión", "ejecución", "escritura resultado", "terminación", "ROB"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2016.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[tomasulo]]

Secuencia de 10 instrucciones FP para rellenar tabla de ciclos en Tomasulo: 1) DIV.D F0,F2,F4 2) ADD.D F2,F6,F8 3) ADD.D F0,F4,F8 4) S.D F0,0(R1) 5) MUL.D F2,F4,F0 6) DIV.D F6,F8,F0 7) L.D F6,0(R2) 8) ADD.D F0,F6,F2 9) MUL.D F2,F0,F8 10) ADD.D F2,F0,F6. Columnas: Emisión, Ejecución, Escritura resultado, Terminación (commit). Pregunta b) pide contenido del ROB en el ciclo de emisión de la instrucción 8 (ADD.D F0,F6,F2). Requiere conocer latencias funcionales típicas (ADD.D, MUL.D, DIV.D, L.D, S.D) y política de emisión en orden, ejecución fuera de orden, commit en orden.

> DIV.D F0, F2, F4 / ADD.D F2, F6, F8 / ADD.D F0, F4, F8 / S.D F0, 0(R1) / MUL.D F2, F4, F0 / DIV.D F6, F8, F0 / L.D F6, 0(R2) / ADD.D F0, F6, F2 / MUL.D F2, F0, F8 / ADD.D F2, F0, F6
> — `repo:datos/temarios/AC/examenes/Junio2016.pdf` (cita sin comprobar)

Relacionado: [[algoritmo-tomasulo-los-resultados-se-difunden-por-el-bus-com]] · [[buffer-de-reordenamiento-rob-en-tomasulo-con-especulacion-ca]] · [[analisis-de-dependencias-en-bucle-con-add-d-y-s-d-misma-iter]] · [[como-simular-tomasulo-especulativo-con-rob-de-4-entradas-y-l]] · [[secuencia-de-instrucciones-mips64-para-simulacion-tomasulo-p]] · [[simulacion-de-algoritmo-tomasulo-basico-y-especulativo-con-r]]
