---
tipo: "receta"
titulo: "Diagramas de secuencia con pgf-umlsd: reglas de sintaxis"
temas: ["latex", "pgf-umlsd", "sequencediagram"]
claves: ["sequencediagram", "\\newthread", "\\newinst", "call", "\\mess", "sdblock"]
proyectos: ["memoria-procesos"]
fuentes: ["memoria/reglas-tfg.md (ejemplo compilado)"]
confianza: "propuesto"
fecha: "2026-11-22"
actualizado: "2026-11-22"
---

Temas: [[latex]] · [[pgf-umlsd]] · [[sequencediagram]]

Reglas obligatorias para que revisar_umlsd.py pase: 1) Cada participante usado debe estar declarado. 2) Sin caracteres especiales ni comandos en textos. 3) Sin paréntesis en \mess. 4) Usar sdblock para alt. 5) Entorno sequencediagram en minúsculas.

> \begin{sequencediagram} \newthread{nav}{Navegador} \newinst[2]{api}{API (Express)} \begin{call}{nav}{POST /api/auth/login}{api}{200 o 401} \begin{call}{api}{authenticate(email, contraseña)}{srv}{usuario} \begin{call}{srv}{SELECT por email}{bd}{fila} \end{call} \end{call} \end{call} \begin{sdblock}{alt}{cuenta pendiente} \mess{api}{403 + enlace de reenvío}{nav} \end{sdblock} \end{sequencediagram}
problema: Errores de sintaxis en diagramas de secuencia (participantes no declarados, caracteres prohibidos, paréntesis en \mess, comandos LaTeX en textos).
solucion: Declarar todos los participantes con \newthread/\newinst. En textos de \mess, call, callself, \newinst: no usar #, _, &, %, $, {}, comandos LaTeX, ni paréntesis en \mess. Usar sdblock para alternativas.
> — `memoria/reglas-tfg.md (ejemplo compilado)` (cita sin comprobar)

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
