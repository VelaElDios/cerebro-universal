---
tipo: "concepto"
titulo: "Tres mecanismos de especulación evaluados en examen AC Enero 2014"
temas: ["ac", "arquitectura", "prediccion-saltos"]
claves: ["sin especulación", "cooperación hardware/software", "poison bits", "especulación estática"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2014.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[arquitectura]] · [[prediccion-saltos]]

El problema evalúa tres enfoques: (a) Procesador sin ayuda para especulación: las instrucciones especulativas se ejecutan normalmente y sus excepciones terminan el programa. (b) Cooperación HW/SW sin distinción: la rutina de excepción siempre devuelve valor indefinido y no termina el programa, tratando igual instrucciones normales y especulativas. (c) Poison bits: las instrucciones especulativas que fallan marcan el registro destino con poison bit (valor "sucio"), propagándose a instrucciones dependientes; solo si una instrucción no especulativa usa un valor sucio se lanza excepción real.

> a) Un procesador sin ayuda para la especulación. b) Mecanismo de cooperación hardware/software sin distinción entre instrucciones normales e instrucciones especulativas. c) Especulación con poison bits.
> — `repo:datos/temarios/AC/examenes/Enero2014.pdf` (cita sin comprobar)
