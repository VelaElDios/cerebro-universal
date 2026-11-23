---
tipo: "receta"
titulo: "Una imagen en un solo sitio, y en el resto una referencia"
temas: ["figuras", "latex", "tfg", "memoria"]
claves: ["includegraphics", "ref", "imagen repetida"]
proyectos: ["memoria-procesos"]
fuentes: ["memoria/reglas-tfg.md", "../../memoria/reglas-tfg.md"]
confianza: "verificado"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[figuras]] · [[latex]] · [[tfg]]

Si una captura sirve en dos capítulos (por ejemplo, el CI en verde en la descripción y en la evaluación), se pone una sola vez, en el sitio donde más sentido tiene, y en el otro se escribe «(Figura~\ref{fig:actions-verde})». `revisar_maquetacion.py` falla si un mismo archivo aparece en dos `\includegraphics`.

> cada imagen aparece una sola vez
> — `memoria/reglas-tfg.md`

## Ampliación (2026-11-16, )
Cada imagen (figura, captura, diagrama) debe incluirse una única vez en el documento. Si se necesita referenciarla desde otro capítulo o sección, se usa una referencia cruzada `\ref{fig:etiqueta}` (o `\autoref`) en lugar de volver a insertar el archivo gráfico. Esto reduce el tamaño del PDF, evita inconsistencias y obliga a una estructura de referencias clara.

Relacionado: [[sin-figuras-repetidas-usar-ref-a-la-figura-existente]] · [[cada-imagen-aparece-una-sola-vez-en-el-capitulo-canonico]] · [[como-centralizar-capturas-duplicadas-entre-capitulos-en-late]] · [[imagenes-repetidas-una-sola-aparicion-y-ref-en-el-resto]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
