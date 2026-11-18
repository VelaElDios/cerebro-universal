---
tipo: "receta"
titulo: "Desenrollado de bucle 4x con salto retardado para eliminar stalls en pipeline in-order"
temas: ["ac", "delayed-branch", "loop-unrolling", "optimizacion", "pipeline"]
claves: ["desenrollar 4 veces", "renombrar registros", "reordenar", "salto retardado", "N múltiplo 4"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2026.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[delayed-branch]] · [[loop-unrolling]] · [[optimizacion]] · [[pipeline]]

Técnica estándar: replicar cuerpo del bucle 4 veces (4 iteraciones por vuelta). Renombrar registros destino (f1..f12, f2..f13, etc.) para evitar dependencias WAR/WAW entre iteraciones. Reordenar instrucciones para ocultar latencias: intercalar cargas, muls, adds, stores de distintas iteraciones. Usar salto retardado (delayed branch): colocar instrucciones útiles en el slot de retardo del bne (o reorganizar para que el salto se evalúe antes). Actualizar punteros (addi x10, x10, -32) una vez por 4 iteraciones. Condición de fin: comparar x10 con x11 (lecturas[0]-8) tras decrementar 32 bytes.

> Desenrolla el código ensamblador 4 veces y planifica el código (renombra y reordena) para eliminar todas las detenciones posibles. Muestra el código resultante. Asume que N es múltiplo de 4 y que aplicamos la técnica de salto retardado.
> — `repo:datos/temarios/AC/examenes/Junio2026.pdf`

Relacionado: [[analisis-de-dependencias-en-bucle-con-add-d-y-s-d-misma-iter]] · [[antidependencia-entre-iteraciones-en-bucle-con-store-y-actua]] · [[desenrollado-4x-de-bucle-mips64-fp-con-renombrado-de-registr]] · [[desenrollado-de-bucle-minimo-para-planificacion-sin-detencio]] · [[desenrollado-de-bucle-minimo-para-eliminar-todos-los-stalls]]
