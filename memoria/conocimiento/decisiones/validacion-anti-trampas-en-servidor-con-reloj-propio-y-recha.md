---
tipo: "decision"
titulo: "Validación anti-trampas en servidor con reloj propio y rechazo de resultados imposibles"
temas: ["anti-cheat", "backend", "donetonic", "grada-colchonera", "scrum", "seguridad", "validacion"]
claves: ["anti-trampas", "reloj servidor", "resultados imposibles", "P29"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/docs/gestion/README.md"]
confianza: "verificado"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[anti-cheat]] · [[backend]] · [[donetonic]] · [[grada-colchonera]] · [[scrum]] · [[seguridad]] · [[validacion]]

Al recibir POST /api/juego/terminar, el servidor:
1. Comprueba que el tiempo enviado ≥ tiempo mínimo teórico para llegar a ese nivel/jefes (basado en simulación determinista).
2. Verifica que stats (daño total, bajas, nivel) no superen máximos calculados con la semilla de la partida.
3. Rechaza (400) si algo no cuadra; no guarda ni actualiza perfil.
4. Usa su propio Date.now() / performance.now() como referencia, no confía en timestamps del cliente.
Esto evita speed-hacks, god-mode y envío de partidas falsificadas.

> El servidor valida cada resultado con su propio reloj (anti-trampas) y rechaza resultados imposibles.
> — `repo:saas/docs/gestion/README.md`

Relacionado: [[cadena-de-middlewares-para-peticion-protegida-y-autorizacion]] · [[validacion-anti-trampas-en-el-servidor-reloj-propio-formulas]] · [[esquema-de-progreso-guardado-en-servidor-migracion-003-tabla]] · [[partida-del-juego-inicio-bucle-de-simulacion-60-hz-y-fin-con]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
