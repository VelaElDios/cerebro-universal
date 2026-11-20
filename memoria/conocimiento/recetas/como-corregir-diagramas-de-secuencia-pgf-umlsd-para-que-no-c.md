---
tipo: "receta"
titulo: "Cómo corregir diagramas de secuencia pgf-umlsd para que no crucen cajas alt"
temas: ["latex", "memoria", "pgf-umlsd", "sequencediagram"]
claves: ["fig:sec-login", "sdblock", "flecha discontinua", "alt", "caja"]
proyectos: ["memoria-procesos"]
fuentes: ["chapters/04-descripcion.tex"]
confianza: "propuesto"
fecha: "2026-11-20"
actualizado: "2026-11-20"
---

Temas: [[latex]] · [[memoria]] · [[pgf-umlsd]] · [[sequencediagram]]

|
  1. En pgf-umlsd, los bloques `sdblock{alt}{...}` crean cajas visuales que agrupan mensajes alternativos.
  2. Las flechas de retorno discontinuas (las que cierran un `call`) se dibujan automáticamente y pueden atravesar cajas `alt` si hay anidamiento.
  3. No añadir `\mess` adicionales después del `call` principal que vayan de un participante a otro si hay cajas `alt` entre medio.
  4. Estructura correcta:
     - `call` principal (fe→a→s)
     - Dentro: `call` anidado (a→s) + `sdblock` alt para cada caso
     - Cerrar `call` anidado y `call` principal → pgf-umlsd dibuja las flechas de retorno automáticamente.
  5. Si se quiere mostrar la respuesta al frontend, está implícita en el cierre del `call` fe→a. No hace falta `\mess{a}{...}{fe}`.
  6. Verificar en PDF: ninguna flecha discontinua cruza el borde de una caja `alt`, las líneas de vida son verticales limpias.
ejemplo: |
  \begin{sequencediagram}
    \newthread{u}{Usuario}
    \newinst[2]{fe}{Frontend}
    \newinst[2]{a}{API login}
    \newinst[2]{s}{userService}
    \begin{call}{u}{email y contrasena}{fe}{ok}
    \end{call}
    \begin{call}{fe}{POST login}{a}{200 o 401}
      \begin{call}{a}{authenticate}{s}{usuario}
      \end{call}
      \begin{sdblock}{alt}{email desconocido o contrasena mala}
        \mess{s}{401 mismo mensaje}{a}
      \end{sdblock}
      \begin{sdblock}{alt}{cuenta pendiente}
        \mess{s}{403 cuenta pendiente}{a}
      \end{sdblock}
      \begin{sdblock}{alt}{correcto}
        \mess{a}{200 usuario y cookie}{fe}
      \end{sdblock}
    \end{call}
    % NO añadir \mess sueltas aquí
  \end{sequencediagram}

> La línea vertical discontinua de retorno de 'authenticate' atraviesa el borde izquierdo de la caja 'alt' inferior correspondiente a 'cuenta pendiente'.
problema: Las flechas \mess sueltas después del bloque call principal (respuestas 403 y 200) salían del participante 'a' (API) hacia 'fe' (Frontend) pero cruzaban la caja 'alt' de 'cuenta pendiente' porque pgf-umlsd dibuja las líneas de retorno discontinuas dentro del flujo anidado.
solucion: Eliminar las \mess sueltas que cruzan cajas alt. Las respuestas del API al Frontend ya están representadas implícitamente por el cierre de los bloques call/sdblock. Si se necesitan mostrar explícitamente, usar flechas normales fuera de cualquier sdblock y asegurar que los participantes sean contiguos (sin cajas entre medio). Aumentar node distance vertical entre participantes.
> — `chapters/04-descripcion.tex` (cita sin comprobar)

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
