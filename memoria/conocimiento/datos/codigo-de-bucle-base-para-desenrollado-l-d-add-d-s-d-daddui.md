---
tipo: "dato"
titulo: "Código de bucle base para desenrollado: L.D, ADD.D, S.D, DADDUI, BNE con R2/R3 como límites"
temas: ["ac", "pipeline", "tomasulo"]
claves: ["loop", "L.D", "ADD.D", "S.D", "DADDUI", "BNE", "R2", "R3", "memory addresses"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2021.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]] · [[tomasulo]]

Bucle original (5 instrucciones, itera hacia direcciones decrecientes):
| Instrucción | Significado |
|---|---|
| `L.D  F10, 0(R2)` | Carga double FP desde dirección en R2 → F10 |
| `ADD.D F8, F10, F12` | Suma FP: F8 = F10 + F12 (F12 invariante) |
| `S.D  F8, 0(R2)` | Almacena F8 en misma dirección (R2) |
| `DADDUI R2, R2, -8` | Decrementa puntero R2 en 8 bytes (siguiente double) |
| `BNE  R2, R3, Bucle` | Salta si R2 ≠ R3 (límite final) |

**Dependencias por iteración:**
- RAW: `L.D → ADD.D` (F10), `ADD.D → S.D` (F8), `DADDUI → BNE` (R2), `DADDUI → L.D(next)` (R2).
- WAR/WAW: F10, F8, R2 se reescriben cada iteración → **renombrado de registros** esencial en VLIW y útil en superscalar para evitar stalls por dependencias falsas.
**Direccionamiento**: R2 inicial = dirección inicial, R3 = dirección final (menor). El bucle recorre array de doubles hacia atrás.

> Given the following code fragment, where R2 and R3 contain the initial and final memory addresses where the data are stored: Bucle: L.D F10, 0(R2) ADD.D F8, F10, F12 S.D F8, 0(R2) DADDUI R2, R2, -8 BNE R2, R3, Bucle
> — `repo:datos/temarios/AC/examenes/January2021.pdf`

Relacionado: [[definicion-de-dependencia-de-datos-raw-entre-instrucciones]] · [[clasificacion-de-dependencias-en-bucle-antidependencia-war-e]]
