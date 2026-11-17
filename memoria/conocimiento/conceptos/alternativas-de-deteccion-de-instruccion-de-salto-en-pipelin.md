---
tipo: "concepto"
titulo: "Alternativas de detección de instrucción de salto en pipeline"
temas: ["ac", "arquitectura", "deteccion-salto", "pipeline"]
claves: ["detección salto", "etapa IF", "etapa ID", "decodificador saltos", "buffer instrucciones", "Alpha 21064", "PowerPC 604"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[arquitectura]] · [[deteccion-salto]] · [[pipeline]]

Tres alternativas para detectar saltos en el pipeline: 1) Detección en paralelo con la decodificación (IF/ID): usa un decodificador de saltos dedicado que detecta saltos antes de terminar ID. Ejemplos: Alpha 21064, Alpha 21064A. 2) Detección después de IF: detecta saltos en el buffer de instrucciones antes de decodificar. Ejemplos: Power 1, Power 2, PowerPC 601. 3) Detección durante IF: detecta saltos mientras se leen de la caché de instrucciones. Ejemplos: PowerPC 603, PowerPC 604, PowerPC 620, R8000, PA 8000.

> Detección en paralelo con la decodificación – Usa un decodificador de saltos dedicado capaz de detectar las instrucciones de salto antes del final de la etapa ID – Detección después de la etapa IF – Detecta las instrucciones de salto en el buffer de instrucciones, antes de que sean decodificadas – Detección durante la etapa IF – Detecta las instrucciones de salto al tiempo que se leen de la cache de instrucciones
> — `repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4.pdf` (cita sin comprobar)

Relacionado: [[planteamiento-general-de-prediccion-de-saltos-con-ejecucion]]
