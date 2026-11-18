---
tipo: "receta"
titulo: "Segmentación software (software pipelining) para bucle con mul y add (Ejercicio 4)"
temas: ["ac", "epilogue", "kernel", "planificacion-estatica", "prologue", "segmentacion-software"]
claves: ["fmul.d 4 ciclos", "fadd.d 2 ciclos", "fld/fadd/fmul/fsd/addi/slti/bne", "cuerpo modificado", "inicio y final"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3_Prob.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[epilogue]] · [[kernel]] · [[planificacion-estatica]] · [[prologue]] · [[segmentacion-software]]

La segmentación software (software pipelining) solapa iteraciones en un kernel cíclico. Para el bucle dado (carga, mul, carga, add, store, actualiza punteros, salto), se construye un diagrama de precedencias con latencias (mul 4, add 2). Se busca un Initiation Interval (II) mínimo, limitado por recurrencias (aquí la cadena mul->add->store->... no hay recurrencia en registros flotantes salvo punteros enteros). II típico = max(latencia mul, latencia add, recursos) = 4 ciclos si hay una sola UF mul. El kernel contiene instrucciones de varias iteraciones en vuelo: p.ej. en ciclo 1: fld iteración i; ciclo 2: fld iteración i+1, fmul.d iteración i; etc. El prólogo rellena la tubería (primeras iteraciones parciales), el epilogo la vacía (últimas iteraciones parciales). Registros rotados o renombrados para evitar colisiones (f2, f4, f6, f8...).

> Aplica segmentación software al siguiente código: ... a) Muestra sólo el cuerpo del bucle modificado b) Completa el código del apartado anterior con el código de inicio y el final.
> — `repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3_Prob.pdf` (cita sin comprobar)

Relacionado: [[segmentacion-software-software-pipelining-en-bucles-sin-depe]] · [[desenrollamiento-y-segmentacion-software-con-latencia-fadd-d]] · [[segmentacion-software-software-pipelining-para-bucle-encript]]
