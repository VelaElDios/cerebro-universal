---
tipo: "receta"
titulo: "Cálculo de operaciones por ciclo en VLIW con software pipelining"
temas: ["ac", "software-pipelining", "throughput", "vliw"]
claves: ["operaciones por ciclo", "IPC", "VLIW", "loop scheduling", "steady state"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2017.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[software-pipelining]] · [[throughput]] · [[vliw]]

Una vez construida la tabla de planificación (schedule) para el bucle en estado estacionario (steady state), el número de operaciones por ciclo se calcula como:
  Operaciones por ciclo = (Total de instrucciones útiles ejecutadas en un periodo de iniciación) / (Longitud del periodo de iniciación en ciclos).
En VLIW con software pipelining, el periodo de iniciación (II) está limitado por:
  - Recursos: II ≥ ceil(instrucciones_tipo / unidades_tipo) para cada tipo.
  - Dependencias: II ≥ latencia / distancia en iteraciones (recurrencias).
El enunciado pide el valor numérico final tras planificar; no da la respuesta, pero la receta para obtenerla es medir el II mínimo alcanzable en la tabla y dividir instrucciones por II.

> b) ¿Cuántas operaciones por ciclo se obtienen?
> — `repo:datos/temarios/AC/examenes/Enero2017.pdf`

Relacionado: [[planificacion-vliw-de-bucle-con-6-unidades-funcionales-exame]]
