---
tipo: "receta"
titulo: "Ejecución paso a paso de instrucciones FP en Tomasulo (ciclos 16-20)"
temas: ["ac", "planificacion-dinamica", "tomasulo"]
claves: ["fld", "fmul.d", "fsd", "buffers carga almacenamiento", "estaciones reserva", "estado registros", "Qi", "Vj", "Vk", "Qj", "Qk"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[planificacion-dinamica]] · [[tomasulo]]

El ejemplo muestra 6 instrucciones de punto flotante (2 bucles de carga-multiplicación-almacenamiento) y su progreso en ciclos 16-20.
- Instrucciones: fld f0,0(x1) | fmul.d f4,f0,f2 | fsd f4,0(x1) (repetición con solapamiento).
- Columnas: Emisión, Ejecución, Escritura resultado.
- En ciclo 16: la 1ª iteración ya escribió resultado (ciclos 10, 15); la 2ª iteración está en ejecución (fmul.d en ciclo 14-15, fsd pendiente).
- Buffers de carga: Carga 3 ocupada en dir. 64; buffers de almacenamiento: Almac 1 (dir. 80, Qi=M(80)*R()), Almac 2 (dir. 72, Qi=M(72)*R()), Almac 3 (dir. 64, Qi=Mult 1).
- Estaciones de reserva: Mult 1 ocupada (Op=Mult, Vk=R(f2), Qj=Carga 3).
- Registros: x1=64; Qi en f0=Carga 3, f4=Mult 1.
- En ciclo 17: Almac 3 pasa a ocupada con Qi=Mult 1.
- En ciclo 18: fsd #3 escribe resultado (ciclo 18); Almac 1 libera (NO).
- En ciclo 19: fsd #3 y fsd #6 escriben resultado (ciclo 19); x1 cambia a 56; Almac 1 sigue NO.
- En ciclo 20: fsd #6 escribe resultado (ciclo 20); Almac 2 queda sin Qi (solo dirección 72).

> ciclo 16                           Instrucción                Emisión           Ejecución      Escritura resultado                           fld      f0, 0(x1)                       1                9                    10                           fmul.d   f4, f0, f2                      2               14                    15
> — `repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf`

Relacionado: [[algoritmo-tomasulo-origen-y-objetivo-cpi1]] · [[buffers-de-carga-y-almacenamiento-en-tomasulo]] · [[estructura-de-una-estacion-de-reserva-en-tomasulo]] · [[estado-de-registros-resultado-register-result-status-en-el-m]] · [[ejecucion-ciclo-a-ciclo-del-ejemplo-tomasulo-fld-fmul-d-fsub]] · [[secuencia-de-instrucciones-y-dependencias-en-el-ejemplo-toma]] · [[secuencia-de-instrucciones-y-latencias-en-ejemplo-tomasulo-c]]
