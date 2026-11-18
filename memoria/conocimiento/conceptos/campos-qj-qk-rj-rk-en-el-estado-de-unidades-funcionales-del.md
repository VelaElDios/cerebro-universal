---
tipo: "concepto"
titulo: "Campos Qj, Qk, Rj, Rk en el estado de unidades funcionales del marcador"
temas: ["ac", "arquitectura", "dependencias", "hazard", "qj", "qk", "rj", "rk", "scoreboard"]
claves: ["Qj", "Qk", "Rj", "Rk", "unidad funcional", "operando", "listo", "dependencia"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[arquitectura]] · [[dependencias]] · [[hazard]] · [[qj]] · [[qk]] · [[rj]] · [[rk]] · [[scoreboard]]

Significado y uso de los cuatro campos de dependencia en cada fila de UF:

- **Qj / Qk** (número de UF productor): indican **qué unidad funcional producirá el operando Fj/Fk**. Valor 0 = operando ya disponible en registro. En el ejemplo:
  - `fmul.d` en Mult1 (UF 2): Fj=f2 → Qj=1 (UF Entera produce f2), Fk=f4 → Qk=0 (f4 ya en registro).
  - `fsub.d` en Suma (UF 4): Fj=f6 → Qj=1, Fk=f2 → Qk=1 (ambos vienen de UF Entera).
  - `fdiv.d` en Divide (UF 5): Fj=f0 → Qj=2 (Mult1 produce f0), Fk=f6 → Qk=1 (Entera produce f6).

- **Rj / Rk** (bandera operando listo): **SI** = el operando ya se puede leer (la UF productora terminó y escribió, o ya estaba en registro). **NO** = aún no listo.
  - Al emitir: Rj/Rk = NO si Qj/Qk ≠ 0.
  - Cuando la UF productora completa ejecución y escribe, pone Rj/Rk = SI en todas las UF que esperaban ese resultado (broadcast por bus de resultados).
  - En ciclo 8b: `fmul.d` (UF 2) pasa a Rj=SI, Rk=SI → puede leer operandos en ciclo 9. `fsub.d` (UF 4) también pasa a Rj=SI, Rk=SI.

Estos campos implementan la **esperada de dependencias RAW (Read After Write)** sin parada global: cada UF avanza independientemente cuando sus Rj/Rk se ponen a SI.

> UF Nombre Ocupada Op Fi Fj Fk Qj Qk Rj Rk 1 Entera SI Carga f6 x2 NO 2 Mult1 SI Mult f0 f2 f4 1 NO SI
> — `repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf` (cita sin comprobar)

Relacionado: [[estructura-del-marcador-scoreboard-en-arquitectura-de-comput]] · [[deteccion-de-riesgos-war-y-waw-en-marcador-y-bloqueo-de-escr]] · [[semantica-de-los-campos-qj-qk-rj-rk-en-el-estado-de-uf]] · [[marcador-scoreboard-distingue-riesgos-raw-y-war-con-detencio]]
