---
tipo: "receta"
titulo: "Estado inicial (ciclo 1) de un bucle vector-escalar en Tomasulo"
temas: ["ac", "bucle", "escalar", "tomasulo", "vector"]
claves: ["fld f0 0(x1)", "fmul.d f4 f0 f2", "fsd f4 0(x1)", "addi", "bne", "Carga 1 SI 80"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[bucle]] · [[escalar]] · [[tomasulo]] · [[vector]]

Configuración inicial del ejemplo de bucle (páginas 113-114):
**Código:**
```
start: addi x1, x0, x        ; x1 = dirección x[n]
       fld  f2, k(x0)        ; f2 = k (escalar)
loop: fld  f0, 0(x1)         ; carga elemento vector
      fmul.d f4, f0, f2      ; multiplica por escalar
      fsd  f4, 0(x1)         ; almacena resultado
      addi x1, x1, -8        ; decrementa puntero
      bne  x1, x0, loop      ; salta si x1 != 0
```
**Estado ciclo 1 (tras emitir primera fld):**
- **Buffers de carga/almacenamiento**: Carga 1 = Ocupada SI, Dirección 80 (dirección efectiva 0(x1)=80); Carga 2/3, Almac 1/2/3 = NO.
- **Estaciones de reserva**: Todas libres (Suma 1/2/3, Mult 1/2 = NO).
- **Registros**: Qi vacíos (no hay dependencias pendientes aún).
- **Instrucciones emitidas**: solo la primera fld (ciclo 1). Las siguientes (fmul.d, fsd, segunda fld, etc.) esperan emisión en ciclos posteriores.
Este estado sirve de punto de partida para trazar el desenrollado del bucle y ver cómo Tomasulo solapa iteraciones mediante renombrado de registros (f0, f4 se reutilizan) y buffers de carga/almacenamiento separados.

> ciclo 1 Instrucción Emisión Ejecución Escritura resultado fld f0, 0(x1) 1 fmul.d f4, f0, f2 fsd f4, 0(x1)
> — `repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf`

Relacionado: [[como-se-traza-la-ejecucion-ciclo-a-ciclo-en-el-algoritmo-de]] · [[latencias-de-cache-asumidas-en-el-ejemplo-de-bucle-vector-es]]
