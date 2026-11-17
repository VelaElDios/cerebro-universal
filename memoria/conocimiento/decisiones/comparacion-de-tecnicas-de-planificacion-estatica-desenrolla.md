---
tipo: "decision"
titulo: "Comparación de técnicas de planificación estática: desenrollamiento vs segmentación software vs planificación de trazas"
temas: ["ac", "planificacion-estatica", "tradeoffs"]
claves: ["desenrollamiento de bucles", "segmentación software", "planificación de trazas", "tamaño código", "saltos", "complejidad", "anulación"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[planificacion-estatica]] · [[tradeoffs]]

Tabla de trade-offs: Desenrollamiento crea bloques grandes ideales para planificar y elimina saltos, pero infla código. Segmentación software no requiere dependencias en el cuerpo, pero mantiene saltos y necesita prólogo/epílogo. Planificación de trazas destaca fuera de bucles (código general con if-then-else), pero añade complejidad y exige hardware/compiler para anular instrucciones especulativas en caminos no tomados.

> Desenrollamiento de bucles: Bloque básico grande para planificar; Reduce el número de saltos; Incrementa el tamaño del código. Segmentación software: Sin dependencias en el cuerpo del bucle; No reduce el número de saltos; Necesita inicio y fin especial. Planificación de trazas: Funciona bien sin bucles; Mayor complejidad; Se necesita anulación
> — `repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf` (cita sin comprobar)

Relacionado: [[segmentacion-software-software-pipelining-en-bucles-sin-depe]] · [[planificacion-de-trazas-trace-scheduling-para-condicionales]]
