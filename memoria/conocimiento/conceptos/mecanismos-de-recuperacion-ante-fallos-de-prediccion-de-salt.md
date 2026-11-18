---
tipo: "concepto"
titulo: "Mecanismos de recuperación ante fallos de predicción de saltos"
temas: ["ac", "arquitectura", "pipeline", "prediccion-saltos", "recuperacion-fallos"]
claves: ["recuperación", "fallo predicción", "keep result separate from commit", "kill instructions", "restore state"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[arquitectura]] · [[pipeline]] · [[prediccion-saltos]] · [[recuperacion-fallos]]

Tres mecanismos clave para recuperarse de un fallo de predicción (misprediction): (1) Mantener la computación de resultados separada del commit (writeback/confirmación) — resultados especulativos no se hacen arquitectónicos hasta confirmar predicción correcta. (2) Matar (flush) las instrucciones posteriores al salto que entraron en el pipeline por la vía errónea. (3) Restaurar el estado arquitectónico (registros, PC, etc.) al punto inmediatamente posterior a la instrucción de salto, para reanudar por la vía correcta.

> Mecanismos de recuperación ante fallos: Keep result computation separate from commit. Kill instructions following branch in pipeline. Restore state to that following branch
> — `repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4.pdf` (cita sin comprobar)

Relacionado: [[algoritmo-tomasulo-origen-y-objetivo-cpi1]] · [[alternativas-de-deteccion-de-instruccion-de-salto-en-pipelin]] · [[recuperacion-ante-fallo-de-prediccion-de-salto-misprediction]] · [[recuperacion-ante-fallo-de-prediccion-descartar-resultados-e]] · [[recuperacion-de-fallos-de-prediccion-con-registros-temporale]]
