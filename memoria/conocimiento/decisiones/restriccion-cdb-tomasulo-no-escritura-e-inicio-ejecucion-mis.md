---
tipo: "decision"
titulo: "Restricción CDB Tomasulo: no escritura e inicio ejecución mismo ciclo"
temas: ["ac", "cdb", "tomasulo"]
claves: ["Bus Datos Común", "mismo ciclo", "escritura", "inicio ejecución", "espera dato"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Diciembre2010.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[cdb]] · [[tomasulo]]

Decisión de modelado en el enunciado: el Common Data Bus (CDB) no permite broadcast y captura simultánea en el mismo ciclo. Si una instrucción escribe resultado en CDB en ciclo T, una instrucción esperando ese operando no puede comenzar ejecución hasta ciclo T+1. Esto añade 1 ciclo de latencia efectiva en dependencias RAW vía CDB frente a modelo ideal.

> se supone que en el mismo ciclo de reloj no se puede escribir un dato en este bus e iniciar la ejecución de una operación que estuviera esperando ese dato
> — `repo:datos/temarios/AC/examenes/Diciembre2010.pdf`

Relacionado: [[escritura-de-resultado-y-actualizacion-de-qi-en-registro-des]] · [[restriccion-de-cdb-en-tomasulo-no-escritura-e-inicio-simulta]] · [[restriccion-cdb-mismo-ciclo-en-tomasulo-no-iniciar-ejecucion]] · [[restriccion-de-forwarding-por-cdb-en-tomasulo-no-escritura-e]]
