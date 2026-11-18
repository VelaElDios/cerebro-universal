---
tipo: "concepto"
titulo: "Restricción de forwarding por CDB en Tomasulo: no escritura e inicio ejecución mismo ciclo"
temas: ["ac", "pipeline", "tomasulo"]
claves: ["BDC CDB forwarding mismo ciclo", "restriccion inicio ejecucion espera dato"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2014.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]] · [[tomasulo]]

Esta restricción modela la latencia real del forwarding por CDB: el dato escrito en el bus en ciclo T está disponible para iniciar ejecución en ciclo T+1. En simulación de Tomasulo, esto significa que si una instrucción escribe resultado en CDB en ciclo X, una instrucción dependiente que espera ese operando en su estación de reserva no puede comenzar su etapa de Ejecución hasta el ciclo X+1. Es equivalente a decir que el "Write Result" (escritura en CDB) y el inicio de "Ejecución" de consumidor no pueden solaparse en el mismo ciclo. Afecta al cálculo de ciclos en la tabla de la parte b).

> En el mismo ciclo de reloj no se puede escribir un dato en el Bus de Datos Común (BDC) e iniciar la ejecución de una operación que estuviera esperando ese dato
> — `repo:datos/temarios/AC/examenes/Junio2014.pdf`

Relacionado: [[algoritmo-tomasulo-los-resultados-se-difunden-por-el-bus-com]] · [[buffer-de-reordenamiento-rob-en-tomasulo-con-especulacion-ca]] · [[restriccion-cdb-mismo-ciclo-en-tomasulo-no-iniciar-ejecucion]] · [[restriccion-de-cdb-en-tomasulo-no-escritura-e-inicio-simulta]] · [[restriccion-de-escritura-en-cdb-en-tomasulo-no-mismo-ciclo]]
