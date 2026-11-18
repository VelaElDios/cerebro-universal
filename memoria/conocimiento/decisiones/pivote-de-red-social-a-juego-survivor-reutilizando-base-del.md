---
tipo: "decision"
titulo: "Pivote de red social a juego survivor reutilizando base del Sprint 1"
temas: ["decision", "grada-colchonera", "saas"]
claves: ["pivote", "red social", "juego", "survivor", "determinismo", "rendimiento", "validación servidor", "procedural", "audio sintetizado"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/docs/documentacion-tecnica.md"]
confianza: "verificado"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[decision]] · [[grada-colchonera]] · [[saas]]

Decisión estratégica: transformar el proyecto de "red social de aficionados" a "juego survivor (La Grada Colchonera)" tras Sprint 1.
Razones:
- Reutiliza 100% la base: auth, usuarios, admin, CI/CD, despliegue, BD, logs.
- Obliga a resolver retos técnicos valiosos para el TFG:
  * Simulación determinista (fixed timestep 1/60 s).
  * Rendimiento: 60 FPS con muchos rivales, procedural map, particle systems.
  * Validación servidor-autoritaria (anti-cheat).
  * Generación procedural de mapa desde semilla.
  * Audio 100% sintetizado (Web Audio API, chiptune, formantes vocales).
Resultado: proyecto más completo técnicamente y diferenciador.

> Pasar de red social a **juego** fue una buena decisión: reutiliza toda la base del sprint y obliga a resolver problemas técnicos interesantes (determinismo, rendimiento, validación en el servidor, generación procedural, audio sintetizado).
> — `repo:saas/docs/documentacion-tecnica.md`

Relacionado: [[cambio-de-alcance-de-red-social-a-juego-survivor-justificaci]] · [[cambio-de-enfoque-de-red-social-a-juego-justificado-en-la-in]] · [[arquitectura-del-juego-simulacion-determinista-presentacion]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
