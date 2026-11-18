---
tipo: "receta"
titulo: "Manual de usuario: entrada, menús, controles, oleadas, ambientes y fin de partida"
temas: ["game-design", "grada-colchonera", "saas", "ux"]
claves: ["#/jugar", "mote 3-16", "cara avatar", "WASD/joystick", "Espacio/E ulti", "Esc/P pausa", "F fullscreen", "1-3 mejoras", "oleada 30s", "jefe 4 oleadas", "ambientes 5 min", "pantalla fin estadísticas"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/docs/documentacion-tecnica.md"]
confianza: "verificado"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[game-design]] · [[grada-colchonera]] · [[saas]] · [[ux]]

**Flujo de juego:**
1. **Entrar:** ruta `#/jugar` con sesión; primer acceso pide mote único (3-16 chars) y cara de avatar.
2. **Menú principal:** botones Jugar, Vestuario, Entrenamiento, Contratar, Logros, Combinaciones, Dirección, Ranking, Ajustes; a la izquierda ficha del usuario y tiempos.
3. **Controles:** WASD / flechas (móvil: joystick al arrastrar); `Espacio`/`E` = ulti; `Esc`/`P` = pausa; `F` = pantalla completa; `1`–`3` = elegir mejora al subir de nivel.
4. **Partida:** nueva oleada cada 30 s; jefe cada 4 oleadas (primero a 1:30, luego cada 2 min). Rivales sueltan experiencia; al subir de nivel se ofrecen 3 mejoras (las que completan una combinación marcan ★).
5. **Ambientes:** cada 5 min cambia el fondo y la música: Pretemporada → Final Copa del Rey → Final Liga → Final Champions → Final Mundial (camiseta de selección). Rivales más fuertes y suena fanfarria de la competición.
6. **Fin:** al morir, pantalla con estadísticas (tiempo, ambiente, bajas, jefes, daño por habilidad, golpe más fuerte, daño recibido, logros nuevos) y recompensas del club (puntos de entrenamiento, ficha de contrato cada 3 jefes).

> 1. **Entrar:** con sesión iniciada, `#/jugar` abre el menú del juego. La primera vez pide un **mote** (3 a 16 caracteres, único) y una **cara** para el avatar.
> — `repo:saas/docs/documentacion-tecnica.md`

Relacionado: [[frontend-spa-con-rutas-por-hash-y-vistas-cargadas-bajo-deman]] · [[maquina-de-estados-de-la-cuenta-de-usuario]] · [[partida-del-juego-inicio-bucle-de-simulacion-60-hz-y-fin-con]] · [[arquitectura-del-juego-simulacion-determinista-presentacion]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
