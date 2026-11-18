---
tipo: "dato"
titulo: "Predictor correlacionado (2,1): BHR tras dos saltos tomados desde 00 es 11"
temas: ["ac", "prediccion-saltos"]
claves: ["predictor correlacionado", "BHR", "Branch History Register", "historia"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2016.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[prediccion-saltos]]

Un predictor correlacionado (m,n) usa m bits de historia global (BHR) y n bits de historia local. Aquí (2,1): BHR de 2 bits. Inicialmente 00. Cada salto tomado añade 1 por la derecha (shift left + OR). Tras dos tomados: 00 → 01 → 11.

> En un predictor correlacionado (2,1), indica el valor del BHR sabiendo que inicialmente vale 00 y que los dos últimos saltos ejecutados han sido tomados: b) 11
> — `repo:datos/temarios/AC/examenes/Junio2016.pdf` (cita sin comprobar)

Relacionado: [[bht-en-predictor-dinamico-de-3-bits-contadores-de-saturacion]]
