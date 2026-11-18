---
tipo: "receta"
titulo: "Eliminación de dependencias de nombre mediante renombrado de registros en desenrollamiento"
temas: ["ac", "dependencias-nombre", "loop-unrolling", "optimizacion-compilador", "renombrado-registros", "war", "waw", "dependencias", "register-renaming"]
claves: ["dependencias nombre", "renombrado registros", "WAW", "WAR", "desenrollamiento", "registros flotantes f0 f4 f6 f8 f10 f12 f14 f16"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf", "repo:datos/temarios/AC/examenes/January2016.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[dependencias-nombre]] · [[loop-unrolling]] · [[optimizacion-compilador]] · [[renombrado-registros]] · [[war]] · [[waw]]

Al desenrollar un bucle, las instrucciones replicadas usan los mismos registros arquitectónicos → crean **dependencias de nombre** (falsas):
- **WAW (Write After Write)**: Dos `fld f0,...` escriben `f0`.
- **WAR (Write After Read)**: `fadd.d f4, f0, f2` lee `f0`; siguiente `fld f0,...` lo sobrescribe antes de que el `fadd` anterior lo use (si hay solapamiento).

**Solución: Renombrado de registros por compilador** (static register renaming).
En el ejemplo 4x:
- Iter 1: `f0`, `f4`
- Iter 2: `f6`, `f8`
- Iter 3: `f10`, `f12`
- Iter 4: `f14`, `f16`

Cada iteración usa registros físicos/distintos, rompiendo WAW/WAR. Requiere **mayor número de registros arquitectónicos disponibles** (presión de registros). El hardware Tomasulo hace esto dinámicamente con registros físicos + tabla de renombrado; aquí lo hace el compilador estáticamente.

> Hay que eliminar las dependencias de nombre • Renombrado de registros • Se necesita un mayor número de registros
> — `repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf` (cita sin comprobar)

Relacionado: [[aos-vs-soa-desperdicio-de-ancho-de-banda-en-cache]] · [[calculo-de-flops-ciclo-para-avx2-con-fma]]

## Ampliación (2026-11-18, )
Las dependencias de nombre (WAW y WAR) se eliminan con renombrado de registros (hardware o software). El desenrollado de bucles y trace scheduling no las eliminan por sí solos. Opción c).
