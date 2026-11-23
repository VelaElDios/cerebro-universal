---
tipo: "concepto"
titulo: "Diagramas de secuencia pgf-umlsd — sintaxis válida y errores comunes"
temas: ["latex", "pgf-umlsd", "sequencediagram", "verificacion"]
claves: ["sequencediagram", "newthread", "newinst", "call", "mess", "sdblock", "revisar_umlsd.py"]
proyectos: ["memoria-procesos"]
fuentes: ["spec versión 4 (ejemplo compilado) y revisar_umlsd.py", "spec del proyecto (ejemplo compilado)"]
confianza: "propuesto"
fecha: "2026-11-23"
actualizado: "2026-11-23"
---

Temas: [[latex]] · [[pgf-umlsd]] · [[sequencediagram]] · [[verificacion]]

**Sintaxis obligatoria** (probada y compilada):
```latex
\begin{figure}[htbp]
\centering
\begin{adjustbox}{max width=\textwidth, max totalheight=0.6\textheight}
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
\end{adjustbox}
\caption{Inicio de sesión local.}
\label{fig:sec-login}
\end{figure}
```
**Reglas estrictas** (revisar_umlsd.py las comprueba):
1. Entorno: `sequencediagram` (minúsculas).
2. Participantes: `\newthread{id}{Nombre}` o `\newinst[desplazamiento]{id}{Nombre}` — **todos los usados deben estar declarados**.
3. Llamadas anidadas: `\begin{call}{origen}{mensaje}{destino}{respuesta} ... \end{call}`.
4. Mensajes sueltos: `\mess{origen}{mensaje}{destino}`.
5. Alternativas: `\begin{sdblock}{alt}{condición} ... \end{sdblock}` (no existe entorno `alt`).
6. **Prohibido en textos de `\mess`, `call`, `callself`, `\newinst`**:
   - `\#`, `\_`, `\&`, `\%`, `\$`, `\{`, `\}`
   - Comandos LaTeX (`\texttt`, `\path`, etc.)
   - Caracteres sueltos `#`, `&`, `_`, `$`
   - Paréntesis `(` `)` en `\mess` (sí en `call`).
7. **Nodos TikZ vacíos no existen** en este paquete.
**Errores comunes detectados**:
- Usar `sequenceDiagram` (mayúsculas) → no compila.
- Usar `alt` como entorno → error.
- Poner `\texttt{...}` dentro de `\mess` → revisar_umlsd.py falla.
- Paréntesis en `\mess{api}{403 (error)}{nav}` → falla.
- Participante usado sin declarar → falla.
**Solución**: Escribir textos planos, escapar `_` como `\_` solo si es código en `\texttt{}`, pero mejor evitar código en textos de secuencia; usar descripciones cortas sin símbolos especiales.

> El entorno es sequencediagram (en minúsculas; no existen sequenceDiagram ni un entorno alt: para alternativas, sdblock).
> — `spec versión 4 (ejemplo compilado) y revisar_umlsd.py` (cita sin comprobar)

## Ampliación (2026-11-23, memoria-procesos)
Reglas de sintaxis (comprobadas por revisar_umlsd.py):
- Entorno: `\begin{sequencediagram} ... \end{sequencediagram}` (minúsculas).
- Participantes: `\newthread{id}{Nombre}` (línea de vida con caja) o `\newinst[dist]{id}{Nombre}` (solo línea). `dist` opcional (default 2).
- Llamadas: `\begin{call}{origen}{mensaje}{destino}{respuesta} ... \end{call}`. Anidables.
- Mensajes sueltos: `\mess{origen}{mensaje}{destino}`. Sin paréntesis en el mensaje.
- Alternativas: `\begin{sdblock}{alt}{condición} ... \end{sdblock}`. No existe `alt` ni `else` sueltos.
- Textos en `\mess`, `call`, `callself`, `\newinst`: NO `#`, `\_`, `\&`, `\%`, `\$`, `\{`, `\}`, comandos LaTeX (`\texttt`...), ni `#`, `&`, `_`, `$` sueltos. En `\mess` tampoco paréntesis.
- Todo participante usado debe estar declarado en ese diagrama.
- Envolver diagramas grandes en `\resizebox{\textwidth}{!}{...}` o `adjustbox{max width=\textwidth, max totalheight=0.6\textheight}`.
- Fuente: `\scriptsize` o `\footnotesize` antes de `\begin{sequencediagram}` para letras ≥8pt en PDF.

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
