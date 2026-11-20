---
tipo: "receta"
titulo: "Diagramas de secuencia con pgf-umlsd (sequencediagram)"
temas: ["diagramas", "diagramas-secuencia", "latex", "pgf-umlsd", "secuencia", "tikz"]
claves: ["sequencediagram", "newthread", "newinst", "call", "mess", "sdblock"]
proyectos: ["memoria-procesos"]
fuentes: ["chapters/04-descripcion.tex", "spec del proyecto (bloque «Cómo se escribe un diagrama de secuencia»)", "memoria/reglas-tfg.md (ejemplo en spec)"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-20"
---

Temas: [[diagramas]] · [[diagramas-secuencia]] · [[latex]] · [[pgf-umlsd]] · [[secuencia]] · [[tikz]]

Temas: [[latex]] · [[pgf-umlsd]] · [[secuencia]] · [[tikz]] · [[diagramas]]

## Reglas obligatorias para que compile y pase `revisar_umlsd.py`

1. **Entorno**: `sequencediagram` (minúsculas; no existen `sequenceDiagram` ni un entorno `alt`).
2. **Participantes**:
   - `\newthread{id}{Nombre}`
   - `\newinst[dist]{id}{Nombre}` (distancia opcional)
3. **Llamadas anidadas**:
   ```latex
   \begin{call}{origen}{mensaje}{destino}{respuesta}
     ...
   \end{call}
   ```
4. **Mensajes simples**: `\mess{origen}{mensaje}{destino}`
5. **Bloques alternativos** (equivalente a `alt`):
   ```latex
   \begin{sdblock}{alt}{condición}
     ...
   \end{sdblock}
   ```
6. **Caracteres y comandos prohibidos** en los textos de `\mess`, `call`, `callself` y `\newinst`:
   - Versiones con barra invertida: `\#`, `\_`, `\&`, `\%`, `\$`, `\{`, `\}`
   - Versiones sueltas: `#`, `&`, `_`, `$` (Nota A añade también `%`, `{`, `}` sueltos)
   - Comandos LaTeX (p.ej. `\texttt{...}`)
   - **En `\mess` además**: paréntesis `(` `)`
7. **Declaración de participantes**: todo participante usado debe estar declarado en ese diagrama.
8. **Diagramas anchos**: envolver en `\resizebox{\textwidth}{!}{% ... %}`
9. **Diagramas altos**: usar `\begin{adjustbox}{max width=\textwidth,max totalheight=0.6\textheight} ... \end{adjustbox}`
10. **Códigos de estado HTTP**: usar los exactos de la doc técnica (ej. `400`, no `422`).

## Ejemplo (cita sin comprobar — `chapters/04-descripcion.tex`)

```latex
\begin{sequencediagram}
  \newthread{u}{Usuario}
  \newinst[2]{v}{Vista registro}
  \begin{call}{u}{escribe email y contraseña}{v}{ok}
  \end{call}
  \begin{sdblock}{alt}{ya existe}
    \mess{s}{409 ConflictError}{a}
  \end{sdblock}
\end{sequencediagram}
```

## Citas de referencia

- **Especificación del proyecto** (bloque «Cómo se escribe un diagrama de secuencia») — cita sin comprobar:
  > El entorno es sequencediagram (en minúsculas; no existen sequenceDiagram ni un entorno alt: para alternativas, sdblock). Participantes con \newthread/\newinst, llamadas anidadas con call (origen, mensaje, destino, respuesta), mensajes sueltos con \mess y bloques alternativos con sdblock.

- **Ampliación (2026-11-16, memoria-procesos)**:
  Entorno sequencediagram (minúsculas). Participantes con \newthread/\newinst. Llamadas anidadas con call (origen, mensaje, destino, respuesta). Mensajes sueltos con \mess. Bloques alternativos con sdblock. En textos de \mess, call, callself, \newinst: no \#, \_, \&, \%, \$, \{, \}, comandos (\texttt...), ni #, &, _, $ sueltos; en \mess tampoco paréntesis. Todo participante usado debe estar declarado en ese diagrama. Usar \resizebox{\textwidth}{!}{...} para que no se salgan; si ocupan casi una página, adjustbox con max totalheight=0.6\textheight.

## Relacionados

[[diagramas-de-secuencia-con-pgf-umlsd]] · [[diagramas-de-secuencia-con-pgf-umlsd-sequencediagram]] · [[diagramas-de-secuencia-con-pgf-umlsd-sequencediagram]] · [[numeros-en-diagramas-de-secuencia-deben-coincidir-con-la-esp]]

Relacionado: [[diagramas-de-secuencia-pgf-umlsd-sintaxis-correcta]] · [[como-corregir-diagramas-de-secuencia-pgf-umlsd-para-pasar-re]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]

> \begin{sequencediagram} \newthread{u}{Usuario} \newinst[2]{v}{Vista registro} \begin{call}{u}{escribe email y contraseña}{v}{ok} \end{call} \begin{sdblock}{alt}{ya existe} \mess{s}{409 ConflictError}{a} \end{sdblock} \end{sequencediagram}
> — `chapters/04-descripcion.tex` (cita sin comprobar)
> El entorno es sequencediagram (en minúsculas; no existen sequenceDiagram ni un entorno alt: para alternativas, sdblock). Participantes con \newthread/\newinst, llamadas anidadas con call (origen, mensaje, destino, respuesta), mensajes sueltos con \mess y bloques alternativos con sdblock.
> — `spec del proyecto (bloque «Cómo se escribe un diagrama de secuencia»)` (cita sin comprobar)

Fusionada con: Escribir diagramas de secuencia con pgf-umlsd (sequencediagram)

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
