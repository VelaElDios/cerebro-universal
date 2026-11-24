---
tipo: "decision"
titulo: "Imágenes repetidas: una sola aparición y \\ref en el resto"
temas: ["figuras", "gestion-contenido", "latex", "maquetacion", "regla 10 javier"]
claves: ["figura repetida", "ref cruzado", "DoneTonic", "produccion", "ref", "figura", "captura", "duplicado"]
proyectos: ["memoria-procesos"]
fuentes: ["memoria/reglas-tfg.md regla 10 y spec versión 4", "memoria/reglas-tfg.md"]
confianza: "propuesto"
fecha: "2026-11-22"
actualizado: "2026-11-24"
---

Temas: [[figuras]] · [[gestion-contenido]] · [[latex]] · [[maquetacion]] · [[regla 10 javier]]

**Temas**: [[figuras]] · [[gestion-contenido]] · [[latex]] · [[maquetacion]] · [[regla 10 javier]]

**Regla 10 (Javier)**: cada captura (DoneTonic, producción, prueba técnica, app, hito4, juego, fase7) se incluye **una sola vez** en el capítulo/anexo donde más sentido tiene. En los demás capítulos se cita con `\ref{fig:etiqueta}`.

**Distribución canónica (versión 4 / verificada)**:

- **Capturas DoneTonic Sprint 1** (tablero S1, gráficas S1, backlog) → solo en **cap:propuesta** (Capítulo 3)  
  Figuras: `\ref{fig:donetonic-tablero}`, `\ref{fig:donetonic-graficas-s1}`, `\ref{fig:donetonic-backlog}`.
- **Capturas DoneTonic Sprint 2** (tablero S2, gráficas S2, detalle PBI, tareas) → solo en **anx:desarrollo** (Anexo A)  
  Figuras: `\ref{fig:donetonic-s2-tablero}`, `\ref{fig:donetonic-s2-graficas}`, `\ref{fig:donetonic-s2-detalle}`.
- **Capturas producción** (correo, actions, google) → solo en **cap:evaluacion** (Capítulo 5)  
  Figuras: `\ref{fig:correo-confirmacion}`, `\ref{fig:actions-verde}`, `\ref{fig:google-publicada}`.  
  En Capítulo 4 (Descripción) se citan con `\ref{fig:actions-verde}`, etc.
- **Capturas app/ y hito4/** → solo en **cap:descripcion** (Capítulo 4, sección «La aplicación»).
- **Capturas juego/** → solo en **cap:juego** (Capítulo 4b, sección «Cómo se juega»).
- **Capturas fase7/** → solo en **cap:juego** (Capítulo 4b) si se usan, **o en anexo** si son comparativas antes/después.
- **Capturas prueba-tecnica/** → solo en **cap:evaluacion** (Capítulo 5)  
  Figura: `\ref{fig:prueba-tecnica}`.

**Verificación automática**:  
`verificar.py` comprueba mínimos por carpeta; `revisar_maquetacion.py` **no** detecta duplicados — el revisor debe confirmar visualmente en el PDF.

**Ejemplos de cita cruzada**:
- En `04-descripcion.tex`: «El despliegue en Google Cloud Run se validó… (Figura~\ref{fig:correo-confirmacion}, Capítulo~\ref{cap:evaluacion})».
- En texto: «el tablero del Sprint 1 (Figura~\ref{fig:donetonic-tablero})» en lugar de volver a incluir la imagen.

> **Sin figuras repetidas: cada imagen aparece una sola vez. Si hace falta en otro sitio, se pone \ref a la figura que ya existe.**  
> — `memoria/reglas-tfg.md` (regla 10 y spec versión 4)

**Relacionado**:  
[[imagenes-repetidas-una-sola-aparicion-y-ref-en-el-resto]] · [[imagenes-repetidas-una-sola-aparicion-y-ref-en-el-resto]] · [[cada-imagen-aparece-una-sola-vez-en-el-capitulo-canonico]] · [[una-imagen-en-un-solo-sitio-y-en-el-resto-una-referencia]]

**Origen**: [[proyectos/memoria-procesos/estado|memoria-procesos]]

> Sin figuras repetidas: cada imagen aparece una sola vez. Si hace falta en otro sitio, se pone \ref a la figura que ya existe.
> — `memoria/reglas-tfg.md regla 10 y spec versión 4` (cita sin comprobar)
> Sin figuras repetidas: cada imagen aparece una sola vez. Si hace falta en otro sitio, se pone \ref a la figura que ya existe.
> — `memoria/reglas-tfg.md`

Fusionada con: Imágenes repetidas — una sola aparición + \ref en el resto

Relacionado: [[sin-figuras-repetidas-usar-ref-a-la-figura-existente]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
