---
tipo: "receta"
titulo: "Renombrado de registros para eliminar dependencias de nombre (estático y dinámico)"
temas: ["ac", "hardware-dinamico", "optimizacion-compilador", "paralelismo-instruccion", "renombrado-registros"]
claves: ["renombrado-registros", "renombrado-estatico", "renombrado-dinamico", "dependencia-nombre", "WAR", "WAW"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema2-Paralelismo a nivel de instruccion/Tema2-2026-2027.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[hardware-dinamico]] · [[optimizacion-compilador]] · [[paralelismo-instruccion]] · [[renombrado-registros]]

Para romper dependencias de nombre (antidependencias WAR y dependencias de salida WAW), se asignan registros físicos distintos a cada escritura lógica. En el ejemplo, el bucle original reusa f0 y f4; la versión renombrada usa f0/f4 en la primera iteración y f6/f8 en la segunda, permitiendo solapamiento sin riesgos. El compilador puede hacerlo estáticamente (asignación de registros, desenrollado) o el hardware dinámicamente (registro de renombrado, ROB, estación de reserva).

> Se trata de escribir sobre registros o posiciones distintas a las que se usan para leer. Puede conseguirse estática (compilador) o dinámicamente (hardware)
> — `repo:datos/temarios/AC/Tema2-Paralelismo a nivel de instruccion/Tema2-2026-2027.pdf` (cita sin comprobar)
