---
tipo: "concepto"
titulo: "Generación de mundo procedural infinito con distritos, estadios y colisión por pies (vista 3/4)"
temas: ["game-engine", "grada-colchonera", "procedural-generation", "saas"]
claves: ["TERRENO", "terreno.js", "semilla", "ruido suave", "distritos (ciudad", "entrenamiento", "parque", "prado)", "estadios con gradas", "plazas", "tiendas", "mesetas", "escaleras", "barro", "lluvia", "caminos", "colisión pies 3/4"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/docs/documentacion-tecnica.md"]
confianza: "verificado"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[game-engine]] · [[grada-colchonera]] · [[procedural-generation]] · [[saas]]

El mundo se genera proceduralmente a partir de una semilla (determinista). Usa ruido suave para crear distritos temáticos: ciudad, zona de entrenamiento, parque, prado. Incluye estadios con gradas, plazas, tiendas, mesetas con escaleras, barro, lluvia y caminos. La colisión se calcula solo por los pies del personaje (vista 3/4), permitiendo que el cuerpo pase por encima de obstáculos bajos. La generación es infinita y coherente gracias a la semilla fija por partida.

> **Mundo** | Procedural e infinito por semilla, con ruidos suaves: distritos (ciudad, entrenamiento, parque, prado), estadios con gradas, plazas y tiendas, mesetas con escaleras, barro, lluvia y caminos. Colisión por los pies (vista 3/4) | `TERRENO`, `terreno.js`
> — `repo:saas/docs/documentacion-tecnica.md`

Relacionado: [[arquitectura-del-juego-simulacion-determinista-presentacion]] · [[audio-100-sintetizado-con-web-audio-ondas-pulso-triangulo-ru]] · [[frontend-spa-con-rutas-por-hash-y-vistas-cargadas-bajo-deman]] · [[optimizaciones-de-rendimiento-busqueda-por-radio-con-claves]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
