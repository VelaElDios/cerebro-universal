---
tipo: "receta"
titulo: "Cómo agrupar capturas relacionadas con subfigure (dos por fila) usando subcaption en LaTeX"
temas: ["capturas", "figura", "figuras", "latex", "maquetacion", "maquetación", "memoria-procesos", "subcaption", "subfigure"]
claves: ["subfigure", "0.48\\textwidth", "caption general", "caption individual", "subcaption", "cludegraphics", "width", "height", "keepaspectratio", "agrupación", "capturas"]
proyectos: ["memoria-procesos"]
fuentes: ["memoria/chapters/04-descripcion.tex", "memoria/reglas-tfg.md", "memoria/reglas-tfg.md (regla 13) y spec del proyecto", "chapters/04-descripcion.tex (ejemplo real compilado)", "memoria/chapters/04-descripcion.tex (fig:app-inicio-registro, fig:app-errores-acceso, fig:app-perfil-baja, fig:app-admin-full, fig:app-responsive, fig:app-estados-especiales, fig:hito4-flujo, fig:hito4-estados-privacidad)", "spec versión 4 y 04-descripcion.tex / 04b-juego.tex corregidos", "chapters/04-descripcion.tex, chapters/04b-juego.tex", "chapters/04-descripcion.tex"]
confianza: "propuesto"
fecha: "2026-11-23"
actualizado: "2026-11-25"
---

Temas: [[capturas]] · [[figura]] · [[figuras]] · [[latex]] · [[maquetacion]] · [[maquetación]] · [[memoria-procesos]] · [[subcaption]] · [[subfigure]]

# Cómo agrupar capturas relacionadas con subfigure (dos por fila) usando subcaption en LaTeX

**Temas:** [[capturas]] · [[figuras]] · [[figura]] · [[latex]] · [[maquetacion]] · [[maquetación]] · [[memoria-procesos]] · [[subcaption]] · [[subfigure]]

**Origen común:** [[proyectos/memoria-procesos/estado|memoria-procesos]]

---

### Propósito / Objetivo
Evitar cadenas de «La figura X muestra…» agrupando capturas relacionadas (mismo flujo, misma pantalla) en una sola figura con entorno `subfigure` (paquete `subcaption`, ya cargado), dos por fila, con un `\caption` general y un `\subcaption` por subfigura. Cada subfigura lleva su `\label` y se cita con `\ref` / `\subref` en la prosa que explica el flujo de usuario. Cumple la **regla 13 de Javier**: prosa que explica qué hace el usuario y por qué la aplicación responde así, citando las figuras dentro de esa explicación.

---

### Plantilla obligatoria / Procedimiento (2 capturas relacionadas, disposición horizontal)

**Patrón genérico**
```latex
\begin{figure}[htbp]
\centering
\begin{subfigure}{0.48\textwidth}
\centering
\includegraphics[width=\linewidth,height=0.35\textheight,keepaspectratio]{figs/capturas/carpeta/imagen1}
\subcaption{Descripción corta imagen 1.}
\label{fig:etiqueta1}
\end{subfigure}
\hfill
\begin{subfigure}{0.48\textwidth}
\centering
\includegraphics[width=\linewidth,height=0.35\textheight,keepaspectratio]{figs/capturas/carpeta/imagen2}
\subcaption{Descripción corta imagen 2.}
\label{fig:etiqueta2}
\end{subfigure}
\caption{Caption general que une las dos imágenes.}
\label{fig:etiqueta-general}
\end{figure}
```

