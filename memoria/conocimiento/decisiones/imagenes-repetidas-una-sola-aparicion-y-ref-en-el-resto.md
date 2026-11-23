---
tipo: "decision"
titulo: "Imágenes repetidas: una sola aparición y \\ref en el resto"
temas: ["figuras", "latex", "maquetacion"]
claves: ["ref", "figura", "captura", "duplicado"]
proyectos: ["memoria-procesos"]
fuentes: ["memoria/reglas-tfg.md"]
confianza: "verificado"
fecha: "2026-11-22"
actualizado: "2026-11-23"
---

Temas: [[figuras]] · [[latex]] · [[maquetacion]]

Regla 10 de Javier: cada captura (DoneTonic, producción, prueba técnica, app, hito4, juego, fase7) se incluye **una sola vez** en el capítulo/anexo donde más sentido tiene. En los demás capítulos se cita con `\ref{fig:etiqueta}`.
- Capturas DoneTonic (tablero S1, gráficas S1, backlog) → solo en **cap:propuesta** (Figuras \ref{fig:donetonic-tablero}, \ref{fig:donetonic-graficas-s1}, \ref{fig:donetonic-backlog}).
- Capturas DoneTonic Sprint 2 (tablero S2, gráficas S2, detalle PBI, tareas) → solo en **anx:desarrollo** (Figuras \ref{fig:donetonic-s2-tablero}, \ref{fig:donetonic-s2-graficas}, \ref{fig:donetonic-s2-detalle}).
- Capturas producción (correo, actions, google) → solo en **cap:evaluacion** (Figuras \ref{fig:correo-confirmacion}, \ref{fig:actions-verde}, \ref{fig:google-publicada}).
- Capturas app/ y hito4/ → solo en **cap:descripcion** (sección "La aplicación").
- Capturas juego/ y fase7/ → solo en **cap:juego** (sección "Cómo se juega").
- Capturas prueba-tecnica/ → solo en **cap:evaluacion** (Figura \ref{fig:prueba-tecnica}).
En el texto, al referirse a ellas: "el tablero del Sprint 1 (Figura~\ref{fig:donetonic-tablero})" en lugar de volver a incluir la imagen.

> Sin figuras repetidas: cada imagen aparece una sola vez. Si hace falta en otro sitio, se pone \ref a la figura que ya existe.
> — `memoria/reglas-tfg.md`

Relacionado: [[imagenes-repetidas-una-sola-aparicion-ref-en-el-resto]] · [[cada-imagen-aparece-una-sola-vez-en-el-capitulo-canonico]] · [[una-imagen-en-un-solo-sitio-y-en-el-resto-una-referencia]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
