---
tipo: "receta"
titulo: "Cómo se traza la ejecución ciclo a ciclo en el algoritmo de Tomasulo"
temas: ["ac", "pipeline", "simulacion", "tomasulo"]
claves: ["Tomasulo", "estado instrucciones", "estaciones reserva", "buffers carga", "Qi", "escritura resultado"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[pipeline]] · [[simulacion]] · [[tomasulo]]

Para simular Tomasulo ciclo a ciclo se mantienen tres tablas sincronizadas:
1. **Estado de las instrucciones**: para cada instrucción se anota ciclo de emisión, rango de ejecución y ciclo de escritura de resultado.
2. **Estaciones de reserva** (Reservation Stations): por cada unidad funcional (buffers de carga, sumadores, multiplicadores/divisores) se registra: Ocupada (SI/NO), Operación (Op), operandos disponibles (Vj, Vk) o pendientes (Qj, Qk).
3. **Estado de los registros** (Register Status): por cada registro flotante (f0, f2, f4, f6, f8, f10, f12) se guarda Qi = estación de reserva que producirá su valor (o vacío si ya está disponible).

Pasos de la traza:
- En emisión: se asigna estación de reserva libre, se copian operandos disponibles (V) o se anotan dependencias (Q).
- En ejecución: la unidad funcional opera cuando sus Qj/Qk se resuelven (broadcast por CDB).
- En escritura: el resultado viaja por el CDB, actualiza V en estaciones que esperaban ese Q y limpia Qi del registro destino.
El ejemplo muestra ciclos 14, 15, 16, 55, 56, 57 de una secuencia con fld, fmul.d, fsub.d, fdiv.d, fadd.d, evidenciando cómo la división (fdiv.d) ocupa Mult 2 durante muchos ciclos (17-56) y cómo fadd.d escribe en ciclo 11 mientras fmul.d escribe en 16.

> Estado de las instrucciones ciclo 14 Instrucción Emisión Ejecución Escritura resultado fld f6, 34(x2) 1 2-3 4
> — `repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf`

Relacionado: [[algoritmo-tomasulo-origen-y-objetivo-cpi1]] · [[buffers-de-carga-y-almacenamiento-en-tomasulo]]
