---
tipo: "dato"
titulo: "Latencias VLIW 1.0 para examen Enero 2026 Problema 3"
temas: ["ac", "examen", "vliw"]
claves: ["ALU PF→ALU PF 3 ciclos", "ALU PF→fsd 3 ciclos", "fld→ALU PF 1 ciclo"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2026.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[examen]] · [[vliw]]

Tabla de latencias (stall cycles) entre productor y consumidor. ALU PF cubre fadd.d, fmul.d, fdiv.d. Significa: tras fadd.d/fmul.d, consumidor PF debe esperar 3 ciclos (slots vacíos o nops) antes de usar resultado; tras fadd.d/fmul.d, fsd espera 3 ciclos; tras fld, consumidor PF espera 1 ciclo. No hay forwarding; latencia = ciclos de hueco obligatorios. Crítico para planificar desenrollado 4× minimizando nops.

> c) Latencias del modelo actual (V1.0): Ciclos de "hueco" necesarios entre instrucción productora y consumidora. Instrucción que produce el resultado Instrucción que usa el resultado Latencia en ciclos ALU PF ALU PF 3 ALU PF fsd 3 fld ALU PF 1
> — `repo:datos/temarios/AC/examenes/Enero2026.pdf`

Relacionado: [[especificacion-vliw-1-0-para-examen-enero-2026-problema-3]]
