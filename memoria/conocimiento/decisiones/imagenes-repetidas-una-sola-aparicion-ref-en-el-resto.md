---
tipo: "decision"
titulo: "Imágenes repetidas — una sola aparición + \\ref en el resto"
temas: ["figuras", "gestion-contenido", "latex", "regla 10 javier"]
claves: ["figura repetida", "ref cruzado", "DoneTonic", "produccion"]
proyectos: ["memoria-procesos"]
fuentes: ["memoria/reglas-tfg.md regla 10 y spec versión 4"]
confianza: "propuesto"
fecha: "2026-11-23"
actualizado: "2026-11-23"
---

Temas: [[figuras]] · [[gestion-contenido]] · [[latex]] · [[regla 10 javier]]

**Decisión aplicada** en versión 4:
- **Capturas DoneTonic** (8 imágenes): solo en **Capítulo 3 (Propuesta)** → fig:donetonic-tablero, fig:donetonic-graficas-s1, fig:donetonic-backlog. En Anexo A (a1-desarrollo.tex) se citan con `\ref{fig:donetonic-tablero}` etc., **no se vuelven a incluir**.
- **Capturas producción** (3 imágenes): solo en **Capítulo 5 (Evaluación)** → fig:actions-verde, fig:correo-confirmacion, fig:google-publicada. En Capítulo 4 (Descripción) se citan con `\ref{fig:actions-verde}` etc.
- **Capturas juego** (16 imágenes): solo en **Capítulo 4b (Juego)** — no aparecen en otros capítulos.
- **Capturas app/hito4** (24 imágenes): solo en **Capítulo 4 (Descripción, § La aplicación)**.
- **Capturas fase7** (12 imágenes): solo en **Capítulo 4b (Juego)** si se usan, o en anexo si son comparativas antes/después.
- **Capturas prueba-tecnica** (2 imágenes): solo en **Capítulo 5 (Evaluación)**.
**Verificación**: `verificar.py` comprueba mínimos por carpeta; `revisar_maquetacion.py` no mide duplicados — el revisor debe confirmar visualmente en PDF.
**Ejemplo de cita cruzada**: En 04-descripcion.tex final: "El despliegue en Google Cloud Run se validó... (Figura~\ref{fig:correo-confirmacion}, Capítulo~\ref{cap:evaluacion})".

> Sin figuras repetidas: cada imagen aparece una sola vez. Si hace falta en otro sitio, se pone \ref a la figura que ya existe.
> — `memoria/reglas-tfg.md regla 10 y spec versión 4` (cita sin comprobar)

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
