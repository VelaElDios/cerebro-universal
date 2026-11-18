---
tipo: "decision"
titulo: "Restricción de uso del CDB y liberación de recursos en Tomasulo del examen"
temas: ["ac", "tomasulo"]
claves: ["CDB", "Common Data Bus", "contención", "liberación recurso ciclo siguiente"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2025.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[tomasulo]]

Dos reglas críticas para la simulación de ciclos:
1. CDB de puerto único: solo una instrucción puede hacer Write Result por ciclo. Si dos instrucciones terminan ejecución en el mismo ciclo, una debe esperar al ciclo siguiente para usar el CDB.
2. Liberación tardía: cuando una instrucción libera una estación de reserva, entrada de load buffer, o unidad funcional en el ciclo N, ese recurso no está disponible para otra instrucción hasta el ciclo N+1. Esto afecta a la emisión (Issue) de instrucciones posteriores que necesiten ese recurso.

> Cualquier paso de una instrucción que quiera escribir en el CDB (Common Data Bus) no puede hacerlo si otra instrucción ya lo está utilizando. En general, cualquier recurso que se libera en un ciclo de reloj no puede utilizarse hasta el siguiente ciclo de reloj.
> — `repo:datos/temarios/AC/examenes/Junio2025.pdf` (cita sin comprobar)

Relacionado: [[algoritmo-tomasulo-los-resultados-se-difunden-por-el-bus-com]] · [[simulacion-tomasulo-con-especulacion-parametros-de-hardware]]
