---
tipo: "concepto"
titulo: "Distinción entre arquitectura, organización y tecnología en procesadores"
temas: ["ac", "arquitectura"]
claves: ["arquitectura", "organización", "tecnología", "ISA", "microarquitectura"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2020.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[arquitectura]]

La arquitectura (ISA) define la interfaz programador: conjunto de instrucciones, registros, modos de direccionamiento, modelo de memoria. La organización (microarquitectura) es la implementación interna: pipeline, cachés, predictores, unidades funcionales. La tecnología es el proceso de fabricación (nm, voltaje, materiales). Dos procesadores pueden compartir arquitectura (misma ISA) pero tener distinta organización (p.ej. Intel Core i7 vs AMD Ryzen 7 ambos x86-64) o distinta tecnología (distinto nodo de fabricación). No pueden tener la misma organización y distinta arquitectura porque la organización implementa a la arquitectura.

> There are no two processors… a) With the same organization and different architecture b) With the same architecture and different organization c) With the same architecture and different technology d) None of the above
> — `repo:datos/temarios/AC/examenes/January2020.pdf`

Relacionado: [[distincion-entre-arquitectura-isa-y-organizacion-microarquit]] · [[diferencia-entre-arquitectura-y-organizacion-de-computadores]] · [[definicion-de-arquitectura-de-computadores-frente-a-organiza]]
