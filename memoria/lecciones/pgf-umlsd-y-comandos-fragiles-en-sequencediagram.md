---
titulo: "pgf-umlsd y comandos frágiles en sequencediagram"
temas: ["latex", "pgf-umlsd", "sequencediagram"]
claves: ["Missing \\endcsname inserted", "\\protect", "\\csname"]
estado: "propuesta"
veces: 1
fecha: "2026-10-31"
proyectos: ["memoria-procesos"]
---

Temas: [[latex]] · [[pgf-umlsd]] · [[sequencediagram]]

## Problema
pgf-umlsd usa los textos de participantes, mensajes y bloques como nombres de macros internos (\csname ... \endcsname). Si esos textos contienen comandos LaTeX robustos (\texttt, \allowbreak, \url, ~, \textbackslash, etc.), al expandirse aparece \protect dentro del \csname y LuaLaTeX aborta con "Missing \endcsname inserted" al cerrar el entorno.

## Solución
Dentro del entorno sequencediagram, neutralizar TODOS los comandos frágiles posibles redefiniéndolos a versiones expandibles seguras (\lgc@umlsd@plain para comandos de un argumento, \lgc@umlsd@noop para comandos de cero argumentos). Además, parchear \newthread, \newinst, \call, \mess y sdblock para que apliquen \lgc@umlsd@plain a sus argumentos antes de pasarlos a pgf-umlsd. Prohibir cualquier comando LaTeX dentro de los diagramas de secuencia: solo texto plano.

## Ejemplo
|
  \begin{sequencediagram}
    \newthread{nav}{Navegador}
    \newinst[2]{api}{API (Express)}
    \begin{call}{nav}{POST /api/auth/login}{api}{200 o 401}
      \begin{call}{api}{authenticate(email, password)}{srv}{usuario}
      \end{call}
    \end{call}
  \end{sequencediagram}
  % Correcto: sin \texttt, \allowbreak, \url, etc.
  % Incorrecto: \newthread{nav}{\texttt{Navegador}} o \mess{api}{\allowbreak 401}{nav}

Origen: [[proyectos/memoria-procesos/bitacora|memoria-procesos]]
