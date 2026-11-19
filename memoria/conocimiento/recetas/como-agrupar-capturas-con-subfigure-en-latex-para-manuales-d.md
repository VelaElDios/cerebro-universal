---
tipo: "receta"
titulo: "Cómo agrupar capturas con subfigure en LaTeX para manuales de usuario"
temas: ["figuras", "latex", "maquetacion", "subcaption", "subfigure"]
claves: ["subfigure", "height=0.42\\textheight", "caption general", "subcaption", "agrupación capturas"]
proyectos: ["memoria-procesos"]
fuentes: ["chapters/04-descripcion.tex (cambios aplicados en este paso)", "chapters/04-descripcion.tex", "memoria/reglas-tfg.md"]
confianza: "propuesto"
fecha: "2026-11-16"
actualizado: "2026-11-19"
---

Temas: [[figuras]] · [[latex]] · [[maquetacion]] · [[subcaption]] · [[subfigure]]

Temas: [[latex]] · [[maquetacion]] · [[subcaption]]

**Propósito**  
Evitar páginas con una sola imagen (Regla 8) y cadenas de «La figura X muestra…» (Regla 12), agrupando capturas relacionadas en una figura flotante con subfiguras (paquete `subcaption`, ya cargado en `include/extra.tex`).

**Procedimiento**  
1. Usar el entorno `figure` con especificador de posición `[htbp]`.  
2. Dentro, crear cada subfigura con `\begin{subfigure}{0.48\textwidth}` (dos por fila).  
3. Separar las subfiguras horizontalmente con `\hfill`.  
4. En cada subfigura:  
   - `\centering`  
   - `\includegraphics[width=\linewidth,height=0.42\textheight,keepaspectratio]{ruta/archivo.png}`  
   - **Leyenda individual**: `\subcaption{Texto...}` *o* `\caption{Texto...}` (ver contradicción).  
   - `\label{fig:subfigura-propria}` propio.  
5. En la figura contenedora:  
   - `\caption{Texto general descriptivo.}`  
   - `\label{fig:contenedora}` distinto al de las subfiguras.  
6. En el texto: redactar prosa explicativa que integre las referencias.  
   - Opción A: referenciar la figura general y usar sufijo de letra (`Figura~\ref{fig:contenedora}a`).  
   - Opción B: referenciar subfiguras individuales con `\ref{fig:subfigura}` o `\subref{fig:subfigura}` (requiere opción `subrefformat=parens` al cargar `subcaption`).  
7. Eliminar todas las figuras sueltas y sus frases introductorias.

**Ejemplo completo (dos subfiguras)**
```latex
\begin{figure}[htbp]
\centering
\begin{subfigure}{0.48\textwidth}
  \centering
  \includegraphics[width=\linewidth,height=0.42\textheight,keepaspectratio]{figs/capturas/app/01-inicio.png}
  \subcaption{Página de inicio sin sesión.}
  \label{fig:app-inicio}
\end{subfigure}
\hfill
\begin{subfigure}{0.48\textwidth}
  \centering
  \includegraphics[width=\linewidth,height=0.42\textheight,keepaspectratio]{figs/capturas/app/02-registro-validacion.png}
  \subcaption{Registro con validación de campos.}
  \label{fig:app-registro}
\end{subfigure}
\caption{Pantallas de acceso: inicio y registro.}
\label{fig:app-acceso}
\end{figure}
```

**Ejemplo de integración en prosa**  
> Al acceder a la aplicación sin sesión, el usuario encuentra la página de inicio (Figura~\ref{fig:app-acceso}a) y, tras pulsar «Registrarse», el formulario con validación (Figura~\ref{fig:app-acceso}b).

**Fuentes y trazabilidad**  
- Aplicado en `chapters/04-descripcion.tex` (verificado).  
- Citado en `memoria/reglas-tfg.md` (propuesto, sin comprobar).  
- Ampliaciones 2026-11-16 desde [[proyectos/memoria-procesos/estado|memoria-procesos]].

**Relacionado**  
[[cada-imagen-aparece-una-sola-vez-en-el-capitulo-canonico]] · [[corregir-paginas-con-una-sola-imagen-regla-8]] · [[como-agrupar-capturas-con-subfigure-en-latex-para-manuales-d]] · [[agrupar-capturas-con-subfigure]] · [[como-se-agrupan-capturas-con-subfigure]] · [[como-agrupar-capturas-con-subfigure-en-latex-para-manuales-d]]

> \begin{subfigure}{0.48\textwidth} \centering \includegraphics[width=\linewidth,height=0.42\textheight,keepaspectratio]{figs/capturas/app/01-inicio.png} \subcaption{Página de inicio sin sesión.} \label{fig:app-inicio} \end{subfigure}
> — `chapters/04-descripcion.tex (cambios aplicados en este paso)`
> Las capturas relacionadas van juntas en una figura con `subfigure` (de `subcaption`, ya cargado; dos por fila, `\begin{subfigure}{0.48\textwidth}`), con un caption general y uno por subfigura.
> — `memoria/reglas-tfg.md` (cita sin comprobar)


> ⚠️ Posible contradicción al fusionar: 1. Leyenda de subfigura: Nota A usa `\subcaption{...}`, Nota B usa `\caption{...}` dentro de `subfigure` (ambos funcionan con `subcaption`, pero la orden canónica es `\subcaption`). 2. Estilo de referencia: Nota A sugiere `Figura~\ref{fig:contenedora}a` (etiqueta contenedora + letra), Nota B propone `\ref{fig:subfigura}` o `\subref{fig:subfigura}` (etiquetas propias por subfigura). 3. Nota B añade `[htbp]` al `figure` y `\hfill` entre subfiguras; Nota A no lo especifica. 4. Extensión `.png` explícita en Nota A y en la ampliación de B, pero no en el primer ejemplo de B. 5. Estado de verificación: A = verificado, B = propuesto (cita sin comprobar).

Fusionada con: Cómo agrupar capturas con subfigure en LaTeX

Relacionado: [[arreglar-pagina-con-una-sola-imagen-regla-8-agrupando-en-sub]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
