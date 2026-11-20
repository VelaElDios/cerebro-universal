---
tipo: "receta"
titulo: "Diagramas de secuencia pgf-umlsd sintaxis correcta"
temas: ["diagramas", "latex", "pgf-umlsd", "diagramas-secuencia", "sequencediagram"]
claves: ["sequencediagram", "newthread", "newinst", "call", "mess", "sdblock"]
proyectos: ["memoria-procesos"]
fuentes: ["memoria/reglas-tfg.md", "spec del proyecto (ejemplo compilado y probado)", "memoria/reglas-tfg.md (ejemplo en spec)", "lección guardada (propuesta, sin confirmar)"]
confianza: "propuesto"
fecha: "2026-11-19"
actualizado: "2026-11-19"
---

Temas: [[diagramas]] · [[latex]] · [[pgf-umlsd]]

Sintaxis obligatoria para diagramas de secuencia en esta plantilla: (1) Entorno `sequencediagram` (minúsculas). (2) Participantes: `\newthread{id}{Nombre}` para hilos, `\newinst[desplazamiento]{id}{Nombre}` para instancias. (3) Llamadas anidadas: `\begin{call}{origen}{mensaje}{destino}{respuesta}...\end{call}`. (4) Mensajes simples: `\mess{origen}{mensaje}{destino}`. (5) Alternativas: `\begin{sdblock}{alt}{condición}...\end{sdblock}`. (6) En textos de `\mess`, `call`, `callself`, `\newinst`: NO usar `#`, `_`, `&`, `%`, `$`, `{`, `}`, comandos LaTeX (`\texttt`...), paréntesis en `\mess`. (7) Todo participante usado debe estar declarado en ese diagrama. (8) Usar `\resizebox{\textwidth}{!}{...}` para diagramas anchos; `adjustbox{max totalheight=0.6\textheight}` si ocupan casi una página.

> El entorno es `sequencediagram` (en minúsculas; **no** existen `sequenceDiagram` ni un entorno `alt`: para alternativas, `sdblock`): participantes con `\newthread`/`\newinst`, llamadas anidadas con `call` (origen, mensaje, destino, respuesta), mensajes sueltos con `\mess` y bloques alternativos con `sdblock`.
> — `memoria/reglas-tfg.md` (cita sin comprobar)

## Ampliación (2026-11-19, memoria-procesos)
|
  **Sintaxis obligatoria (ya probada y compilando en esta plantilla):**
  
  ```latex
  \begin{figure}[htbp]
  \centering
  \resizebox{\textwidth}{!}{%
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
  \end{sequencediagram}}
  \caption{Inicio de sesión local.}
  \label{fig:sec-login}
  \end{figure}
  ```
  
  **Reglas estrictas (revisar_umlsd.py las comprueba):**
  1. Entorno: `sequencediagram` (minúsculas)
  2. Participantes: `\newthread{id}{Label}` o `\newinst[n]{id}{Label}` — `id` no vacío, sin espacios, sin caracteres especiales
  3. Llamadas anidadas: `\begin{call}{origen}{mensaje}{destino}{respuesta} ... \end{call}`
  4. Mensajes simples: `\mess{origen}{mensaje}{destino}`
  5. Alternativas: `\begin{sdblock}{alt}{condición} ... \end{sdblock}` (no existe entorno `alt`)
  6. Bucles: `\begin{sdblock}{loop}{condición} ... \end{sdblock}`
  7. **Caracteres prohibidos en mensajes** (de `\mess`, `\call`, `\callself`, `\newinst`):
     - `\#`, `\_`, `\&`, `\%`, `\$`, `\{`, `\}`, cualquier comando (`\texttt`…)
     - `#`, `&`, `_`, `$` sueltos
     - En `\mess` **tampoco paréntesis** `(` `)`
  8. Todo participante usado debe estar declarado en ese diagrama
  9. Envolver en `\resizebox{\textwidth}{!}{...}` y opcionalmente en `adjustbox{max width=\textwidth, max totalheight=0.6\textheight}`
  
  **Errores comunes que rompen la compilación:**
  - Participante vacío: `\newinst{}{Label}` → "el participante «» no está declarado"
  - Mensaje vacío: `\mess{a}{}{b}` → error de sintaxis
  - Paréntesis en \mess: `\mess{a}{func(x)}{b}` → usar `func x` o `funcion x`
  - Comando en mensaje: `\mess{a}{\texttt{POST}}{b}` → usar `POST`
  - `alt` como entorno: `\begin{alt}...\end{alt}` → usar `sdblock`

## Ampliación (2026-11-19, memoria-procesos)
|
  Reglas de sintaxis obligatorias (comprobadas por revisar_umlsd.py):
  - Entorno: `\begin{sequencediagram} ... \end{sequencediagram}` (minúsculas).
  - Participantes: `\newthread{id}{Nombre}` o `\newinst[desplazamiento]{id}{Nombre}`. Cada id usado debe estar declarado.
  - Llamadas anidadas: `\begin{call}{origen}{mensaje}{destino}{respuesta} ... \end{call}`.
  - Mensajes simples: `\mess{origen}{mensaje}{destino}`.
  - Alternativas: `\begin{sdblock}{alt}{condición} ... \end{sdblock}` (no existe entorno `alt`).
  - En textos de `\mess`, `call`, `callself`, `\newinst`: no `#`, `_`, `&`, `%`, `$`, `{`, `}`, `\`, comandos LaTeX, ni paréntesis en `\mess`.
  - Usar `\resizebox{\textwidth}{!}{...}` para encoger un poco; si ocupa casi una página, `adjustbox{max width=\textwidth,max totalheight=0.6\textheight}`.
  - Ejemplo correcto en la spec del proyecto.

## Ampliación (2026-11-19, memoria-procesos)
Sintaxis válida obligatoria:
- Participantes: `\newthread{nombre}{Etiqueta}` o `\newinst[desplazamiento]{nombre}{Etiqueta}` — **nombre nunca vacío**.
- Llamadas anidadas: `\begin{call}{origen}{mensaje}{destino}{respuesta} ... \end{call}`.
- Mensajes sueltos: `\mess{origen}{mensaje}{destino}` — **sin paréntesis en el mensaje**, sin comandos LaTeX, sin `#`, `&`, `_`, `$`, `%`, `{`, `}` sueltos.
- Bloques alternativos: `\begin{sdblock}{alt}{condición} \mess{...} \end{sdblock}` — no usar `alt` como entorno, solo como primer argumento de `sdblock`.
- Bucles: `\begin{sdblock}{loop}{condición} ... \end{sdblock}`.
- **Antes de compilar**, pasar `scripts/revisar_umlsd.py` que valida sintaxis completa y dice todos los fallos a la vez.
Ejemplo mínimo correcto:
```latex
\begin{sequencediagram}
  \newthread{u}{Usuario}
  \newinst[2]{api}{API}
  \begin{call}{u}{petición}{api}{respuesta}
  \end{call}
  \begin{sdblock}{alt}{caso error}
    \mess{api}{400 error}{u}
  \end{sdblock}
\end{sequencediagram}
```

Relacionado: [[diagramas-de-secuencia-con-pgf-umlsd-sequencediagram]] · [[como-corregir-diagramas-de-secuencia-pgf-umlsd-para-pasar-re]] · [[diagramas-de-secuencia-con-pgf-umlsd]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
