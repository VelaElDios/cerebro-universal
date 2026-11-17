---
tipo: "receta"
titulo: "Cálculo de speedup y porcentaje de mejora entre dos máquinas"
temas: ["ac", "comparacion-rendimiento", "rendimiento", "speedup"]
claves: ["speedup", "aceleración", "n veces más rápido", "porcentaje más rápido"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema1-Introduccion/Tema1 2026-27.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[comparacion-rendimiento]] · [[rendimiento]] · [[speedup]]

**Speedup (aceleración)** = Rendimiento_con_mejora / Rendimiento_sin_mejora = Tiempo_sin_mejora / Tiempo_con_mejora.
Para comparar dos máquinas A y B ejecutando el mismo programa:
- n = Tiempo_B / Tiempo_A  (veces que A es más rápida que B).
- Porcentaje de mejora f = (n - 1) × 100 %.
Ejemplo del texto: A = 10 s, B = 15 s → n = 15/10 = 1.5 → A es 1.5× más rápida (50 % más rápida).

> “X es n veces más rápida que Y”: RendimientoX / RendimientoY = n ... 𝑓 = (𝑛 − 1)𝑥100  “X es un f % más rápida que Y”
> — `repo:datos/temarios/AC/Tema1-Introduccion/Tema1 2026-27.pdf` (cita sin comprobar)

Relacionado: [[definicion-de-speedup-como-razon-de-tiempos-de-ejecucion]]