**Ejemplo concreto verificado (memoria-procesos, 2026-11-23)**
```latex
\begin{figure}[htbp]
\centering
\begin{subfigure}{0.48\textwidth}
\centering
\includegraphics[width=\linewidth,height=0.35\textheight,keepaspectratio]{figs/capturas/app/01-inicio.png}
\subcaption{Página de inicio sin sesión.}
\label{fig:app-inicio}
\end{subfigure}
\hfill
\begin{subfigure}{0.48\textwidth}
\centering
\includegraphics[width=\linewidth,height=0.35\textheight,keepaspectratio]{figs/capturas/app/02-registro-validacion.png}
\subcaption{Validación en cliente: email y contraseña con errores.}
\label{fig:app-registro}
\end{subfigure}
\caption{Inicio y registro: página pública y validación del formulario.}
\label{fig:app-inicio-registro}
\end{figure}
```

**Ejemplo completo alternativo (Nota B — `chapters/04-descripcion.tex` con `height=0.42\textheight`)**
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

**Pasos resumidos (fusionados de ambas notas)**
1. **Entorno general**: `\begin{figure}[htbp]\centering` … `\end{figure}`.
2. **Subfiguras (dos por fila)**:  
   `\begin{subfigure}{0.48\textwidth}\centering` … `\end{subfigure}\hfill`  
   (Usar `\\` para salto de fila si se necesitan más de dos).
3. **Imagen en cada subfigura**:  
   `\includegraphics[<opciones>]{ruta}` — *ver tabla de parámetros consolidada abajo*.
4. **Metadatos por subfigura**: `\subcaption{...}` y `\label{fig:...}` (prefijo descriptivo recomendado, p.ej. `fig:app-*`).
5. **Caption y label general**: Al final del entorno `figure`, `\caption{...}` y `\label{fig:...}`.
6. **Citación en texto**: Redactar en prosa la acción del usuario y la respuesta de la app, citando subfiguras o figura general según necesidad.  
   *Ejemplo:* «Al acceder sin sesión, el usuario ve la página de inicio (Figura~\ref{fig:app-inicio}) y, al registrarse, la validación en cliente muestra errores en línea (Figura~\ref{fig:app-registro}).»

---

### Reglas de maquetación
- **Dos por fila**: `0.48\textwidth` + `\hfill`.
- **Caption general** (`\caption`) y uno por subfigura (`\subcaption`).
- **Cada subfigura con su `\label`** para citar con `\ref` o `\subref`.
- **Verticales (móvil)**: `width=0.35\textwidth` (Nota A) **o** `width=\linewidth` (Nota B, equivale a `0.48\textwidth` dentro del subfigure); el resto `width=0.9\textwidth` máx (Nota A/Nota B ampliación) **o** `width=\linewidth` (Nota A paso 2 / Nota B código).
- **Regla 8**: ninguna página con una sola imagen; si una figura queda sola, reducir height o agrupar.
- **Siempre** `keepaspectratio`.

---

### Parámetros de imagen (tabla consolidada con contradicciones explícitas)

| Contexto | `width` en `\includegraphics` | `height` en `\includegraphics` | Notas / Fuentes |
|---|---|---|---|
| **Verticales (móvil)** | `0.35\textwidth` (Nota A paso 6) **vs** `width=\linewidth` ≈ `0.48\textwidth` (Nota B ampliación / código) | `0.35\textheight` (Nota A paso 2, Nota B ampliación) **vs** `0.42\textheight` (Nota A paso 6, Nota B código) | En `subfigure` usar `width=\linewidth` respeta el `0.48\textwidth` del contenedor. **No hay consenso único**. |
| **Horizontales (resto / escritorio)** | `0.9\textwidth` máx (Nota A paso 6, Nota B ampliación) **vs** `width=\linewidth` (Nota A paso 2, Nota B código) | `0.42\textheight` (coinciden Nota A paso 6 y Nota B código/ampliación) | **Siempre** `keepaspectratio`. Regla 8: ninguna página con una sola imagen. |

