---
tipo: "receta"
titulo: "Cómo agrupar capturas relacionadas con subfigure (dos por fila)"
temas: ["capturas", "figuras", "latex", "maquetacion", "memoria-procesos", "subcaption"]
claves: ["subfigure", "0.48\\textwidth", "caption general", "caption individual", "subcaption", "cludegraphics", "width", "height", "keepaspectratio", "agrupación", "capturas"]
proyectos: ["memoria-procesos"]
fuentes: ["memoria/chapters/04-descripcion.tex", "memoria/reglas-tfg.md", "memoria/reglas-tfg.md (regla 13) y spec del proyecto", "chapters/04-descripcion.tex (ejemplo real compilado)", "memoria/chapters/04-descripcion.tex (fig:app-inicio-registro, fig:app-errores-acceso, fig:app-perfil-baja, fig:app-admin-full, fig:app-responsive, fig:app-estados-especiales, fig:hito4-flujo, fig:hito4-estados-privacidad)", "spec versión 4 y 04-descripcion.tex / 04b-juego.tex corregidos"]
confianza: "propuesto"
fecha: "2026-11-23"
actualizado: "2026-11-24"
---

Temas: [[capturas]] · [[figuras]] · [[latex]] · [[maquetacion]] · [[memoria-procesos]] · [[subcaption]]

Temas: [[capturas]] · [[figuras]] · [[latex]] · [[maquetacion]] · [[subcaption]] · [[memoria-procesos]]

---

### Propósito
Evitar cadenas de «La figura X muestra…» agrupando capturas relacionadas en una sola figura con `subfigure` (paquete `subcaption`, ya cargado), dos por fila, con un `\caption` general y un `\subcaption` por subfigura. Cada subfigura lleva su `\label` y se cita con `\ref` / `\subref` en la prosa que explica el flujo de usuario.

---

### Plantilla obligatoria (2 capturas relacionadas, disposición horizontal)
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

**Ejemplo concreto (memoria-procesos, 2026-11-23)**
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

**En la prosa**  
Referenciar la figura general (`Figura~\ref{fig:etiqueta-general}`) y/o las subfiguras (`subfigura~\ref{fig:etiqueta1}`) dentro de la explicación del flujo.

---

### Reglas de maquetación
- **Dos por fila**: `0.48\textwidth` + `\hfill`.
- **Caption general** (`\caption`) y uno por subfigura (`\subcaption`).
- **Cada subfigura con su `\label`** para citar con `\ref` o `\subref`.
- **Verticales (móvil)**: `width=0.35\textwidth`; el resto `width=0.9\textwidth` máx.
- **Regla 8**: ninguna página con una sola imagen; si una figura queda sola, reducir height o agrupar.

---

### Parámetros de imagen (resumen consolidado)

| Contexto | `width` en `\includegraphics` | `height` en `\includegraphics` | Notas |
|---|---|---|---|
| **Verticales (móvil)** | `0.35\textwidth` | **Ver contradicciones** | En `subfigure` usar `width=\linewidth` (respeta el `0.48\textwidth` del contenedor). |
| **Horizontales (resto)** | `0.9\textwidth` máx. | `0.42\textheight` | **Siempre** `keepaspectratio`. Regla 8: ninguna página con una sola imagen. |

> **Detalle de las fuentes**  
> - *Nota A (1ª ampliación)*: móvil `height=0.15\textheight`.  
> - *Nota A (2ª ampliación)*: «siempre `height=0.42\textheight,keepaspectratio`» en el resumen inicial, pero luego especifica: «capturas verticales (móvil) usan `height=0.35\textheight`; el resto `height=0.42\textheight`».  
> - *Nota B*: para horizontales «siempre `height=0.42\textheight,keepaspectratio`»; para verticales (móvil) solo fija `width=0.35\textwidth` y remarca que en `subfigure` el `width=\linewidth` equivale a `0.48\textwidth`.  
> - **Código real en ambas notas**: los bloques de ejemplo usan `height=0.35\textheight,keepaspectratio`.

---

### Prosa de TFG (Regla 13)
- Citar en prosa explicando el flujo, nunca con frases sueltas tipo «La figura X muestra…».
- Ejemplo: «Al acceder sin sesión, el usuario ve la página de inicio (Figura~\ref{fig:app-inicio}) y, al registrarse, la validación en cliente muestra errores en línea (Figura~\ref{fig:app-registro}).»
- Las capturas que van juntas se agrupan con `subfigure`.

