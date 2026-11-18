---
tipo: "dato"
titulo: "Registros flotantes involucrados y su estado inicial en el ejemplo"
temas: ["ac", "estado inicial", "registros", "tomasulo"]
claves: ["f0", "f2", "f4", "f6", "f8", "f10", "f12", "Qi inicial"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[estado inicial]] · [[registros]] · [[tomasulo]]

La tabla muestra 7 registros de doble precisión (f0, f2, f4, f6, f8, f10, f12). Al inicio (ciclo 2) solo f0 y f4 tienen Qi (Carga 1 y Mult 1 respectivamente); f2 no tiene Qi (valor listo, se muestra `R(f2)` en las estaciones Mult); f6, f8, f10, f12 permanecen sin Qi durante toda la traza (no se usan en este fragmento de código).

> Estado de los registros                                       f0            f2          f4            f6         f8      f10         f12
> — `repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf`

Relacionado: [[uso-de-qi-en-registros-flotantes-para-renombrado-dinamico-en]] · [[evolucion-del-registro-base-x1-y-qi-de-registros-fp-en-el-ej]] · [[renombrado-de-registros-via-qi-register-status-en-tomasulo]]
