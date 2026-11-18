---
tipo: "receta"
titulo: "Planificación en VLIW 4 operaciones sin restricciones de tipo (emisión agresiva out-of-order estática)"
temas: ["ac", "examen", "pipeline", "vliw"]
claves: ["Processor B", "VLIW", "issue 4 operations per instruction", "no type restrictions", "static scheduling aggressive"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2022.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[examen]] · [[pipeline]] · [[vliw]]

VLIW: cada instrucción (palabra larga) contiene 4 operaciones que se emiten simultáneamente en un ciclo. No hay restricción de mezcla (pueden ser 4 FP, 4 enteras, o cualquier combinación). Planificación estática agresiva: reordenar libremente (out-of-order estático) respetando dependencias verdaderas (RAW) y latencias funcionales (L.D 2 ciclos, ADD.D 1, MUL.D 3, S.D necesita dato listo, DADDUI 1, BNEZ 2 delay slots). Renombrado ya hecho en desenrollado. Objetivo: empaquetar 4 ops/ciclo lo más posible. Delay slots del BNEZ: las 2 ops siguientes en la palabra de instrucción (o siguientes palabras) se ejecutan siempre. Tabla de salida: Cycle | Operation 1 | Operation 2 | Operation 3 | Operation 4.

> Processor B. VLIW that can issue in each cycle four operations per instruction and imposes no restrictions on the type of operations that can be issued.
> — `repo:datos/temarios/AC/examenes/June2022.pdf`

Relacionado: [[desenrollado-4x-de-bucle-mips64-fp-con-renombrado-de-registr]]
