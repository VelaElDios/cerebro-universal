---
tipo: "dato"
titulo: "Cronograma de emisión, ejecución y escritura por instrucción en ciclos 1-8"
temas: ["ac", "cronograma", "pipeline", "tomasulo"]
claves: ["emision", "ejecucion", "escritura resultado", "ciclos"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[cronograma]] · [[pipeline]] · [[tomasulo]]

Tabla «Estado de las instrucciones» (ciclos 2-8):
- Iteración 1:
  * fld #1: Emisión=1, Ejecución=2-3 (latencia carga=2 ciclos), Escritura=4
  * fmul.d #1: Emisión=2, Ejecución=3-5 (latencia multiplicación=3 ciclos), Escritura=6
  * fsd #1: Emisión=3, Ejecución=4-7 (espera dato Mult 1), Escritura=8
- Iteración 2:
  * fld #2: Emisión=6, Ejecución=7-8, Escritura=9 (fuera del trozo)
  * fmul.d #2: Emisión=7, Ejecución=8-10, Escritura=11
  * fsd #2: Emisión=8, Ejecución=9-12, Escritura=13
La emisión es in-order (1,2,3,6,7,8); la ejecución y escritura son out-of-order según disponibilidad de operandos y unidades.

> Instrucción                 Emisión           Ejecución   Escritura resultado                           fld       f0, 0(x1)                        1                           fmul.d    f4, f0, f2                       2                           fsd       f4, 0(x1)                        3
> — `repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf`

Relacionado: [[secuencia-de-instrucciones-y-dependencias-en-el-ejemplo-toma]] · [[orden-de-emision-en-orden-in-order-issue-con-ejecucion-fuera]] · [[secuencia-exacta-de-ciclos-para-cada-instruccion-en-la-simul]] · [[secuencia-de-instrucciones-y-latencias-en-ejemplo-tomasulo-c]]
