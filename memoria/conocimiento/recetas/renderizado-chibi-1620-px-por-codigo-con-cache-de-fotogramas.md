---
tipo: "receta"
titulo: "Renderizado chibi 16×20 px por código con caché de fotogramas"
temas: ["donetonic", "grada-colchonera", "graficos", "pixel-art", "rendimiento", "scrum"]
claves: ["chibi", "16x20", "frame cache", "canvas", "P22", "P45"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/docs/gestion/README.md"]
confianza: "verificado"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[donetonic]] · [[grada-colchonera]] · [[graficos]] · [[pixel-art]] · [[rendimiento]] · [[scrum]]

- Cada muñeco (jugador, rival, jefe) se dibuja en un canvas off-screen de 16×20 px usando primitivas (rect, arc, fill) — cero assets de imagen.
- Se generan y cachean todos los fotogramas de animación (idle, run, attack, hit, death) al cargar el juego o al desbloquear el personaje.
- En runtime solo se hace drawImage del fotograma cacheado → coste de draw call mínimo.
- Detalles añadidos en P45: sombreado, orejas, nariz, peinados, brazalete de capitán, cinta, pecas, barba, pendientes, tatuajes.
- Respeta prefers-reduced-motion: se desactivan sacudidas y partículas.

> Muñecos de 16×20 píxeles dibujados con código (sin imágenes), con caché de fotogramas.
> — `repo:saas/docs/gestion/README.md`

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
