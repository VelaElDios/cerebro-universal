---
tipo: "dato"
titulo: "Valores iniciales de registros del bucle (examen enero 2016)"
temas: ["ac", "examen", "valores-iniciales", "vliw"]
claves: ["R1=0x1000", "R2=0x1500", "R10=0x3C", "60 iteraciones"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2016.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[examen]] · [[valores-iniciales]] · [[vliw]]

Valores iniciales que determinan el número de iteraciones del bucle original:
- R1 = 0x1000 (4096 decimal) = dirección base array 1
- R2 = 0x1500 (5376 decimal) = dirección base array 2
- R10 = 0x3C (60 decimal) = contador de iteraciones
El bucle se ejecuta 60 veces. Al desenrollar 4 veces, quedan 15 "macro-iteraciones" (60/4). Cada macro-iteración procesa 4 elementos (32 bytes, ya que DADDUI incrementa en 8 = double precision).

> Initially, R1=0x1000, R2=0x1500, and R10=0x3C.
> — `repo:datos/temarios/AC/examenes/January2016.pdf`

Relacionado: [[problema-de-planificacion-vliw-con-desenrollado-de-bucle-exa]]
