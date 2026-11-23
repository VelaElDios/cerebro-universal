---
tipo: "decision"
titulo: "Cita obligatoria a cada figura (incluidas subfiguras) en el texto"
temas: ["latex", "maquetacion", "referencias-cruzadas"]
claves: ["ref", "subfigure", "label", "cita"]
proyectos: ["memoria-procesos"]
fuentes: ["memoria/reglas-tfg.md (regla 10, 13)"]
confianza: "propuesto"
fecha: "2026-11-24"
actualizado: "2026-11-24"
---

Temas: [[latex]] · [[maquetacion]] · [[referencias-cruzadas]]

|
  **Regla:** Toda figura con `\label{fig:...}` debe aparecer citada en el texto con `\ref{fig:...}` o `\subref{fig:...}` al menos una vez.
  **Ejemplo correcto (cap. 04-descripcion.tex, sección Hito 4):**
  - Párrafo explica el flujo OAuth.
  - «El flujo completo, con sus dos subfiguras, se resume en la Figura~\ref{fig:sec-google}».
  - Luego: «La subfigura~\ref{fig:sec-google-redirect} muestra la redirección…» y «la subfigura~\ref{fig:sec-google-callback} muestra el intercambio…».
  **Error común:** Crear `fig:sec-google` con dos `subfigure` y solo citar las subfiguras, sin citar nunca `fig:sec-google` en el texto principal. `revisar_maquetacion.py` lo detecta como «figura no citada».
relacionado: Prosa de TFG sin listas de capturas (regla 13 Javier), Una sola portada oficial y elementos fijos de la plantilla TFG

> Cada imagen aparece una sola vez. Si hace falta en otro sitio, se pone \ref a la figura que ya existe." y "Prosa de TFG, no listas de capturas: nada de una frase suelta «La figura X muestra…» por cada imagen."
problema: El borrador tenía ~45 frases sueltas tipo «La figura X muestra…» y algunas figuras (como fig:sec-google) no se citaban en el texto principal, solo sus subfiguras.
solucion: Cada figura (incluidas las que agrupan subfiguras) debe tener al menos una `\ref` en la prosa que explica el flujo. Las subfiguras se citan con `\subref` o `\ref` dentro de la explicación.
> — `memoria/reglas-tfg.md (regla 10, 13)` (cita sin comprobar)

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
