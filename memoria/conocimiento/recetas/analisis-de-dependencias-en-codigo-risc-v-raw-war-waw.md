---
tipo: "receta"
titulo: "Análisis de dependencias en código RISC-V (RAW, WAR, WAW)"
temas: ["ac", "dependencias", "paralelismo-instruccion", "riscv"]
claves: ["fld", "fadd.d", "fmul.d", "fdiv.d", "fsd", "addi", "bne", "RAW", "WAR", "WAW", "dependencias de datos", "antidependencias", "dependencias de salida"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema2-Paralelismo a nivel de instruccion/Tema2_Prob_RISCV_rev.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[dependencias]] · [[paralelismo-instruccion]] · [[riscv]]

Para analizar dependencias en código RISC-V:
1. Identifica cada instrucción y sus operandos origen/destino (registros y memoria).
2. Dependencia de datos (RAW): una instrucción lee un registro/memoria que otra escribe antes. Ej: i1 `fld f0,0(x1)` → i2 `fadd.d f4,f0,f2` (f0).
3. Antidependencia (WAR): una instrucción escribe un registro/memoria que otra lee antes. Ej: i2 `fadd.d f4,f0,f2` escribe f4; i3 `fadd.d f6,f0,f4` lee f4 → no es WAR, es RAW. Busca caso inverso: i3 escribe f6, i6 `fmul.d f6,f12,f2` escribe f6 → WAW. Si i4 `fld f2,0(x3)` escribe f2 e i6 lee f2 → RAW. Si i6 escribiera f2 e i4 leyera f2 → WAR.
4. Dependencia de salida (WAW): dos instrucciones escriben el mismo registro/memoria. Ej: i3 `fadd.d f6,f0,f4` e i6 `fmul.d f6,f12,f2` ambas escriben f6.
5. Para memoria: usa direcciones efectivas. `fld f2,0(x3)` (i4) y `fld f2,0(x3)` (i7) tras `addi x3,x3,-8` (i5) acceden a direcciones distintas → no hay dependencia de memoria entre ellas.

> Indica todas las dependencias de datos, antidependencias y dependencias de salida que hay en el siguiente código:
> — `repo:datos/temarios/AC/Tema2-Paralelismo a nivel de instruccion/Tema2_Prob_RISCV_rev.pdf`

Relacionado: [[dependencias-en-bucles-risc-v-clasificacion-intra-iteracion]] · [[identificacion-de-dependencias-loop-carried-en-bucles-c-styl]] · [[tipos-de-dependencias-en-codigo-fp-mips64-para-tomasulo-raw]]
