---
tipo: "concepto"
titulo: "Renombrado de registros vía Qi en bucle con reuso de f0/f2/f4"
temas: ["ac", "dependencias", "registros", "renombrado", "tomasulo"]
claves: ["Qi", "f0", "f2", "f4", "renombrado dinamico", "WAR WAW"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[dependencias]] · [[registros]] · [[renombrado]] · [[tomasulo]]

El bucle reutiliza los mismos registros arquitectónicos (f0, f2, f4) en cada iteración. Tomasulo evita dependencias falsas (WAR/WAW) asignando etiquetas Qi distintas a cada instancia:
- Ciclo 9: f0 ← Qi "Carga 2" (segunda carga), f4 ← Qi "Mult 2" (segunda multiplicación).
- Ciclo 10-15: f0 ← Qi "Carga 3" (tercera carga), f4 ← Qi "Mult 2" (segunda/tercera multiplicación).
El registro f2 nunca cambia de Qi (siempre "R(f2)" en estaciones), indicando que es invariante del bucle (valor constante). El renombrado dinámico permite solapar varias iteraciones en vuelo sin colisiones de registros.

> Estado de los registros f0 f2 f4 f6 f8 f10 f12 x1 = 72 Qi Carga 2 Mult 2
> — `repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf`

Relacionado: [[algoritmo-tomasulo-origen-y-objetivo-cpi1]] · [[renombrado-de-registros-via-qi-register-status-en-tomasulo]] · [[uso-de-qi-en-registros-flotantes-para-renombrado-dinamico-en]] · [[evolucion-del-registro-base-x1-y-qi-de-registros-fp-en-el-ej]]