> **Detalle de las fuentes**  
> - *Nota A (1ª ampliación)*: móvil `height=0.15\textheight`.  
> - *Nota A (2ª ampliación)*: resumen inicial dice «siempre `height=0.42\textheight,keepaspectratio`», pero en detalle: capturas verticales (móvil) `height=0.35\textheight`; resto `height=0.42\textheight`.  
> - *Nota B*: para horizontales «siempre `height=0.42\textheight,keepaspectratio`»; para verticales (móvil) solo fija `width=0.35\textwidth` y remarca que en `subfigure` el `width=\linewidth` equivale a `0.48\textwidth`.  
> - **Código real en ambas notas**: los bloques de ejemplo (genérico y ejemplo concreto de Nota A) usan `height=0.35\textheight,keepaspectratio`; el ejemplo completo de Nota B usa `height=0.42\textheight,keepaspectratio`.

---

### Prosa de TFG (Regla 13)
- Citar en prosa explicando el flujo, nunca con frases sueltas tipo «La figura X muestra…».
- Ejemplo: «Al acceder sin sesión, el usuario ve la página de inicio (Figura~\ref{fig:app-inicio}) y, al registrarse, la validación en cliente muestra errores en línea (Figura~\ref{fig:app-registro}).»
- Las capturas que van juntas se agrupan con `subfigure`.

> **Prosa de TFG, no listas de capturas:** nada de una frase suelta «La figura X muestra…» por cada imagen. Las capturas se explican dentro de párrafos que cuentan qué hace el usuario y por qué la aplicación responde así. Las que van juntas se agrupan con `subfigure`.
> — `memoria/reglas-tfg.md (regla 13) y spec del proyecto`

---

### Ejemplos aplicados (memoria-procesos)
**04-descripcion.tex**:  
`fig:app-inicio-registro`, `fig:app-errores-acceso`, `fig:app-perfil-baja`, `fig:app-admin-full`, `fig:app-responsive`, `fig:app-estados-especiales`, `fig:hito4-flujo`, `fig:hito4-estados-privacidad`

**04b-juego.tex**:  
`fig:juego-menu-vestuario`, `fig:juego-partida-mejora`, `fig:juego-jefe-ambiente`, `fig:juego-fin-pausa`, `fig:juego-club-pantallas-a`, `fig:juego-club-pantallas-b`

---

### Referencias de origen
- `memoria/chapters/04-descripcion.tex` — *Nota A*  
- `spec versión 4 y 04-descripcion.tex / 04b-juego.tex corregidos` — *Nota B*  
- Origen común: [[proyectos/memoria-procesos/estado|memoria-procesos]]

> \begin{subfigure}{0.48\textwidth} \centering \includegraphics[width=\linewidth,height=0.35\textheight,keepaspectratio]{ruta} \subcaption{Texto} \label{fig:sub} \end{subfigure}
> — `memoria/chapters/04-descripcion.tex`

> Las capturas relacionadas van juntas en una figura con subfigure (de subcaption, ya cargado; dos por fila, \begin{subfigure}{0.48\textwidth}), con un caption general y uno por subfigura.
> — `spec versión 4 y 04-descripcion.tex / 04b-juego.tex corregidos`

> \begin{figure}[htbp]\centering\begin{subfigure}{0.48\textwidth}\centering\includegraphics[width=\linewidth,height=0.42\textheight,keepaspectratio]{figs/capturas/app/01-inicio.png}\subcaption{Página de inicio sin sesión.}\label{fig:app-inicio}\end{subfigure}\hfill\begin{subfigure}{0.48\textwidth}\centering\includegraphics[width=\linewidth,height=0.42\textheight,keepaspectratio]{figs/capturas/app/02-registro-validacion.png}\subcaption{Validación en cliente: email y contraseña con errores.}\label{fig:app-registro}\end{subfigure}\caption{Inicio y registro: página pública y validación del formulario.}\label{fig:app-inicio-registro}\end{figure}
> — `chapters/04-descripcion.tex` (cita sin comprobar)

---

