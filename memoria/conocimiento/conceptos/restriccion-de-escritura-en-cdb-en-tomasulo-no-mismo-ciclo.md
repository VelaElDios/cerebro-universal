---
tipo: "concepto"
titulo: "Restricción de escritura en CDB en Tomasulo (no mismo ciclo)"
temas: ["ac", "cdb", "hazard", "tomasulo"]
claves: ["CDB", "write result", "same cycle", "Tomasulo constraint"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2017.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[cdb]] · [[hazard]] · [[tomasulo]]

En este enunciado de examen se impone explícitamente que la etapa de "Escritura resultado" (Write Result) no puede solaparse con la colocación del dato en el CDB. Si una unidad funcional termina ejecución en ciclo T y pone el dato en el bus en ese mismo ciclo, la instrucción dependiente que espera ese dato no puede iniciar su ejecución hasta el ciclo T+1. Esto añade un ciclo de burbuja efectivo frente al modelo ideal donde el forwarding es inmediato.

> La ejecución de una instrucción que está esperando un resultado no puede comenzar en el mismo ciclo en el que este resultado es escrito en el Bus Común de Datos.
> — `repo:datos/temarios/AC/examenes/Enero2017.pdf`

Relacionado: [[algoritmo-tomasulo-origen-y-objetivo-cpi1]] · [[escritura-de-resultado-y-actualizacion-de-qi-en-registro-des]] · [[buffers-de-carga-y-almacenamiento-en-tomasulo]] · [[restriccion-de-forwarding-por-cdb-en-tomasulo-no-escritura-e]] · [[restriccion-cdb-mismo-ciclo-en-tomasulo-no-iniciar-ejecucion]] · [[restriccion-de-cdb-en-tomasulo-no-escritura-e-inicio-simulta]]
