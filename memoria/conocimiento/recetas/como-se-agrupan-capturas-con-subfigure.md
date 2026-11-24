---
tipo: "receta"
titulo: "Agrupar capturas relacionadas en subfiguras con `subcaption` (LaTeX)"
temas: ["figura", "figuras", "latex", "maquetación", "subcaption", "subfigure"]
claves: ["subfigure", "subcaption", "0.48\\textwidth", "caption general", "agrupación"]
proyectos: ["memoria-procesos"]
fuentes: ["chapters/04-descripcion.tex, chapters/04b-juego.tex", "chapters/04-descripcion.tex", "memoria/chapters/04-descripcion.tex"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-24"
---

Temas: [[figura]] · [[figuras]] · [[latex]] · [[maquetación]] · [[subcaption]] · [[subfigure]]

**Temas:** [[figuras]] · [[latex]] · [[maquetación]] · [[subcaption]]

**Objetivo:** Evitar cadenas «La figura X muestra…» agrupando capturas relacionadas (mismo flujo, misma pantalla) en una única figura con entorno `subfigure` (paquete `subcaption` ya cargado). Cumple la **regla 13 de Javier**: prosa que explica qué hace el usuario y por qué la aplicación responde así, citando las figuras dentro de esa explicación.

---

### Procedimiento

1. **Entorno general**: `\begin{figure}[htbp]\centering` … `\end{figure}`.
2. **Subfiguras (dos por fila)**:  
   `\begin{subfigure}{0.48\textwidth}\centering` … `\end{subfigure}\hfill`  
   (Usar `\\` para salto de fila si se necesitan más de dos).
3. **Imagen en cada subfigura**:  
   `\includegraphics[<opciones>]{ruta}`  
   - **Móvil (vertical)**: `width=0.35\textwidth` (Nota A) **o** `width=\linewidth` (Nota B), `height=0.35\textheight` (Nota A paso 2 / Nota B ampl.) **o** `height=0.42\textheight` (Nota A paso 6 / Nota B código), `keepaspectratio`.  
   - **Escritorio**: `width=0.9\textwidth` máx (Nota A paso 6 / Nota B ampl.) **o** `width=\linewidth` (Nota A paso 2 / Nota B código), `height=0.42\textheight`, `keepaspectratio`.
4. **Metadatos por subfigura**: `\subcaption{...}` y `\label{fig:sub-...}` (Nota A) / `\label{fig:...}` (Nota B).
5. **Caption y label general**: Al final del entorno `figure`, `\caption{...}` y `\label{fig:general}` (Nota A) / `\label{fig:...}` (Nota B).
6. **Citación en texto**: Redactar en prosa la acción del usuario y la respuesta de la app, citando subfiguras o figura general según necesidad.  
   *Ejemplo (Nota A):* «Al registrarse, el formulario valida email y contraseña en cliente (subfigura~\ref{fig:app-registro}) y el servidor responde 409 si el email existe (subfigura~\ref{fig:app-entrar})».

---

### Ejemplos de código

**Esquema rápido (Nota A):**
```latex
\begin{subfigure}{0.48\textwidth}
  \centering
  \includegraphics[width=\linewidth,height=0.35\textheight,keepaspectratio]{ruta}
  \subcaption{...}
  \label{fig:sub-...}
\end{subfigure}\hfill
% ... segunda subfigure ...
\caption{...}
\label{fig:general}
```

**Ejemplo completo verificado (Nota B — `chapters/04-descripcion.tex`):**
```latex
\begin{figure}[htbp]\centering
\begin{subfigure}{0.48\textwidth}\centering
  \includegraphics[width=\linewidth,height=0.42\textheight,keepaspectratio]{figs/capturas/app/01-inicio.png}
  \subcaption{Página de inicio sin sesión.}
  \label{fig:app-inicio}
\end{subfigure}\hfill
\begin{subfigure}{0.48\textwidth}\centering
  \includegraphics[width=\linewidth,height=0.42\textheight,keepaspectratio]{figs/capturas/app/02-registro-validacion.png}
  \subcaption{Validación en cliente: email y contraseña con errores.}
  \label{fig:app-registro}
\end{subfigure}
\caption{Inicio y registro: página pública y validación del formulario.}
\label{fig:app-inicio-registro}
\end{figure}
```

---

### Referencias y enlaces relacionados

- **Origen común:** [[proyectos/memoria-procesos/estado|memoria-procesos]]
- **Archivos citados (sin comprobar):** `chapters/04-descripcion.tex`, `chapters/04b-juego.tex` (Nota A); `chapters/04-descripcion.tex` (Nota B).
- **Notas relacionadas (Nota B):**  
  `[[como-agrupar-capturas-con-subfigure-en-latex-para-manuales-d]]` · `[[agrupar-capturas-con-subfigure]]` · `[[reescribir-frases-la-figura-x-muestra-como-prosa-integrada]]` · `[[agrupar-capturas-relacionadas-en-subfiguras-con-prosa-integr]]` · `[[como-agrupar-capturas-con-subfigure-dos-por-fila]]`

> begin{subfigure}{0.48\textwidth} ... subcaption{...} ... end{subfigure} hfill ... caption{...} label{fig:...}
> — `chapters/04-descripcion.tex, chapters/04b-juego.tex` (cita sin comprobar)
> \begin{figure}[htbp]\centering\begin{subfigure}{0.48\textwidth}\centering\includegraphics[width=\linewidth,height=0.42\textheight,keepaspectratio]{figs/capturas/app/01-inicio.png}\subcaption{Página de inicio sin sesión.}\label{fig:app-inicio}\end{subfigure}\hfill\begin{subfigure}{0.48\textwidth}\centering\includegraphics[width=\linewidth,height=0.42\textheight,keepaspectratio]{figs/capturas/app/02-registro-validacion.png}\subcaption{Validación en cliente: email y contraseña con errores.}\label{fig:app-registro}\end{subfigure}\caption{Inicio y registro: página pública y validación del formulario.}\label{fig:app-inicio-registro}\end{figure}
> — `chapters/04-descripcion.tex` (cita sin comprobar)


> ⚠️ Posible contradicción al fusionar: Dimensiones de imagen contradictorias entre notas:  
- **Móvil**: Nota A (paso 6) dice `width=0.35\textwidth`; Nota B (ampliación 2026-11-23) dice `width=\linewidth` (≈ `0.48\textwidth` dentro del subfigure).  
- **Alto móvil**: Nota A (paso 2) y Nota B (ampliación) usan `height=0.35\textheight`; Nota A (paso 6) y Nota B (código) usan `height=0.42\textheight`.  
- **Escritorio ancho**: Nota A (paso 6) y Nota B (ampliación) limitan a `0.9\textwidth`; Nota A (paso 2) y Nota B (código) usan `\linewidth`.  
- **Prefijo de labels**: Nota A sugiere `fig:sub-...` / `fig:general`; Nota B usa `fig:app-*` descriptivos.

Fusionada con: Agrupar capturas relacionadas en subfiguras (subcaption)

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
