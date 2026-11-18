---
tipo: "concepto"
titulo: "Tipos de dependencias y hazards en código MIPS64 de punto flotante (pregunta 6)"
temas: ["ac", "dependencias", "hazards", "mips64", "pipeline", "punto-flotante"]
claves: ["L.D", "ADD.S", "S.D", "dependencia de datos", "dependencia de salida", "WAW", "RAW", "WAR"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2021.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[dependencias]] · [[hazards]] · [[mips64]] · [[pipeline]] · [[punto-flotante]]

I3: ADD.S F5, F4, F3 (escribe F5). I4: S.D F5, 0(R1) (lee F5). Hay dependencia de datos (RAW) de I3 a I4 por F5. No hay dependencia de salida (WAW) porque I4 no escribe en F5. No hay antidependencia (WAR) porque I4 no escribe en un registro que I3 lea. Respuesta correcta: a) Only a data dependence.

> In the next code fragment, between I3 and I4 (in the same iteration) there is: L.D F3, 0(R1) ; I1 ADD.S F4, F3, F3 ; I2 ADD.S F5, F4, F3 ; I3 S.D F5, 0(R1) ; I4
> — `repo:datos/temarios/AC/examenes/June2021.pdf`

Relacionado: [[dependencias-en-fragmento-de-codigo-fp-mips-l-d-add-s-add-s]] · [[tipos-de-dependencias-en-codigo-fp-mips64-para-tomasulo-raw]] · [[analisis-de-dependencias-entre-instrucciones-de-punto-flotan]]
