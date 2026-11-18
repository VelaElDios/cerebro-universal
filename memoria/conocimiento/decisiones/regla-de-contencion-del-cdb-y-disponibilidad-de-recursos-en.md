---
tipo: "decision"
titulo: "Regla de contención del CDB y disponibilidad de recursos en Tomasulo (examen June 2025)"
temas: ["ac", "tomasulo"]
claves: ["CDB", "Common Data Bus", "structural hazard", "resource availability", "cycle timing"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2025.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[tomasulo]]

Dos decisiones de diseño clave para la simulación: 1) Contención del CDB: solo una instrucción puede hacer Writing (broadcast resultado) por ciclo. Si dos instrucciones terminan Execution en el mismo ciclo, una debe esperar al ciclo siguiente (structural hazard en Writing). 2) Disponibilidad de recursos diferida: cuando una instrucción libera una estación de reserva, entrada de ROB, buffer de carga o unidad funcional en el ciclo N, ese recurso no puede ser asignado a otra instrucción hasta el ciclo N+1. Esto afecta al Issue de nuevas instrucciones y al inicio de Execution de instrucciones esperando unidad funcional.

> Any step of an instruction that wants to write to the CDB (Common Data Bus) cannot do so if another instruction is already using it. In general, any resource that is freed in one clock cycle cannot be used until the next clock cycle.
> — `repo:datos/temarios/AC/examenes/June2025.pdf` (cita sin comprobar)

Relacionado: [[bus-comun-de-datos-cdb-en-el-algoritmo-de-tomasulo]] · [[parametros-de-recursos-y-latencias-para-tomasulo-con-especul]]
