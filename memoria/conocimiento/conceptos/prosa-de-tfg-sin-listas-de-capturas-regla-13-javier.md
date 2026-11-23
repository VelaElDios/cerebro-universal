---
tipo: "concepto"
titulo: "Prosa de TFG sin listas de capturas (regla 13 Javier)"
temas: ["latex", "redacción", "tfg", "figuras", "maquetacion", "redaccion", "estilo"]
claves: ["subfigure", "prosa", "manual de usuario", "\\ref"]
proyectos: ["memoria-procesos"]
fuentes: ["memoria/reglas-tfg.md (regla 13)", "memoria/reglas-tfg.md"]
confianza: "verificado"
fecha: "2026-11-21"
actualizado: "2026-11-23"
---

Temas: [[latex]] · [[redacción]] · [[tfg]]

Reescribir secciones de manual de usuario (cap 4, 4b) como prosa continua: explicar qué hace el usuario y por qué la app responde, citando figuras con \ref dentro del texto. Agrupar capturas relacionadas en una sola figure con subfigure (dos por fila, \begin{subfigure}{0.48\textwidth}), un \caption general y \subcaption por subfigura. Eliminar cualquier frase que empiece por "La figura", "La captura", "En la imagen" seguida solo de descripción visual sin contexto de uso.

> Prosa de TFG, no listas de capturas: nada de una frase suelta «La figura X muestra…» por cada imagen. Las capturas se explican dentro de párrafos que cuentan qué hace el usuario y por qué la aplicación responde así. Las que van juntas se agrupan con subfigure.
> — `memoria/reglas-tfg.md (regla 13)`

## Ampliación (2026-11-22, memoria-procesos)
Cada figura y tabla se cita en el texto y se explica, no hay texto de relleno y el orden de las secciones sigue el de la plantilla. Las capturas relacionadas van juntas en una figura con subfigure (de subcaption, dos por fila, \begin{subfigure}{0.48\textwidth}), con un caption general y uno por subfigura.
relacionado: Cada imagen una sola vez (regla 10), Capturas máx. height=0.42\textheight (regla 8)

Relacionado: [[prosa-de-tfg-sin-cadenas-la-figura-x-muestra-regla-13-javier]] · [[prosa-de-tfg-nada-de-la-figura-x-muestra-suelto-agrupar-capt]] · [[prosa-de-tfg-en-lugar-de-listas-de-capturas-regla-13-javier]]

## Ampliación (2026-11-23, memoria-procesos)
El manual de uso (cap:descripcion §La aplicación) y el del juego (cap:juego §Cómo se juega) se escriben como prosa que explica qué hace el usuario y por qué la aplicación responde así, citando las figuras dentro de esa explicación. Las capturas relacionadas van juntas en una figura con `subfigure` (de `subcaption`, dos por fila, `\begin{subfigure}{0.48\textwidth}`), con un caption general y uno por subfigura. Ejemplo: en 04-descripcion.tex se agrupan inicio+registro (fig:app-inicio-registro), errores de acceso (fig:app-errores-acceso), perfil+baja (fig:app-perfil-baja), admin completo+búsqueda (fig:app-admin-full), responsive (fig:app-responsive), estados especiales (fig:app-estados-especiales), flujo Hito 4 (fig:hito4-flujo, fig:hito4-estados-privacidad). En 04b-juego.tex: menú+vestuario (fig:juego-menu-vestuario), partida+mejora (fig:juego-partida-mejora), jefe+ambiente (fig:juego-jefe-ambiente), fin+pausa (fig:juego-fin-pausa), club pantallas I (fig:juego-club-pantallas-a), club pantallas II (fig:juego-club-pantallas-b).

## Ampliación (2026-11-23, memoria-procesos)
- Eliminar toda frase que empiece por "La figura X muestra" o "En la figura X se ve".
- Escribir párrafos que narren la interacción del usuario: "Al acceder sin sesión, el usuario ve la página de inicio (Figura~\ref{fig:app-inicio}) con dos accesos directos... Si elige registrarse, el formulario valida en cliente (Figura~\ref{fig:app-registro})..."
- Agrupar capturas relacionadas en una sola figura con `subfigure` (dos por fila, `\begin{subfigure}{0.48\textwidth}`), caption general y subcaptions.
- Cada figura/tabla debe tener `\caption`, `\label` y ser citada con `\ref` en el texto.

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
