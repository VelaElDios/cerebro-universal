---
tipo: "concepto"
titulo: "Problema de desenrollado y planificación de bucle superescalar con latencias dadas (examen AC 2017/18)"
temas: ["ac", "desenrollado", "pipeline", "planificacion", "superescalar"]
claves: ["desenrollar 4 veces", "planificar mínimo ciclos", "speedup", "tabla emisión/ejecución"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2018.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[desenrollado]] · [[pipeline]] · [[planificacion]] · [[superescalar]]

Ejercicio típico de planificación de instrucciones (instruction scheduling) para procesador superescalar con emisión en orden (in-order issue) pero ejecución fuera de orden (out-of-order execution) gracias a unidades funcionales segmentadas y latencias conocidas. El desenrollado 4 veces (unroll factor 4) permite exponer más paralelismo a nivel de instrucción (ILP) y ocultar latencias. La planificación busca minimizar ciclos totales reordenando instrucciones respetando dependencias (RAW, WAR, WAW) y restricciones de recursos (2 emisiones/ciclo, 1 unidad PF add, 1 PF mul, 2 enteras). El speedup se calcula como (ciclos iteración original) / (ciclos totales desenrollado / 4).

> A) Desenrolla el bucle 4 veces y planifícalo tal que emplee el menor número de ciclos. Escribe la solución en la tabla adjunta (Usa tantas filas como necesites) B) ¿Cuántos ciclos invertirá cada iteración en el código original? ¿Cuál es el speedup de la versión desenrollada y planificada con respecto al código original?
> — `repo:datos/temarios/AC/examenes/Junio2018.pdf`

Relacionado: [[analisis-de-dependencias-en-bucle-con-add-d-y-s-d-misma-iter]] · [[antidependencia-entre-iteraciones-en-bucle-con-store-y-actua]] · [[metodo-para-calcular-speedup-de-bucle-desenrollado-y-planifi]] · [[planificacion-en-superescalar-3-vias-entero-salto-memoria-fp]] · [[desenrollamiento-de-bucle-3x-y-re-planificacion-en-vliw-para]]
