---
tipo: "concepto"
titulo: "Desenrollado de bucle (loop unrolling) 3× para VLIW y compactación"
temas: ["ac", "ilp", "loop-unrolling", "optimizacion", "vliw"]
claves: ["unroll 3 veces", "compactar código VLIW", "reordenar instrucciones sin afectar comportamiento", "eliminar overhead de salto", "aumentar ILP"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2018.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[ilp]] · [[loop-unrolling]] · [[optimizacion]] · [[vliw]]

Desenrollar 3 veces replica el cuerpo del bucle 3 veces, ajustando offsets de memoria (R1, R2 avanzan 8 bytes por iteración original → 24 bytes totales) y el contador de bucle (R3 decrementa 3 por iteración desenrollada). Se eliminan 2 de los 3 saltos BNEZ y sus DADDUI asociados al contador. Luego se reordenan todas las instrucciones de las 3 iteraciones para llenar paquetes VLIW de 4 ops, respetando dependencias y latencias, minimizando NOPs. La tabla vuelve a tener 10 ciclos (Cycle1–Cycle10) para la versión compactada.

> Unroll 3 times the original loop and schedule it for this VLIW processor. Use the table. Compact the VLIW code as much as possible. You can reorder the instructions, without affecting the program behavior.
> — `repo:datos/temarios/AC/examenes/January2018.pdf`

Relacionado: [[planificacion-vliw-de-bucle-con-latencias-dadas-examen-ac-en]]
