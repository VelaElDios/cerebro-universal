---
tipo: "concepto"
titulo: "Segmentación software (software pipelining) en bucles sin dependencias"
temas: ["ac", "ilp", "planificacion-estatica", "risc-v"]
claves: ["segmentación software", "software pipelining", "fld", "fadd.d", "fsd", "addi", "bne", "desenrollamiento simbólico"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[ilp]] · [[planificacion-estatica]] · [[risc-v]]

La segmentación software reorganiza un bucle para solapar iteraciones como etapas de un pipeline. El ejemplo muestra un bucle que procesa un array X[1000] hacia abajo (direcciones 0xFF00 a 0xFED8) usando registros f0, f2, f4 y puntero x1. Código previo al bucle (prologue): carga f0=X[999], fadd.d f4=f0+f2, carga f0=X[998]. Cuerpo del bucle (kernel): fsd f4→M[i]; fadd.d f4=f0+f2; fld f0←M[i-2]; addi x1,x1,-8; bne x1,x0,L. Epílogo: dos fsd y un fadd.d finales. Ventaja: consume menos espacio que desenrollamiento real. Desventaja: no reduce saltos ni actualización de contadores; necesita código especial de entrada/salida.

> El nombre surge porque el procesamiento del bucle original se realiza simulando el comportamiento de una unidad segmentada, siendo las iteraciones los datos de dicha unidad segmentada
> — `repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf`

Relacionado: [[segmentacion-software-software-pipelining-para-suma-vectoria]] · [[segmentacion-software-software-pipelining-para-bucle-conteo]] · [[parametros-estandar-para-ejercicios-de-segmentacion-software]]
