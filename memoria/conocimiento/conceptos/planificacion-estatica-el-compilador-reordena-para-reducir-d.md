---
tipo: "concepto"
titulo: "Planificación estática: el compilador reordena para reducir dependencias"
temas: ["ac", "compilador", "estatica", "planificacion", "pipeline", "planificacion-estatica"]
claves: ["planificación estática", "compilador", "reordenación", "dependencias"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2026.pdf", "repo:datos/temarios/AC/examenes/Junio2018.pdf", "repo:datos/temarios/AC/examenes/Junio2025.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[compilador]] · [[estatica]] · [[planificacion]]

En planificación estática (compilador), se reordenan instrucciones en tiempo de compilación para minimizar paradas por dependencias (rellenando slots de delay, desenrollando bucles, etc.). En planificación dinámica (hardware, superescalar, Tomasulo) el procesador reordena en tiempo de ejecución.

> En la planificación estática... c. El compilador reordena el código para reducir las dependencias
> — `repo:datos/temarios/AC/examenes/Enero2026.pdf` (cita sin comprobar)

## Ampliación (2026-11-18, )
La planificación estática (static scheduling) es realizada por el compilador en tiempo de compilación. El compilador reordena las instrucciones para minimizar detenciones por dependencias y riesgos, aprovechando el conocimiento del pipeline. El hardware ejecuta el código en el orden dado. Respuesta correcta: c) El compilador reordena el código para reducir las dependencias.

## Ampliación (2026-11-18, )
La planificación estática (static scheduling) es realizada por el compilador en tiempo de compilación: reordena instrucciones para minimizar paradas (stalls) por dependencias y riesgos, aprovechando el conocimiento del pipeline. La opción correcta es c.
