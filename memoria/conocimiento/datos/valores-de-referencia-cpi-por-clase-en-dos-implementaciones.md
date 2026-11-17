---
tipo: "dato"
titulo: "Valores de referencia: CPI por clase en dos implementaciones M1/M2 (Ejercicio 2)"
temas: ["ac", "cpi", "evaluacion-rendimiento", "frecuencia-reloj", "implementaciones"]
claves: ["M1 500MHz", "M2 750MHz", "CPI clase A", "CPI clase B", "CPI clase C", "CPI clase D"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema1-Introduccion/Tema1_ProbSol.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[cpi]] · [[evaluacion-rendimiento]] · [[frecuencia-reloj]] · [[implementaciones]]

Tabla de CPI para dos implementaciones del mismo ISA:
| Clase | M1 (500 MHz) | M2 (750 MHz) |
|-------|--------------|--------------|
| A     | 1            | 2            |
| B     | 2            | 2            |
| C     | 3            | 4            |
| D     | 4            | 4            |

M1 tiene CPI mínimo 1 (clase A) → MIPS pico 500.
M2 tiene CPI mínimo 2 (clases A y B) → MIPS pico 375.
M2 tiene mayor frecuencia pero CPI peores en clases ligeras; M1 gana en pico.

> Clase A M1=1 M2=2 • Clase B M1=2 M2=2 • Clase C M1=3 M2=4 • Clase D M1=4 M2=4
> — `repo:datos/temarios/AC/Tema1-Introduccion/Tema1_ProbSol.pdf` (cita sin comprobar)
