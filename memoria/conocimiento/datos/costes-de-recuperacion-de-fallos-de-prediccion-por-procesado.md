---
tipo: "dato"
titulo: "Costes de recuperación de fallos de predicción por procesador"
temas: ["ac", "arquitectura", "ciclos", "penalizacion", "prediccion-saltos"]
claves: ["fallo predicción", "recuperación", "ciclos", "Alpha 21264", "Pentium II", "Pentium IV", "penalidad"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[arquitectura]] · [[ciclos]] · [[penalizacion]] · [[prediccion-saltos]]

Penalidad en ciclos de reloj por fallo de predicción (misprediction penalty): Alpha 21264: 4-9 ciclos; Pentium II: 11+ ciclos; Pentium IV: >31 ciclos. El coste depende de la longitud del cauce y de la organización (etapas en las que se resuelva sentido y dirección del salto).

> En general, recuperarse de un fallo en predicción es caro – 4 a 9 ciclos en el Alpha 21264 – 11 o más ciclos en el Pentium II – Hasta más de 31 ciclos en el Pentium IV
> — `repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4.pdf` (cita sin comprobar)

Relacionado: [[planteamiento-general-de-prediccion-de-saltos-con-ejecucion]]
