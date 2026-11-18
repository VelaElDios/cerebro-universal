---
tipo: "dato"
titulo: "Parámetros del procesador superescalar en problema de planificación de bucle (examen AC 2017/18)"
temas: ["ac", "pipeline", "planificacion", "superescalar"]
claves: ["emisión dual", "unidad funcional PF", "unidad entera latencia 0", "retardo salto ignorado"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2018.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]] · [[planificacion]] · [[superescalar]]

El procesador permite emitir hasta 2 instrucciones por ciclo (incluyendo 2 enteras). Dispone de una unidad de suma PF y una de multiplicación PF, ambas totalmente segmentadas (pipelined). Dos unidades enteras con latencia 0 (resultado disponible en mismo ciclo). El retardo de la instrucción de salto (BEQZ) se ignora (se asume predicción perfecta o penalidad 0).

> Se ejecuta el siguiente bucle en un procesador superescalar que puede emitir dos operaciones independientes por ciclo (incluidas dos operaciones enteras). [...] 1 unidad funcional totalmente segmentada para cada tipo de operación en punto flotante (suma PF, multiplicación PF) • 2 unidades funcionales enteras con latencia 0 • Se ignora el retardo del salto
> — `repo:datos/temarios/AC/examenes/Junio2018.pdf` (cita sin comprobar)

Relacionado: [[analisis-de-dependencias-en-bucle-con-add-d-y-s-d-misma-iter]] · [[antidependencia-entre-iteraciones-en-bucle-con-store-y-actua]]
