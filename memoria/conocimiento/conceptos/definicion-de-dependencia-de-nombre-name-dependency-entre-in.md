---
tipo: "concepto"
titulo: "Definición de dependencia de nombre (name dependency) entre instrucciones"
temas: ["ac", "dependencias", "hazards", "pipeline"]
claves: ["name dependency", "WAW", "WAR", "antidependencia", "dependencia salida"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2025.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[dependencias]] · [[hazards]] · [[pipeline]]

La dependencia de nombre ocurre cuando dos instrucciones usan el mismo registro/posición de memoria pero no hay flujo real de datos. Incluye: WAW (ambas escriben mismo destino) y WAR (j escribe lo que i lee). Respuesta correcta: c. Answers a and b are true.

> Given two instructions i and j (j logically after i), there is a name dependency if:
> — `repo:datos/temarios/AC/examenes/June2025.pdf`

Relacionado: [[antidependencia-war-siempre-genera-hazard-war]] · [[antidependencia-entre-iteraciones-en-bucle-con-store-y-actua]] · [[definicion-de-dependencia-de-nombre-anti-y-salida]] · [[name-dependency-dependencia-de-nombre-incluye-waw-y-war]] · [[definicion-de-dependencia-de-nombre-waw-y-war]]
