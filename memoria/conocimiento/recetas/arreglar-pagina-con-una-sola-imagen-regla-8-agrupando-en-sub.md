---
tipo: "receta"
titulo: "Arreglar «página con una sola imagen» (Regla 8) agrupando en subfigure o bajando height"
temas: ["figuras", "latex", "maquetacion", "subcaption", "tfg"]
claves: ["Regla 8", "página con solo una imagen", "height=0.42\\textheight", "subfigure", "revisar_maquetacion.py"]
proyectos: ["memoria-procesos"]
fuentes: ["memoria/reglas-tfg.md (regla 8) + salida de revisar_maquetacion.py en este proyecto"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[figuras]] · [[latex]] · [[maquetacion]] · [[subcaption]] · [[tfg]]

Cuando el script avise de una página con una sola imagen, no basta con reducir un poco el height: agrupar la captura suelta con otra cercana en una figura con subfigure (0.48\textwidth, dos por fila) o bajar a 0.30–0.32\textheight. Después, abrir el PDF en esa página y confirmar con comando_prueba.

> Ninguna página con una sola imagen: capturas como mucho a height=0.42\textheight; figuras [htbp] con los parámetros de flotantes relajados, para que compartan página con el texto u otra figura.
> — `memoria/reglas-tfg.md (regla 8) + salida de revisar_maquetacion.py en este proyecto` (cita sin comprobar)

Relacionado: [[cada-imagen-aparece-una-sola-vez-en-el-capitulo-canonico]] · [[limitar-altura-de-capturas-para-evitar-paginas-con-una-sola]] · [[como-agrupar-capturas-con-subfigure-en-latex-para-manuales-d]] · [[figuras-ninguna-pagina-con-una-sola-imagen-limites-de-altura]] · [[figuras-que-comparten-pagina-con-el-texto-parametros-de-flot]] · [[como-evitar-paginas-con-una-sola-imagen-regla-8-de-javier]] · [[figuras-sin-paginas-solas-ni-casi-vacias-limites-de-altura-y]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
