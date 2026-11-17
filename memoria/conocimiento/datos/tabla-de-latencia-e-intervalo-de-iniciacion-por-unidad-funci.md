---
tipo: "dato"
titulo: "Tabla de latencia e intervalo de iniciación por unidad funcional en segmentación FP"
temas: ["ac", "coma-flotante", "segmentacion", "unidad-funcional"]
claves: ["ALU enteros", "memoria datos", "sumador PF", "multiplicador PF", "divisor PF", "latencia", "intervalo iniciación"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema2-Paralelismo a nivel de instruccion/Tema2-2026-2027.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[coma-flotante]] · [[segmentacion]] · [[unidad-funcional]]

Tabla de referencia rápida para diseñar o analizar pipelines de coma flotante. Cada fila muestra: unidad funcional, latencia (ciclos entre productor y consumidor) e intervalo de iniciación (ciclos mínimos entre dos emisiones del mismo tipo). Destaca que el divisor no está segmentado (iniciación 25 > latencia 24).

> ALU de enteros                                          0             1                      Memoria de datos (cargas enteras y PF)                  1             1                      Sumador PF                                              3             1                      Multiplicador PF (también de enteros)                   6             1                      Divisor PF (también de enteros y raíz cuadrada PF)     24            25
> — `repo:datos/temarios/AC/Tema2-Paralelismo a nivel de instruccion/Tema2-2026-2027.pdf`
