---
tipo: "concepto"
titulo: "Fichero de registros con campo Qi en Tomasulo"
temas: ["ac", "arquitectura", "tomasulo"]
claves: ["Qi", "fichero registros", "renombrado"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[arquitectura]] · [[tomasulo]]

Cada registro arquitectónico tiene un campo Qi. Qi=0 significa que el valor válido está en el propio registro; Qi≠0 apunta a la estación de reserva que está calculando el nuevo valor. Esto implementa renombrado de registros dinámico y evita dependencias WAR/WAW.

> Qi: número de la estación de reserva que contiene la instrucción que producirá el resultado Si el valor de Qi es cero, ninguna instrucción actualmente activa está calculando un resultado destinado para este registro. El valor viene dado por el contenido del registro
> — `repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf` (cita sin comprobar)

Relacionado: [[estructura-de-una-estacion-de-reserva-en-tomasulo]]
