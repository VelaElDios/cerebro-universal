---
tipo: "receta"
titulo: "Renderizado de sprites chibi 32×32 por capas y píxel a píxel sin imágenes (rasgos, equipaciones, selecciones)"
temas: ["game-engine", "grada-colchonera", "graphics", "saas"]
claves: ["sprites.js", "chibi 32x32", "16x20 sin piernas", "capas: zapatos pantalón torso brazos cabeza", "contorno color", "luz superior-izquierda", "18 peinados", "6 barbas", "mandíbula", "complexión", "estatura", "gesto", "gafas", "cinta", "guantes", "brazalete", "4 frames caminata", "26 selecciones sin imágenes", "render-suelo.js 2px", "render-paletas.js", "render-habilidades.js", "efectos.js RNG propio"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/docs/documentacion-tecnica.md"]
confianza: "verificado"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[game-engine]] · [[grada-colchonera]] · [[graphics]] · [[saas]]

**Pipeline de renderizado de personajes (Fase 7):**
- **Canvas 2D** con cámara 3/4 (suelo escalado vertical, sprites erguidos).
- **Grid 32×32**: área dibujable 16×20 px (sin piernas hasta Fase 6). Estilo chibi: cabeza grande, torso, zapatones.
- **Capas píxel a píxel** (orden): 1) zapatos, 2) pantalón, 3) torso, 4) brazos, 5) cabeza. Cada capa tiene su color de contorno y luz direccional (arriba-izquierda).
- **Rasgos parametrizados** (combinados para cada jugador): 18 peinados, 6 tipos de barba, forma de mandíbula, complexión, estatura, gesto facial, gafas, cinta, guantes, brazalete de capitán…
- **Animación**: 4 frames de caminata.
- **Equipaciones y selecciones**: generadas 100% por código (colores, franjas, escudos) → 26 camisetas de selección sin usar archivos de imagen.
- **Mapa (Fase 7)**: píxeles de 2 unidades en `render-suelo.js` y `render-obstaculos.js`; paletas por ambiente en `render-paletas.js`.
- **Efectos de habilidades**: `render-habilidades.js` usa partículas con tope y RNG propio en `efectos.js` (activar/desactivar efectos no altera la simulación).

> Los muñecos se pintan con código en una cuadrícula de 32×32 en estilo chibi (16×20 con piernas hasta la Fase 6): cabeza grande, cuerpo y zapatones, sin piernas. Se pintan por capas y píxel a píxel: zapatos, pantalón, torso, brazos y cabeza, cada una con su contorno de color y luz desde arriba a la izquierda.
> — `repo:saas/docs/documentacion-tecnica.md`

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
