---
tipo: "dato"
titulo: "Secuencia de instrucciones para simulación Tomasulo Problema 2 Enero 2026"
temas: ["ac", "examen", "tomasulo"]
claves: ["flw f6", "32(x2)", "flw f2", "48(x3)", "fmul.s f0", "f2", "f4", "fsub.s f8", "f6", "f2", "fdiv.s f10", "f0", "f6", "fadd.s f6", "f8", "f2", "fsw f6", "64(x4)"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2026.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[examen]] · [[tomasulo]]

Las 7 instrucciones a planificar en la tabla de tiempos (emisión, ejecución, escritura resultado). Dependencias: fmul.s usa f2 (2º flw) y f4; fsub.s usa f6 (1º flw) y f2; fdiv.s usa f0 (fmul.s) y f6; fadd.s usa f8 (fsub.s) y f2; fsw usa f6 (fadd.s). fdiv.s (10c) en camino crítico. fsw espera fadd.s (2c) que espera fsub.s (2c) que espera flw (2c). Salto retardado asumido en apartado d) (no mostrado aquí).

> flw    f6,32(x2) flw    f2,48(x3) fmul.s f0,f2,f4 fsub.s f8,f6,f2 fdiv.s f10,f0,f6 fadd.s f6,f8,f2 fsw    f6,64(x4)
> — `repo:datos/temarios/AC/examenes/Enero2026.pdf`

Relacionado: [[configuracion-tomasulo-con-especulacion-para-examen-enero-20]] · [[contenido-de-una-estacion-de-reserva-en-tomasulo-test-ac-q11]]
