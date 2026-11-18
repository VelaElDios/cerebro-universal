---
tipo: "receta"
titulo: "Desenrollamiento de bucles (loop unrolling) 4x con renombrado de registros en RISC-V"
temas: ["ac", "loop-unrolling", "optimizacion-compilador", "punto-flotante", "risc-v"]
claves: ["desenrollamiento bucles", "loop unrolling", "fld", "fadd.d", "fsd", "addi", "bne", "renombrado registros", "dependencias nombre"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[loop-unrolling]] · [[optimizacion-compilador]] · [[punto-flotante]] · [[risc-v]]

**Ejemplo**: `for (i=n; i>0; i--) x[i] = x[i] + k;` (vector double, 8 bytes/elemento)

**Código original (1 iteración)**:
```
loop: fld      f0, 0(x1)      ; carga x[i]
      fadd.d   f4, f0, f2     ; f4 = x[i] + k
      fsd      f4, 0(x1)      ; almacena resultado
      addi     x1, x1, -8     ; decrementa puntero
      bne      x1, x2, loop   ; salto si x1!=x2
```

**Desenrollado 4x (4 iteraciones por vuelta)**:
```
loop: fld      f0,  0(x1)     ; iter 1
      fadd.d   f4,  f0, f2
      fsd      f4,  0(x1)
      fld      f6, -8(x1)     ; iter 2 (registro f6)
      fadd.d   f8,  f6, f2    ; registro f8
      fsd      f8, -8(x1)
      fld      f10,-16(x1)    ; iter 3 (f10)
      fadd.d   f12, f10, f2   ; f12
      fsd      f12,-16(x1)
      fld      f14,-24(x1)    ; iter 4 (f14)
      fadd.d   f16, f14, f2   ; f16
      fsd      f16,-24(x1)
      addi     x1, x1, -32    ; decrementa 4*8=32 bytes
      bne      x1, x2, loop
```
**Claves**: Requiere que iteraciones totales sean múltiplo de 4. Elimina 3 `bne` y 3 `addi` por cada 4 iteraciones. Usa registros distintos (f0,f4 → f6,f8 → f10,f12 → f14,f16) para romper dependencias de nombre (WAW/WAR) en `f0` y `f4`. Quedan detenciones por latencias de `fld`→`fadd.d` (1 ciclo), `fadd.d`→`fsd` (2 ciclos) y salto retardado.

> Desenrollamiento, 4 veces • Número de iteraciones del bucle múltiplo de 4 • Se han eliminado 3 instrucciones de salto (bne) y 3 addi • Hay que eliminar las dependencias de nombre • Renombrado de registros
> — `repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf` (cita sin comprobar)

Relacionado: [[aos-vs-soa-desperdicio-de-ancho-de-banda-en-cache]] · [[calculo-de-flops-ciclo-para-avx2-con-fma]] · [[desenrollamiento-de-bucles-4x-con-planificacion-para-elimina]] · [[desenrollamiento-de-bucle-minimo-para-eliminar-detenciones-e]] · [[desenrollado-de-bucle-4x-con-salto-retardado-para-eliminar-s]]
