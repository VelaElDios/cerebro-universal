---
tipo: "receta"
titulo: "Análisis de dependencias entre instrucciones de punto flotante en misma iteración"
temas: ["ac", "dependencias", "pipeline"]
claves: ["L.D", "ADD.S", "S.D", "dependencia datos", "dependencia salida"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2018.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[dependencias]] · [[pipeline]]

Entre I3 (ADD.S F5, F4, F3) e I4 (S.D F5, 0(R1)): I3 escribe en F5, I4 lee F5 para almacenar. Existe dependencia de datos (RAW) porque I4 necesita el valor que produce I3 en F5. No hay dependencia de salida (WAW) porque I4 no escribe en F5. Respuesta correcta: a) Solamente una dependencia de datos.

> En el siguiente fragmento de código, entre I3 a I4 hay (en la misma iteración): L.D F3, 0(R1) ; I1 ADD.S F4, F3, F3 ; I2 ADD.S F5, F4, F3 ; I3 S.D F5, 0(R1) ; I4
> — `repo:datos/temarios/AC/examenes/Junio2018.pdf` (cita sin comprobar)

Relacionado: [[analisis-de-dependencias-en-bucle-con-add-d-y-s-d-misma-iter]] · [[antidependencia-war-en-bucle-entre-carga-y-actualizacion-de]] · [[dependencias-en-fragmento-de-codigo-fp-mips-l-d-add-s-add-s]] · [[analisis-de-dependencias-en-codigo-fp-con-registro-f1-raw-y]] · [[tipos-de-dependencias-y-hazards-en-codigo-mips64-de-punto-fl]]
