---
tipo: "dato"
titulo: "Dependencias en fragmento de código FP MIPS (L.D, ADD.S, ADD.S, S.D)"
temas: ["ac", "dependencias", "mips", "pipeline"]
claves: ["L.D", "ADD.S", "S.D", "F3", "F4", "F5", "output dependence", "data dependence"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2016.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[dependencias]] · [[mips]] · [[pipeline]]

I3: ADD.S F5, F4, F3 ; I4: S.D F5, 0(R1). Existe dependencia de datos (RAW) porque I3 escribe F5 e I4 lo lee para almacenar. No hay dependencia de salida (WAW) porque I4 no escribe F5. Respuesta: b) Only a data dependence.

> Between I3 and I4 there is... a) Only an output dependence b) Only a data dependence c) An output dependence and a data dependence d) None of the above
> — `repo:datos/temarios/AC/examenes/January2016.pdf`

Relacionado: [[tipos-de-dependencias-y-hazards-en-codigo-mips64-de-punto-fl]] · [[dependencias-en-codigo-mips64-fp-l-d-mul-s-add-s-s-d]] · [[analisis-de-dependencias-entre-instrucciones-de-punto-flotan]]