> **Prosa de TFG, no listas de capturas:** nada de una frase suelta «La figura X muestra…» por cada imagen. Las capturas se explican dentro de párrafos que cuentan qué hace el usuario y por qué la aplicación responde así. Las que van juntas se agrupan con `subfigure`.
> — `memoria/reglas-tfg.md (regla 13) y spec del proyecto` (cita sin comprobar)

---

### Ejemplos aplicados (memoria-procesos)
**04-descripcion.tex**:  
`fig:app-inicio-registro`, `fig:app-errores-acceso`, `fig:app-perfil-baja`, `fig:app-admin-full`, `fig:app-responsive`, `fig:app-estados-especiales`, `fig:hito4-flujo`, `fig:hito4-estados-privacidad`

**04b-juego.tex**:  
`fig:juego-menu-vestuario`, `fig:juego-partida-mejora`, `fig:juego-jefe-ambiente`, `fig:juego-fin-pausa`, `fig:juego-club-pantallas-a`, `fig:juego-club-pantallas-b`

---

### Referencias de origen
- `memoria/chapters/04-descripcion.tex` (cita sin comprobar) — *Nota A*  
- `spec versión 4 y 04-descripcion.tex / 04b-juego.tex corregidos` (cita sin comprobar) — *Nota B*  
- Origen común: [[proyectos/memoria-procesos/estado|memoria-procesos]]

> \begin{subfigure}{0.48\textwidth} \centering \includegraphics[width=\linewidth,height=0.35\textheight,keepaspectratio]{ruta} \subcaption{Texto} \label{fig:sub} \end{subfigure}
> — `memoria/chapters/04-descripcion.tex` (cita sin comprobar)

> Las capturas relacionadas van juntas en una figura con subfigure (de subcaption, ya cargado; dos por fila, \begin{subfigure}{0.48\textwidth}), con un caption general y uno por subfigura.
> — `spec versión 4 y 04-descripcion.tex / 04b-juego.tex corregidos` (cita sin comprobar)

---

### Relacionado
[[prosa-de-tfg-sin-listas-de-capturas-regla-13-javier]] · [[como-agrupar-capturas-con-subfigure-dos-por-fila]] · [[como-agrupar-capturas-con-subfigure-en-latex-para-manuales-d]] · [[como-se-agrupan-capturas-con-subfigure]]

Relacionado: [[agrupar-capturas-relacionadas-en-subfiguras-con-prosa-integr]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]

> \begin{subfigure}{0.48\textwidth} \centering \includegraphics[width=\linewidth,height=0.35\textheight,keepaspectratio]{ruta} \subcaption{Texto} \label{fig:sub} \end{subfigure}
> — `memoria/chapters/04-descripcion.tex` (cita sin comprobar)
> **Prosa de TFG, no listas de capturas:** nada de una frase suelta «La figura X muestra…» por cada imagen. Las capturas se explican dentro de párrafos que cuentan qué hace el usuario y por qué la aplicación responde así. Las que van juntas se agrupan con `subfigure`.
> — `memoria/reglas-tfg.md (regla 13) y spec del proyecto` (cita sin comprobar)
> \begin{subfigure}{0.48\textwidth} ... \subcaption{...} \label{fig:...} \end{subfigure}
> — `memoria/chapters/04-descripcion.tex` (cita sin comprobar)
> Las capturas relacionadas van juntas en una figura con subfigure (de subcaption, ya cargado; dos por fila, \begin{subfigure}{0.48\textwidth}), con un caption general y uno por subfigura.
> — `spec versión 4 y 04-descripcion.tex / 04b-juego.tex corregidos` (cita sin comprobar)


> ⚠️ Posible contradicción al fusionar: Altura (`height`) en `\includegraphics`: los bloques de código (genérico y ejemplo concreto) usan `height=0.35\textheight,keepaspectratio`; la regla textual de Nota A dice `height=0.42\textheight,keepaspectratio`; Nota A (1ª ampliación) fija móvil en `0.15\textheight`; Nota A (2ª ampliación) dice en resumen «siempre 0.42» pero en detalle móvil `0.35` y resto `0.42`; Nota B tabla pone horizontales `0.42` y móvil «Ver contradicciones» (solo fija `width=0.35\textwidth`). No hay consenso único para capturas verticales (móvil).

Fusionada con: Cómo agrupar capturas relacionadas con subfigure (2 por fila)

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
