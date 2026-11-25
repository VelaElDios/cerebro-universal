---
tipo: "decision"
titulo: "Prosa de TFG obligatoria: nada de listas de capturas, agrupar con subfigure"
temas: ["latex", "memoria", "tfg"]
claves: ["prosa", "capturas", "subfigure", "figura X muestra", "párrafos"]
proyectos: []
fuentes: ["../../memoria/reglas-tfg.md"]
confianza: "verificado"
fecha: "2026-11-23"
actualizado: "2026-11-25"
---

Temas: [[latex]] · [[memoria]] · [[tfg]]

- Prohibido el patrón «La figura X muestra…» repetido por cada captura.
- Escribir párrafos narrativos que describan la interacción del usuario y la respuesta de la aplicación.
- Capturas relacionadas → una sola figura `figure` con varias `subfigure` (subcaption).
- Cada figura/tabla debe citarse en el texto (`\ref{fig:...}`) y explicarse; nada de relleno.
- El orden de secciones sigue la plantilla oficial.

> Prosa de TFG, no listas de capturas: nada de una frase suelta «La figura X muestra…» por cada imagen. Las capturas se explican dentro de párrafos que cuentan qué hace el usuario y por qué la aplicación responde así. Las que van juntas se agrupan con `subfigure`.
> — `../../memoria/reglas-tfg.md`

Relacionado: [[prosa-de-tfg-sin-listas-de-capturas-regla-13-javier]] · [[prosa-de-tfg-vs-lista-de-capturas]] · [[reglas-de-maquetacion-de-javier-resumen-accionable]] · [[como-escribir-prosa-de-tfg-integrando-capturas-sin-la-figura]] · [[prosa-de-tfg-en-lugar-de-listas-de-capturas-regla-13-javier]]

> ⚠️ Posible contradicción con [[como-agrupar-capturas-con-subfigure-en-latex-para-manuales-d]]: Nota B señala explícitamente que la carga del paquete `subcaption` está en `include/extra.tex` «según Nota A» y en `include/configuracion.tex` «según Nota B», contradiciéndose sobre la ubicación real. Además, Nota B describe dos estilos de referencia distintos (Opción A con sufijo de letra y Opción B con `subref` + «de la Figura»), presentándolos como provenientes de cada nota respectivamente.
