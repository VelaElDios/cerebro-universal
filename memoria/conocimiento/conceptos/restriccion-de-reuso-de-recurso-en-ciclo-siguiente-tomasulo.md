---
tipo: "concepto"
titulo: "Restricción de reuso de recurso en ciclo siguiente (Tomasulo examen)"
temas: ["ac", "hazard", "resource", "tomasulo"]
claves: ["resource reuse", "next cycle", "reservation station", "load buffer"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2017.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[hazard]] · [[resource]] · [[tomasulo]]

Regla adicional del enunciado: cuando una estación de reserva o buffer de carga/almacenamiento queda libre al terminar una instrucción (tras escritura de resultado), no puede ser asignado a una nueva instrucción en el mismo ciclo; la asignación (Emisión) solo puede ocurrir en el ciclo siguiente. Esto modela un realismo de control de asignación y evita colisiones de puerto de escritura en la tabla de estado.

> Un recurso que es liberado en un ciclo de reloj no puede ser usado hasta el siguiente ciclo.
> — `repo:datos/temarios/AC/examenes/Enero2017.pdf`

Relacionado: [[buffers-de-carga-y-almacenamiento-en-tomasulo]] · [[diferencia-entre-buffers-de-carga-y-de-almacenamiento-en-la]] · [[convencion-de-nomenclatura-en-tablas-de-tomasulo-del-temario]]
