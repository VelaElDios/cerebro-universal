---
tipo: "receta"
titulo: "Cómo centralizar capturas duplicadas entre capítulos en LaTeX"
temas: ["figuras", "latex", "memoria"]
claves: ["ref", "label", "includegraphics", "duplicados"]
proyectos: ["memoria-procesos"]
fuentes: ["memoria-procesos"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[figuras]] · [[latex]] · [[memoria]]

Para evitar imágenes repetidas en una memoria LaTeX multi-capítulo:
1. Decidir en qué capítulo tiene más sentido cada captura (donde se explica por primera vez).
2. En ese capítulo, incluir la figura con `\includegraphics` y su `\label{fig:clave-unica}`.
3. En los demás capítulos, NO volver a incluir la imagen; usar solo `\ref{fig:clave-unica}` en el texto (ej.: "como se ve en la Figura~\ref{fig:clave-unica}").
4. Verificar que el label es único en todo el documento y que la figura está en el capítulo canónico.
5. Ejecutar `comando_prueba` que comprueba: no hay imágenes duplicadas (hash), cada figura tiene caption+label+ref, y se cumplen los mínimos por carpeta.
6. Si el test falla por referencias rotas, buscar `\ref{fig:...}` sin `\label{fig:...}` correspondiente y corregir.

> Cada imagen aparece una sola vez. Si hace falta en otro sitio, se pone \ref a la figura que ya existe." (regla 10 de memoria/reglas-tfg.md)
> — `memoria-procesos` (cita sin comprobar)

Relacionado: [[una-imagen-en-un-solo-sitio-y-en-el-resto-una-referencia]] · [[sin-figuras-repetidas-usar-ref-a-la-figura-existente]] · [[cada-imagen-aparece-una-sola-vez-en-el-capitulo-canonico]] · [[imagenes-repetidas-una-sola-aparicion-y-ref-en-el-resto]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
