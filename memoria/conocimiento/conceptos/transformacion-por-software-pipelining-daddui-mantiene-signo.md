---
tipo: "concepto"
titulo: "Transformación por software pipelining: DADDUI mantiene signo de incremento"
temas: ["ac", "bucles", "planificación", "software pipelining"]
claves: ["software pipelining", "DADDUI", "incremento", "prologue", "epilogue"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2023.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[bucles]] · [[planificación]] · [[software pipelining]]

El software pipelining reordena instrucciones creando prólogo, kernel y epílogo. El incremento del contador (DADDUI) **no cambia de signo**; si el original decrementaba (#-8), el kernel también usa #-8. La opción correcta indica que el código original tiene DADDUI con #-8.

> The initial code has the DADDUI instruction with an increment of # -8.
> — `repo:datos/temarios/AC/examenes/June2023.pdf`

Relacionado: [[bucle-vectorial-de-referencia-para-desenrollado-y-planificac]] · [[planificacion-por-software-software-pipelining-y-desenrollad]] · [[calculo-de-instrucciones-tras-desenrollar-bucle-3-veces-unro]] · [[segmentacion-software-software-pipelining-para-bucle-encript]]
