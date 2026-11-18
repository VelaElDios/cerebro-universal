---
tipo: "receta"
titulo: "Desenrollado 8× del bucle L.D/ADD.D/S.D/DADDUI/BNE para scheduling superscalar vs VLIW"
temas: ["ac", "pipeline", "tomasulo"]
claves: ["loop unrolling", "8 times", "L.D", "ADD.D", "S.D", "DADDUI", "BNE", "register renaming"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2021.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]] · [[tomasulo]]

**Código original (1 iteración):**
```
L.D    F10, 0(R2)
ADD.D  F8, F10, F12
S.D    F8, 0(R2)
DADDUI R2, R2, -8
BNE    R2, R3, Bucle
```
**Desenrollado 8× (40 instrucciones):** se replican 8 veces cambiando registros para evitar dependencias falsas (renombrado). Ejemplo de renombrado por iteración *i* (0..7):
- `L.D  F10_i, 0(R2_i)`  (R2_i = R2 - 8*i)
- `ADD.D F8_i, F10_i, F12`  (F12 invariante)
- `S.D  F8_i, 0(R2_i)`
- `DADDUI R2_{i+1}, R2_i, -8`  (encadenamiento de puntero)
- `BNE  R2_{i+1}, R3, Bucle`  (salto condicional)

**Dependencias RAW reales (con latencias dadas):**
1. `L.D → ADD.D` : 1 ciclo (L.D produce F10_i, ADD.D lo consume).
2. `ADD.D → S.D` : 1 ciclo (ADD.D produce F8_i, S.D lo consume).
3. `L.D → S.D` : 0 ciclos (forwarding directo, pero S.D usa F8_i de ADD.D, no F10_i; la latencia L.D→S.D=0 sería si S.D usara F10_i, pero aquí usa F8_i, así que la ruta crítica es L.D→ADD.D→S.D = 1+1=2 ciclos desde L.D hasta S.D).
4. `DADDUI → BNE` : salto retardado → la instrucción en *delay slot* (si la hay) se ejecuta siempre; BNE usa R2_{i+1} producido por DADDUI. En MIPS clásico, la latencia ALU→branch es 0 con forwarding, pero aquí no se da explícitamente; se asume 0 o 1 según arquitectura.
5. `DADDUI → L.D (next iter)` : R2_{i+1} usado como base en L.D de la siguiente iteración. Latencia ALU→L.D (entera) no dada; se asume 0 con forwarding.

**Para Processor A (superscalar 2int+2FP/ciclo):** emitir en tabla ciclos × 4 columnas (Instr1..Instr4) respetando máx 2 int + 2 FP por ciclo y latencias.
**Para Processor B (VLIW 4 ops/ciclo):** empaquetar en filas de 4 operaciones (Op1..Op4) sin límite de tipo, reordenando libremente con renombrado.

> unroll 8 times the code and schedule it as compact as possible... assuming that static scheduling is as aggressive as possible and as efficient and possible to optimize the resulting code. You can use register renaming and out-of-order scheduling.
> — `repo:datos/temarios/AC/examenes/January2021.pdf` (cita sin comprobar)

Relacionado: [[criterio-de-desenrollamiento-de-bucles-loop-unrolling]] · [[definicion-de-dependencia-de-datos-raw-entre-instrucciones]] · [[antidependencia-war-y-dependencia-de-salida-waw-definiciones]] · [[codigo-de-bucle-base-para-desenrollado-l-d-add-d-s-d-daddui]] · [[desenrollado-de-bucle-8-veces-para-superscalar-con-latencias]] · [[como-desenrollar-8x-y-planificar-en-superescalar-4-issue-2-i]]
