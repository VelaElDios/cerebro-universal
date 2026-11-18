---
tipo: "concepto"
titulo: "Estaciones de reserva almacenan etiquetas para control de riesgos"
temas: ["ac", "estaciones de reserva", "tomasulo"]
claves: ["estaciones de reserva", "etiquetas", "control de riesgos", "Tomasulo"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2015.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[estaciones de reserva]] · [[tomasulo]]

En el algoritmo de Tomasulo, cada estación de reserva guarda la operación a realizar, los operandos (valores o etiquetas de otras estaciones que los producirán) y la etiqueta de destino. Las etiquetas permiten el control de riesgos (RAW) y la renombración implícita para evitar WAR/WAW.

> Las estaciones de reserva almacenan: a) El estado de los registros del sistema b) Etiquetas para el control de los riesgos c) El estado de una instrucción d) Ninguna es correcta
> — `repo:datos/temarios/AC/examenes/Enero2015.pdf`

Relacionado: [[contenido-de-una-estacion-de-reserva-en-tomasulo]] · [[que-es-una-estacion-de-reserva-en-el-algoritmo-de-tomasulo]] · [[informacion-almacenada-en-estaciones-de-reserva-de-tomasulo]]
