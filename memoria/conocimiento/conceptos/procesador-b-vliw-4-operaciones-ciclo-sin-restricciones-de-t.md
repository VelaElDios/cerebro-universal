---
tipo: "concepto"
titulo: "Procesador B: VLIW 4 operaciones/ciclo sin restricciones de tipo, scheduling estático agresivo"
temas: ["ac", "pipeline", "saas"]
claves: ["VLIW", "static scheduling", "register renaming", "out-of-order scheduling", "issue width"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2021.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]] · [[saas]]

Características del procesador VLIW del enunciado:
- **Modelo**: VLIW (Very Long Instruction Word), cada instrucción contiene 4 operaciones que se emiten en paralelo en un ciclo.
- **Sin restricciones de tipo**: las 4 operaciones pueden ser de cualquier mezcla (enteras, FP, memoria, salto).
- **Scheduling estático agresivo**: el compilador reordena instrucciones (out-of-order scheduling) y usa **renombrado de registros** para eliminar dependencias falsas (WAR, WAW) y maximizar ILP.
- **Objetivo**: empaquetar las 40 instrucciones del bucle desenrollado 8× en el menor número de ciclos posible, respetando solo las latencias reales (RAW) y la disponibilidad de unidades funcionales (implícitamente ilimitadas o al menos 4 por ciclo sin conflictos estructurales).
- **Ventaja frente al superscalar**: al no tener límite de 2 enteras + 2 FP, puede emitir p.ej. 4 L.D en un ciclo si las latencias lo permiten, o mezclar 3 FP + 1 entero, etc.

> Processor B. It is a VLIW processor, capable of issuing in each cycle four operations per instruction. It does not impose restrictions on the type of operations that can be issued.
> — `repo:datos/temarios/AC/examenes/January2021.pdf`

Relacionado: [[configuracion-vliw-de-6-unidades-funcionales-con-latencias-a]]
