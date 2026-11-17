---
tipo: "concepto"
titulo: "Predictor correlacionado o de dos niveles (m,n): correlación espacial e historia global"
temas: ["ac", "arquitectura-computadores", "correlacion-dos-niveles", "prediccion-saltos"]
claves: ["predictor correlacionado", "dos niveles", "correlación espacial", "predictor (m", "n)", "historia global", "BHR", "BHT"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[arquitectura-computadores]] · [[correlacion-dos-niveles]] · [[prediccion-saltos]]

Los predictores correlacionados explotan la correlación espacial: el comportamiento de saltos recientes influye en el salto actual. Un predictor (m,n) usa m bits de historia global (últimos m saltos) para seleccionar una de 2^m tablas BHT, cada una con predictores de n bits indexados por la dirección del salto actual. Esto permite patrones como "si el salto anterior fue tomado, este salto se comporta de tal forma".

> Predictor correlacionado o de dos niveles • Los saltos están relacionados • Correlación espacial: El comportamiento de los últimos saltos afecta a la predicción actual • Generalización: predictor (m,n)  Usa información de m saltos  Comportamiento de los últimos m saltos para elegir entre 2m predictores de saltos, cada uno de los cuales es un predictor n-bit predictor para un solo salto • Predicción basada en historia global • Pentium II 1997
> — `repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4.pdf` (cita sin comprobar)
