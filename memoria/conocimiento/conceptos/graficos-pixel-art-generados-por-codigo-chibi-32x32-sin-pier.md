---
tipo: "concepto"
titulo: "Gráficos pixel art generados por código (chibi 32x32 sin piernas, rasgos propios, equipaciones y selecciones)"
temas: ["canvas", "juego", "pixel art", "sprites"]
claves: ["chibi", "32x32", "sin piernas", "rasgos", "equipaciones", "selecciones", "renderizado por capas"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/docs/arquitectura.md"]
confianza: "verificado"
fecha: "2026-11-22"
actualizado: "2026-11-22"
---

Temas: [[canvas]] · [[juego]] · [[pixel art]] · [[sprites]]

Los sprites se generan procedimentalmente en sprites.js. Cada jugador, entrenador y jefe tiene rasgos únicos. El mapa (Fase 7) se pinta con píxeles de 2 unidades en render-suelo.js y render-obstaculos.js, con paletas por ambiente en render-paletas.js. Efectos de habilidades en render-habilidades.js con partículas limitadas y azar propio en efectos.js.
relacionado: Rendimiento del juego: búsqueda espacial por celdas, texturas cacheadas, Fase 7: muñecos chibi, mapa nuevo, menú y habilidades

> Los muñecos se pintan con código en una cuadrícula de 32×32 en estilo chibi (16×20 con piernas hasta la Fase 6): cabeza grande, cuerpo y zapatones, sin piernas. Se pintan por capas y píxel a píxel: zapatos, pantalón, torso, brazos y cabeza, cada una con su contorno de color y luz desde arriba a la izquierda. Cada persona tiene sus rasgos (18 peinados, 6 tipos de barba, mandíbula, complexión, estatura, gesto, gafas, cinta, guantes, brazalete…) y caminan con 4 fotogramas. Así se generan las equipaciones y las camisetas de 26 selecciones sin imágenes.
> — `repo:saas/docs/arquitectura.md`

Relacionado: [[renderizado-de-sprites-chibi-3232-por-capas-y-pixel-a-pixel]] · [[renderizado-chibi-1620-px-por-codigo-con-cache-de-fotogramas]] · [[arquitectura-del-juego-simulacion-determinista-presentacion]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
