---
tipo: "dato"
titulo: "Catálogo de sistemas del juego (jugadores, rarezas, entrenadores, armas, pasivas, combos, ultras, rivales, jefes, dificultad, movimiento, mundo, club, logros, sonido)"
temas: ["data", "game-design", "grada-colchonera", "saas"]
claves: ["PERSONAJES", "POSICIONES", "RAREZAS", "ENTRENADORES", "ARMAS", "PASIVAS", "SINERGIAS", "ULTRAS", "EQUIPOS", "ELITES", "JEFES", "ESCALADO", "TRAMO_FINAL", "CURTIDOS", "AMBIENTES", "FISICA", "JUGADOR", "TERRENO", "club.js", "logros.js", "audio.js", "musica.js"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/docs/documentacion-tecnica.md"]
confianza: "verificado"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[data]] · [[game-design]] · [[grada-colchonera]] · [[saas]]

**Resumen de sistemas (configuración en `config.js`):**
- **Jugadores:** 36 (4 POR, 9 DEF, 13 MED, 10 DEL). Posición define stats base; cada uno tiene rasgos y lista de habilidades aprendibles.
- **Rarezas:** por historia en el Atleti: Leyenda (8), Épico (8), Raro (8), Común (12). Más rareza = más habilidades (8-16) y menos probabilidad en contrato.
- **Entrenadores:** Cholo Simeone (+daño, +vida; ulti «¡Partido a partido!»), Luis Aragonés (+velocidad, +exp; ulti «Furia Roja»).
- **Armas/habilidades:** 24, 5 niveles. Categorías: disparo (balón, cañonazo, córner, efecto, vaselina, chilena, volea, penalti), cuerpo a cuerpo (bufanda, banderines, cántico, silbato, tarjeta roja, VAR, cabezazo, entrada, barrera, despeje), movilidad (regate, caño, pared, contragolpe), especiales (himno Champions, bengala). Las fuertes tienen `desdeMinuto` y `cdMin`.
- **Pasivas:** 14 (botas, imán, pasión, pizarra, cantera, masajista, espinilleras, pulmones, toque dorado, botas en llamas, paradón, brazalete, trébol, prórroga).
- **Combinaciones (sinergias):** 24 metas (Muro rojiblanco, Tiki-taka, Pichichi, Catenaccio, Leyenda rojiblanca, Golazo de otro planeta, Remontada épica, Triple Corona, Infierno del Metropolitano, Capitán eterno…).
- **Ultras:** 6 (Premio Puskás, Balón de Oro, MVP Champions, Trofeo Zamora, Bota de Oro histórica, Mejor jugador Mundial). Se consiguen completando varias combinaciones; efecto visual y daño porcentual (menor vs jefes).
- **Rivales:** 16 equipos genéricos; embisten (Liverpool, Arsenal, PSG, Dortmund) o disparan (Bayern, City, Chelsea, Juventus, Milan, Inter, Nápoles); élites: blindado, veloz, furioso.
- **Jefes:** 10 (Guardiola, Mourinho, Cristiano, Messi, Vinicius, Yamal, Neymar, Bale, Benzema, Suárez). 3 fases por vida (66% y 33%), escolta de élites desde 2º jefe, furia si tardas, jugada estrella en fase 3. Desde oleada 24 pueden salir dos a la vez; cada vuelta completa +25% dificultad.
- **Dificultad:** crecimiento continuo vida/daño/velocidad; tramo final más duro desde min 9; rivales «curtidos» desde min 12; multiplicador por ambiente; ayuda inicial se apaga a los 8 min.
- **Movimiento:** inercia, *ritmo* al correr (más daño y exp), castigo por quietud, premios por campo.
- **Mundo:** procedural infinito por semilla, ruido suave: distritos (ciudad, entrenamiento, parque, prado), estadios con gradas, plazas, tiendas, mesetas, escaleras, barro, lluvia, caminos. Colisión por pies (vista 3/4).
- **Club:** plantilla inicial 4 comunes (1 por posición); ficha de contrato cada 3 jefes de la cuenta; puntos de entrenamiento por jefes (1 c/3) y por bajas; stats Vida, Defensa, Disparo, Suerte (máx 20).
- **Logros:** 29 con dato histórico real (tabla 9.6); 10 equipaciones desbloqueables.
- **Sonido:** efectos, música chiptune original (canción por ambiente que se anima con tiempo y jefes, fanfarria por competición), grada (murmullo y cánticos según distancia a gradas).

> | **Jugadores** | 36 (4 porteros, 9 defensas, 13 medios, 10 delanteros). La posición fija las estadísticas base; cada jugador tiene rasgos propios y una lista de habilidades que puede aprender | `PERSONAJES`, `POSICIONES` |
> — `repo:saas/docs/documentacion-tecnica.md`

Relacionado: [[requisitos-funcionales-del-juego-sprint-2-20-rj-con-trazabil]] · [[tabla-de-trazabilidad-sprint-2-pbi-etiqueta-titulo-tareas-pr]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
