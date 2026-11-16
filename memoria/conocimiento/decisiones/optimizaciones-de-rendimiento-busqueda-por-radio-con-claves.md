---
tipo: "decision"
titulo: "Optimizaciones de rendimiento: búsqueda por radio con claves numéricas y una textura por celda y fotograma"
temas: ["grada-colchonera", "juego", "rendimiento", "saas"]
claves: ["colisión", "claves numéricas", "texturas", "fotograma", "4", "5 veces más rápida"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/docs/documentacion-tecnica.md"]
confianza: "propuesto"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[grada-colchonera]] · [[juego]] · [[rendimiento]] · [[saas]]

Dos optimizaciones clave: 1) Búsqueda de obstáculos: antes usaba claves de texto (strings) y recorría muchas celdas; se cambió a claves numéricas (índices de grid) y búsqueda por radio (solo celdas cercanas), logrando ~4.5x speedup. 2) Renderizado de suelo: antes se pintaban múltiples texturas por píxel en un mismo frame causando tirones; se limitó a una textura por celda y ambiente, con precarga de como máximo una textura por frame. Ambas mejoras en módulos de simulación y renderizado del juego (fase 7).

> Simulación lenta con muchos rivales. Búsqueda de obstáculos con claves de texto y demasiadas celdas. Búsqueda por radio con claves numéricas: unas 4,5 veces más rápida. Tirones al pintar el suelo. Se pintaban muchas texturas por píxel en el mismo fotograma. Una textura por celda y ambiente, como mucho una por fotograma y por adelantado
> — `repo:saas/docs/documentacion-tecnica.md` (cita sin comprobar)

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
