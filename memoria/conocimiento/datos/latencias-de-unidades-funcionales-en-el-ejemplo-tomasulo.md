---
tipo: "dato"
titulo: "Latencias de unidades funcionales en el ejemplo Tomasulo"
temas: ["ac", "arquitectura", "tomasulo", "carga", "division", "latencia", "multiplicacion", "suma"]
claves: ["latencia", "carga", "multiplicacion", "division", "suma"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[arquitectura]] · [[tomasulo]]

Latencias observadas en el ejemplo: Carga (fld) = 2 ciclos de ejecución (ciclos 2-3 y 3-4) + 1 ciclo escritura = 3-4 ciclos totales. Multiplicación (fmul.d) empieza ciclo 6 y no termina en el ejemplo (latencia >1). División (fdiv.d) empieza ciclo 5, latencia larga. Suma/resta (fsub.d, fadd.d) empiezan ciclo 6. La unidad de suma/resta se usa tanto para fsub.d como fadd.d.

> fld f6, 34(x2) 1 2-3 4 fld f2, 45(x3) 2 3-4 5 fmul.d f0, f2, f4 3 6- fsub.d f8, f6, f2 4 6- fdiv.d f10, f0, f6 5 ningún bloqueo fadd.d f6, f8, f2 6
> — `repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf`

## Ampliación (2026-11-17, )
Deducido de la columna "Ocupada" (contador descendente) en ciclos 7-13:
- Carga (fld): 2 ciclos ejecución (c2-3 y c3-4) + 1 ciclo escritura = 3 ciclos totales desde emisión.
- Suma/resta (fsub.d, fadd.d): 2 ciclos ejecución (c6-7, c9-10) + 1 escritura = 3 ciclos. Suma1 libera en c8, Suma2 en c9.
- Multiplicación (fmul.d): Mult1 Ocupada=8 en c7 → 2 en c13 = 7 ciclos mostrados; emisión c3, ejecución comienza c6 → latencia ~10 ciclos totales.
- División (fdiv.d): Mult2 Ocupada=8 en c7 → 2 en c13 = 7 ciclos mostrados; emisión c5, sin inicio ejecución visible en c13 → latencia >10 ciclos (espera operandos f0 y f6).
- Buffers de carga: 3 buffers, todos libres (NO) desde c7; direcciones M(34+x2) y M(45+x3) resueltas en emisión.
