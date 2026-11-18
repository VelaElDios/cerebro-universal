---
tipo: "concepto"
titulo: "Riesgos estructurales en marcador (scoreboard): fase de emisión si no hay estación de reserva libre"
temas: ["ac"]
claves: ["scoreboard", "marcador", "riesgo estructural", "estación de reserva", "emisión"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2017.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]]

En scoreboard (marcador), las estaciones de reserva son por unidad funcional. Un riesgo estructural en emisión ocurre si la instrucción no puede obtener una estación de reserva libre (todas ocupadas). La lectura de operandos espera disponibilidad (riesgo de datos, no estructural). La escritura espera bus común (riesgo estructural de bus, pero la opción clásica es emisión). Respuesta correcta: a).

> En marcador se pueden producir riesgos estructurales: a) En la fase de emisión, si no hay espacio en la estación de reserva b) En la fase de lectura de operandos, si no está disponible alguno de los operandos c) En la fase de escritura, si no está libre el bus común de datos d) Ninguna es correcta
> — `repo:datos/temarios/AC/examenes/Enero2017.pdf`

Relacionado: [[comparativa-tomasulo-vs-marcador-scoreboard]] · [[buffers-de-carga-y-almacenamiento-en-tomasulo]] · [[scoreboard-riesgos-estructurales-en-paso-de-escritura-de-res]] · [[scoreboard-los-riesgos-estructurales-se-gestionan-en-la-etap]] · [[riesgo-estructural-en-scoreboard-pregunta-7]]
