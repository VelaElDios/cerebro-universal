---
tipo: "receta"
titulo: "Una imagen en un solo sitio, y en el resto una referencia"
temas: ["figuras", "latex", "tfg"]
claves: ["includegraphics", "ref", "imagen repetida"]
proyectos: ["memoria-procesos"]
fuentes: ["memoria/reglas-tfg.md"]
confianza: "verificado"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[figuras]] · [[latex]] · [[tfg]]

Si una captura sirve en dos capítulos (por ejemplo, el CI en verde en la descripción y en la evaluación), se pone una sola vez, en el sitio donde más sentido tiene, y en el otro se escribe «(Figura~\ref{fig:actions-verde})». `revisar_maquetacion.py` falla si un mismo archivo aparece en dos `\includegraphics`.

> cada imagen aparece una sola vez
> — `memoria/reglas-tfg.md`

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
