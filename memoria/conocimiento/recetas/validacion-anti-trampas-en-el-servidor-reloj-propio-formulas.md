---
tipo: "receta"
titulo: "Validación anti-trampas en el servidor (reloj propio, fórmulas de credibilidad, concurrencia optimista, ranking anónimo)"
temas: ["backend", "grada-colchonera", "saas", "security"]
claves: ["juegoService.js", "club.js", "logros.js", "UPDATE WHERE version", "reintentos", "jefes ≤ 3 + t/50", "nivel ≤ 8 + t/3", "bajas ≤ 20·t + 50", "15 s margen", "4 h máx", "mote y avatar en ranking"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/docs/documentacion-tecnica.md"]
confianza: "verificado"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[backend]] · [[grada-colchonera]] · [[saas]] · [[security]]

**Flujo servidor (`juegoService.js`):**
1. **Inicio:** guarda la partida en curso con su propio reloj (timestamp servidor).
2. **Fin:** el cliente envía resultado. El servidor rechaza si:
   - La partida no coincide con la guardada como «en curso».
   - Tiempo cliente > tiempo transcurrido servidor + 15 s **o** > 4 horas.
   - Valores no creíbles para ese tiempo `t` (segundos):
     - `jefes ≤ 3 + t/50`
     - `nivel ≤ 8 + t/3`
     - `bajas ≤ 20·t + 50`
3. **Logros:** de los que manda el cliente, solo registra los verificables con datos servidor (tiempo, jefes, bajas, jugador, entrenador); los de plantilla los calcula el servidor.
4. **Concurrencia optimista:** cada cambio de perfil (club, entrenamiento, etc.) usa `UPDATE … WHERE version = $n` con reintentos automáticos.
5. **Ranking:** guarda la mejor partida por usuario con **mote** y **avatar** (nunca el correo).

> Al **terminar**, rechaza el resultado si la partida no es la que está en curso, si el tiempo supera lo transcurrido (con 15 s de margen) o 4 horas, o si los jefes, el nivel o las bajas no son creíbles para ese tiempo (`jefes ≤ 3 + t/50`, `nivel ≤ 8 + t/3`, `bajas ≤ 20·t + 50`).
> — `repo:saas/docs/documentacion-tecnica.md`

Relacionado: [[perfil-de-juego-con-jsonb-y-concurrencia-optimista-mediante]] · [[cadena-de-middlewares-para-peticion-protegida-y-autorizacion]] · [[validacion-anti-trampas-en-servidor-con-reloj-propio-y-recha]] · [[esquema-de-progreso-guardado-en-servidor-migracion-003-tabla]] · [[partida-del-juego-inicio-bucle-de-simulacion-60-hz-y-fin-con]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
