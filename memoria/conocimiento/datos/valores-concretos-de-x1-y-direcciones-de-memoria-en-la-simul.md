---
tipo: "dato"
titulo: "Valores concretos de x1 y direcciones de memoria en la simulación"
temas: ["ac", "array", "direccionamiento", "double", "tomasulo"]
claves: ["x1", "72", "64", "80", "stride", "puntero base"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[array]] · [[direccionamiento]] · [[double]] · [[tomasulo]]

Valores observados del registro base x1 y direcciones efectivas:
- Ciclo 9: x1 = 72. Buffers Carga 1 y Almac 1 en dirección 80 (72+8?); Carga 2 y Almac 2 en 72 (72+0). Posible offset 8 en primera iteración o x1 ya pre-decrementado.
- Ciclos 10-15: x1 = 64 fijo. Buffers Carga 3 y Almac 3 en dirección 64.
El patrón sugiere recorrido inverso de array: dirección = x1 + 0, con x1 decrementando 8 bytes por iteración. La primera iteración usa dirección 80 (quizá x1 inicial 80, pre-decremento a 72 antes de ciclo 9).

> x1 = 72 ... x1 = 64
> — `repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf` (cita sin comprobar)

Relacionado: [[buffers-de-carga-y-almacenamiento-en-tomasulo]]
