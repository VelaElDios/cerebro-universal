---
tipo: "receta"
titulo: "Prosa de TFG vs lista de capturas (regla 13 Javier)"
temas: ["capturas", "latex", "redaccion", "subfigure"]
claves: ["La figura X muestra", "subfigure", "adjustbox", "prosa continua"]
proyectos: ["memoria-procesos"]
fuentes: ["memoria/reglas-tfg.md"]
confianza: "propuesto"
fecha: "2026-11-19"
actualizado: "2026-11-19"
---

Temas: [[capturas]] · [[latex]] · [[redaccion]] · [[subfigure]]

|
  **Mal (lista de capturas):**
  > La figura 1 muestra la página de inicio. La figura 2 muestra el formulario de registro. La figura 3 muestra el error de contraseña.
  
  **Bien (prosa integrada con subfigure):**
  > Al acceder a la aplicación sin sesión, el usuario encuentra la página de inicio (Figura~\ref{fig:app-inicio-registro}), que presenta dos accesos directos: «Crear cuenta para jugar» y «Ya tengo cuenta». Si elige registrarse, el formulario valida el email y la contraseña en cliente y muestra los errores en línea (subfigura~\ref{fig:app-registro}). Al enviar, el servidor comprueba unicidad del email; si ya existe, devuelve 409 y la interfaz muestra el error sin recargar.
  
  **Reglas para agrupar capturas:**
  1. Capturas relacionadas (mismo flujo, misma pantalla en distintos estados) → una sola `figure` con `subfigure` (dos por fila: `0.48\textwidth`).
  2. Caption general en la `figure` + caption específico en cada `subfigure`.
  3. Referenciar en el texto con `\ref{fig:general}` o `\subref{fig:sub}`.
  4. Verticales (móvil): `width=\linewidth,height=0.35\textheight,keepaspectratio`; horizontales: `width=\linewidth,height=0.42\textheight,keepaspectratio`.
  5. Si la figura resultante queda muy alta, envolver en `adjustbox{max totalheight=0.42\textheight,width=\linewidth}`.
  
  **Plantilla subfigure:**
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

> Prosa de TFG, no listas de capturas: nada de una frase suelta «La figura X muestra…» por cada imagen. Las capturas se explican dentro de párrafos que cuentan qué hace el usuario y por qué la aplicación responde así. Las que van juntas se agrupan con subfigure.
> — `memoria/reglas-tfg.md` (cita sin comprobar)

Relacionado: [[como-agrupar-capturas-relacionadas-con-subfigure-en-latex]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
