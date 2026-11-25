---
tipo: "decision"
titulo: "Diagramas de secuencia con pgf-umlsd: entorno sequencediagram y reglas de sintaxis"
temas: ["diagramas-secuencia", "latex", "pgf-umlsd", "sequencediagram"]
claves: ["sequencediagram", "newthread", "newinst", "call", "mess", "sdblock", "alt", "participante", "mensaje"]
proyectos: ["memoria-procesos"]
fuentes: ["memoria/reglas-tfg.md (ejemplo compilado y probado)"]
confianza: "propuesto"
fecha: "2026-11-25"
actualizado: "2026-11-25"
---

Temas: [[diagramas-secuencia]] · [[latex]] · [[pgf-umlsd]] · [[sequencediagram]]

Ejemplo mínimo correcto:
\begin{verbatim}
\begin{figure}[htbp]
\centering
\begin{sequencediagram}
  \newthread{nav}{Navegador}
  \newinst[2]{api}{API (Express)}
  \newinst[2]{srv}{userService}
  \newinst[2]{bd}{PostgreSQL}
  \begin{call}{nav}{POST /api/auth/login}{api}{200 o 401}
    \begin{call}{api}{authenticate(email, contraseña)}{srv}{usuario}
      \begin{call}{srv}{SELECT por email}{bd}{fila}
      \end{call}
    \end{call}
  \end{call}
  \begin{sdblock}{alt}{cuenta pendiente}
    \mess{api}{403 + enlace de reenvío}{nav}
  \end{sdblock}
\end{sequencediagram}
\caption{Inicio de sesión local.}
\label{fig:sec-login}
\end{figure}
\end{verbatim}
Reglas clave: (1) Entorno `sequencediagram` en minúsculas. (2) `\newthread`/`\newinst` para declarar participantes (opcional `[n]` para separación horizontal). (3) `call{origen}{mensaje}{destino}{respuesta}` para llamadas anidadas. (4) `\mess{origen}{mensaje}{destino}` para mensajes simples. (5) `sdblock{alt}{condición}{...}` para alternativas. (6) Textos sin caracteres especiales LaTeX ni comandos. (7) Todos los participantes usados deben estar declarados. `revisar_umlsd.py` lo comprueba antes de compilar.

> El entorno es `sequencediagram` (en minúsculas; no existen `sequenceDiagram` ni un entorno `alt`: para alternativas, `sdblock`). Participantes con `\newthread`/`\newinst`, llamadas anidadas con `call` (origen, mensaje, destino, respuesta), mensajes sueltos con `\mess` y bloques alternativos con `sdblock`. En los textos de `\mess`, `call`, `callself` y `\newinst` no puede ir `\#`, `\_`, `\&`, `\%`, `\$`, `\{`, `\}`, ningún comando (`\texttt`…) ni `#`, `&`, `_`, `$` sueltos, y en `\mess` tampoco paréntesis. Todo participante que se use tiene que estar declarado con `\newthread`/`\newinst` en ese diagrama.
> — `memoria/reglas-tfg.md (ejemplo compilado y probado)` (cita sin comprobar)

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