### Relacionado
[[prosa-de-tfg-sin-listas-de-capturas-regla-13-javier]] · [[como-agrupar-capturas-con-subfigure-dos-por-fila]] · [[como-agrupar-capturas-con-subfigure-en-latex-para-manuales-d]] · [[como-agrupar-capturas-con-subfigure-dos-por-fila]] · [[agrupar-capturas-con-subfigure]] · [[reescribir-frases-la-figura-x-muestra-como-prosa-integrada]] · [[agrupar-capturas-relacionadas-en-subfiguras-con-prosa-integr]]

Fusionada con: *Cómo agrupar capturas relacionadas con subfigure (2 por fila)* y *Agrupar capturas relacionadas en subfiguras con subcaption (LaTeX)*

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]

> **Prosa de TFG, no listas de capturas:** nada de una frase suelta «La figura X muestra…» por cada imagen. Las capturas se explican dentro de párrafos que cuentan qué hace el usuario y por qué la aplicación responde así. Las que van juntas se agrupan con `subfigure`.
> — `memoria/reglas-tfg.md (regla 13) y spec del proyecto`
> \begin{subfigure}{0.48\textwidth} \centering \includegraphics[width=\linewidth,height=0.35\textheight,keepaspectratio]{ruta} \subcaption{Texto} \label{fig:sub} \end{subfigure}
> — `memoria/chapters/04-descripcion.tex`
> Las capturas relacionadas van juntas en una figura con subfigure (de subcaption, ya cargado; dos por fila, \begin{subfigure}{0.48\textwidth}), con un caption general y uno por subfigura.
> — `spec versión 4 y 04-descripcion.tex / 04b-juego.tex corregidos`
> \begin{subfigure}{0.48\textwidth} ... \subcaption{...} \label{fig:...} \end{subfigure}
> — `memoria/chapters/04-descripcion.tex`
> begin{subfigure}{0.48\textwidth} ... subcaption{...} ... end{subfigure} hfill ... caption{...} label{fig:...}
> — `chapters/04-descripcion.tex, chapters/04b-juego.tex` (cita sin comprobar)
> \begin{figure}[htbp]\centering\begin{subfigure}{0.48\textwidth}\centering\includegraphics[width=\linewidth,height=0.42\textheight,keepaspectratio]{figs/capturas/app/01-inicio.png}\subcaption{Página de inicio sin sesión.}\label{fig:app-inicio}\end{subfigure}\hfill\begin{subfigure}{0.48\textwidth}\centering\includegraphics[width=\linewidth,height=0.42\textheight,keepaspectratio]{figs/capturas/app/02-registro-validacion.png}\subcaption{Validación en cliente: email y contraseña con errores.}\label{fig:app-registro}\end{subfigure}\caption{Inicio y registro: página pública y validación del formulario.}\label{fig:app-inicio-registro}\end{figure}
> — `chapters/04-descripcion.tex` (cita sin comprobar)


> ⚠️ Posible contradicción al fusionar: Dimensiones de imagen contradictorias entre fuentes:  
- **Móvil (vertical) width**: Nota A (paso 6) = `0.35\textwidth`; Nota B (ampliación 2026-11-23) = `width=\linewidth` (≈ `0.48\textwidth` dentro del subfigure).  
- **Móvil height**: Nota A (paso 2) y Nota B (ampliación) = `0.35\textheight`; Nota A (paso 6) y Nota B (código) = `0.42\textheight`.  
- **Escritorio width**: Nota A (paso 6) y Nota B (ampliación) = `0.9\textwidth` máx; Nota A (paso 2) y Nota B (código) = `\linewidth`.  
- **Prefijo de labels**: Nota A sugiere `fig:sub-...` / `fig:general`; Nota B usa `fig:app-*` descriptivos.  
- **Ejemplo concreto**: Nota A usa `height=0.35\textheight`; Nota B (ejemplo completo verificado) usa `height=0.42\textheight`. No hay consenso único para capturas verticales (móvil).

Fusionada con: Agrupar capturas relacionadas en subfiguras con `subcaption` (LaTeX)

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
