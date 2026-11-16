---
tipo: "decision"
titulo: "Cámara 3/4 con inercia, inclinación y feedback visual (destellos/aplastado)"
temas: ["camara", "donetonic", "grada-colchonera", "graficos", "scrum", "ux"]
claves: ["camera 3/4", "inertia", "tilt", "screen shake", "squash", "prefers-reduced-motion", "P22"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/docs/gestion/README.md"]
confianza: "verificado"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[camara]] · [[donetonic]] · [[grada-colchonera]] · [[graficos]] · [[scrum]] · [[ux]]

- Proyección 3/4 (isométrica suave): eje X pantalla = mundo X - mundo Y; eje Y pantalla = (mundo X + mundo Y) * 0.5 + mundo Z.
- Inercia: la cámara sigue al jugador con un suavizado (lerp) configurable, no centrado rígido.
- Inclinación (tilt) al correr: rota ligeramente la vista en la dirección del movimiento.
- Feedback de daño: flash blanco (tint) + squash vertical (scaleY < 1) durante ~100 ms.
- prefers-reduced-motion: se desactivan shake, tilt y partículas; solo queda el seguimiento suave.

> Cámara 3/4 con inercia, inclinación al correr, destellos y aplastado al recibir golpes.
> — `repo:saas/docs/gestion/README.md`

Relacionado: [[renderizado-chibi-1620-px-por-codigo-con-cache-de-fotogramas]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
