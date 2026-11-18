---
tipo: "decision"
titulo: "Cambio de alcance: de red social a juego survivor (justificación)"
temas: ["alcance", "grada-colchonera", "saas", "sprint"]
claves: ["pivot", "red social", "juego", "sprint 1", "sprint 2", "justificación"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/docs/documentacion-tecnica.md"]
confianza: "verificado"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[alcance]] · [[grada-colchonera]] · [[saas]] · [[sprint]]

Decisión documentada y justificada tras cerrar el Sprint 1. El proyecto nació como red social para aficionados del Atlético de Madrid; al terminar la base SaaS común (hitos 1-4), el profesor dio libertad para la lógica del Sprint 2 y se optó por un juego *survivor* por tres razones: (1) originalidad frente a clon de red social; (2) riqueza técnica (simulación determinista, canvas, generación procedural, audio sintetizado, anti-cheat servidor); (3) reutilización total de la base SaaS (cuentas, sesión, roles, persistencia, despliegue, panel admin, logs). En la memoria debe contarse como cambio de alcance justificado (sección 2.3). Fuera de alcance quedan multijugador tiempo real, amigos/partidas en grupo y apps nativas (sección 15).

> **Por qué un juego y no una red social.** La idea inicial era una red social tipo Twitter para aficionados del Atleti. Cerrado el Sprint 1, el profesor dejó libertad para la lógica y el diseño del producto (y fijó después que el Sprint 2 sería esa lógica), y se decidió hacer un juego porque: (1) es más original y diferenciador que otro clon de red social; (2) permite trabajar problemas técnicos más ricos (simulación determinista, rendimiento en canvas, generación procedural, sonido sintetizado, validación anti-trampas en el servidor); y (3) reutiliza entera la base SaaS del sprint: un juego con cuentas, progreso en el servidor, ranking y roles necesita exactamente lo que piden los hitos.
> — `repo:saas/docs/documentacion-tecnica.md`

Relacionado: [[cada-entrega-solo-lleva-lo-de-su-sprint-alcance-coherente]] · [[pivote-de-red-social-a-juego-survivor-reutilizando-base-del]] · [[cambio-de-enfoque-de-red-social-a-juego-justificado-en-la-in]] · [[cambio-de-alcance-durante-sprint-1-anadido-p19-cloud-run-por]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
