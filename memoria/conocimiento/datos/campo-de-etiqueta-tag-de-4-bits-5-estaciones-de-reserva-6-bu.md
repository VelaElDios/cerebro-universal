---
tipo: "dato"
titulo: "Campo de etiqueta (tag) de 4 bits: 5 estaciones de reserva + 6 buffers de carga"
temas: ["ac", "arquitectura", "etiquetas", "planificacion-dinamica", "tomasulo"]
claves: ["tag 4 bits", "5 estaciones reserva", "6 buffers carga", "operando disponible"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[arquitectura]] · [[etiquetas]] · [[planificacion-dinamica]] · [[tomasulo]]

El tag tiene 4 bits (16 combinaciones). Se asignan: 5 códigos para las 5 estaciones de reserva (Entera, Mult1, Mult2, Suma, Divide) y 6 códigos para los 6 buffers de carga. Los códigos restantes marcan «operando ya disponible» (valor presente en la propia estación/buffer). Esto permite a cualquier consumidor saber qué productor debe vigilar en el CDB.

> Campo de etiqueta: cantidad de 4 bits que indica una de las 5 estaciones de reserva o uno de los 6 buffers de carga; indica la estación de reserva o buffer de carga cuya UF asociada producirá un resultado como un operando fuente; valores de etiqueta no usados indican que el operando ya está disponible
> — `repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf` (cita sin comprobar)

Relacionado: [[contenido-de-una-estacion-de-reserva-en-tomasulo]] · [[estaciones-de-reserva-almacenan-etiquetas-para-control-de-ri]] · [[estructura-del-procesador-tomasulo-cdb-estaciones-de-reserva]]
