---
tipo: "dato"
titulo: "Secuencia de instrucciones para simulación Tomasulo Problema 2 Enero 2026"
temas: ["ac", "examen", "tomasulo"]
claves: ["flw f6", "32(x2)", "flw f2", "48(x3)", "fmul.s f0", "f2", "f4", "fsub.s f8", "f6", "f2", "fdiv.s f10", "f0", "f6", "fadd.s f6", "f8", "f2", "fsw f6", "64(x4)"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2026.pdf", "repo:datos/temarios/AC/examenes/Junio2015.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[examen]] · [[tomasulo]]

Las 7 instrucciones a planificar en la tabla de tiempos (emisión, ejecución, escritura resultado). Dependencias: fmul.s usa f2 (2º flw) y f4; fsub.s usa f6 (1º flw) y f2; fdiv.s usa f0 (fmul.s) y f6; fadd.s usa f8 (fsub.s) y f2; fsw usa f6 (fadd.s). fdiv.s (10c) en camino crítico. fsw espera fadd.s (2c) que espera fsub.s (2c) que espera flw (2c). Salto retardado asumido en apartado d) (no mostrado aquí).

> flw    f6,32(x2) flw    f2,48(x3) fmul.s f0,f2,f4 fsub.s f8,f6,f2 fdiv.s f10,f0,f6 fadd.s f6,f8,f2 fsw    f6,64(x4)
> — `repo:datos/temarios/AC/examenes/Enero2026.pdf`

Relacionado: [[configuracion-tomasulo-con-especulacion-para-examen-enero-20]] · [[contenido-de-una-estacion-de-reserva-en-tomasulo-test-ac-q11]]

## Ampliación (2026-11-18, )
Lista exacta de 9 instrucciones a simular en orden de emisión: 1) MUL.D F4, F2, F10  2) DIV.D F2, F4, F10  3) ADD.D F10, F8, F12  4) L.D F6, 0(R1)  5) ADD.D F8, F8, F6  6) ADD.D F4, F4, F6  7) L.D F6, 0(R1)  8) ADD.D F2, F8, F0  9) MUL.D F10, F12, F20. Dependencias clave: RAW: (1->2 por F4), (1->6 por F4), (2->8 por F2), (4->5 por F6), (4->6 por F6), (7->6? no, 7 redefine F6), (7->8? no), (5->8 por F8), (3->9 por F10), (2->3 por F10? DIV.D escribe F2, ADD.D lee F10), WAW: (1 y 6 escriben F4), (4 y 7 escriben F6), (2 y 8 escriben F2), (3 y 9 escriben F10). WAR: (2 lee F4 antes de que 1 lo escriba? no, 1 escribe F4, 2 lee F4 -> RAW), (6 lee F4 antes de 1? 6 después de 1). El ROB y renombramiento en estaciones de reserva resuelven WAW/WAR.
