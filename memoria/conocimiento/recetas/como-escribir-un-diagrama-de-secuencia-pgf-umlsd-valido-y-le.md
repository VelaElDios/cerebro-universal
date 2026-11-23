---
tipo: "receta"
titulo: "Cómo escribir un diagrama de secuencia pgf-umlsd válido y legible"
temas: ["latex", "pgf-umlsd", "sequencediagram"]
claves: ["\\newthread", "\\newinst", "call", "\\mess", "sdblock", "adjustbox"]
proyectos: ["memoria-procesos"]
fuentes: ["memoria/reglas-tfg.md (ejemplo en spec)"]
confianza: "propuesto"
fecha: "2026-11-23"
actualizado: "2026-11-23"
---

Temas: [[latex]] · [[pgf-umlsd]] · [[sequencediagram]]

|
  Reglas obligatorias para sequencediagram:
  1. Entorno `sequencediagram` (minúsculas). No existe `sequenceDiagram` ni entorno `alt`; para alternativas usar `sdblock`.
  2. Participantes: `\newthread{id}{Nombre}` o `\newinst[desplazamiento]{id}{Nombre}`. Máximo 6 participantes por diagrama.
  3. Llamadas anidadas: `\begin{call}{origen}{mensaje}{destino}{respuesta} ... \end{call}`.
  4. Mensajes sueltos: `\mess{origen}{mensaje}{destino}`. Sin paréntesis en el mensaje.
  5. Bloques alternativos: `\begin{sdblock}{condición}{etiqueta} ... \end{sdblock}`.
  6. Textos: sin `#`, `&`, `_`, `$`, `%`, `{`, `}`, `\`, comandos LaTeX. Usar `\mbox{}` para palabras compuestas. Sin acentos en etiquetas cortas.
  7. Envolver en `adjustbox{max width=\textwidth, max totalheight=0.6\textheight}` para que no se salga de página.
  8. Fuente `\scriptsize` o `\footnotesize` en todo el diagrama.
  9. Flechas con codos implícitos (pgf-umlsd los gestiona); separar participantes con `node distance` suficiente.

  Ejemplo mínimo correcto:
  ```latex
  \begin{figure}[htbp]
  \centering
  \begin{adjustbox}{max width=\textwidth, max totalheight=0.6\textheight}
  \begin{sequencediagram}
    \newthread{u}{Usuario}
    \newinst[2]{api}{API}
    \newinst[2]{srv}{Servicio}
    \begin{call}{u}{peticion}{api}{ok}
      \begin{call}{api}{procesa}{srv}{resultado}
      \end{call}
    \end{call}
    \begin{sdblock}{alt}{error}
      \mess{api}{400}{u}
    \end{sdblock}
  \end{sequencediagram}
  \end{adjustbox}
  \caption{Ejemplo válido.}
  \label{fig:ejemplo-seq}
  \end{figure}
  ```

> En los textos de `\mess`, `call`, `callself` y `\newinst` no puede ir `\#`, `\_`, `\&`, `\%`, `\$`, `\{`, `\}`, ningún comando (`\texttt`…) ni `#`, `&`, `_`, `$` sueltos, y en `\mess` tampoco paréntesis. Todo participante que se use tiene que estar declarado con `\newthread`/`\newinst` en ese diagrama.
> — `memoria/reglas-tfg.md (ejemplo en spec)` (cita sin comprobar)

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
