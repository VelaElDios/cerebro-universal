---
tipo: "decision"
titulo: "Uso de la ley de Amdahl para dimensionar requisitos de uso de disco"
temas: ["ac", "rendimiento", "toma-decisiones"]
claves: ["Amdahl", "dimensionamiento", "requisito uso", "disco"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema1-Introduccion/Tema1_ProbSol.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[rendimiento]] · [[toma-decisiones]]

Se decide aplicar la ley de Amdahl (modelo clásico de aceleración parcial) para responder a la pregunta de diseño: «¿qué intensidad de uso del disco mejorado se necesita para triplicar el rendimiento global?». La decisión implica asumir que el resto del sistema no cambia y que la fracción x es constante.

> speedup = 3 = T / (xT/4 + (1-x)T) ⟹ x = 0.89 (el disco debe usarse el 89% del tiempo)
> — `repo:datos/temarios/AC/Tema1-Introduccion/Tema1_ProbSol.pdf` (cita sin comprobar)

Relacionado: [[aos-vs-soa-desperdicio-de-ancho-de-banda-en-cache]] · [[arquitectura-epic-ia64-y-procesadores-itanium]]
