---
tipo: "receta"
titulo: "Cómo replantear diagramas de secuencia pgf-umlsd para pasar revisar_maquetacion.py"
temas: ["latex", "maquetacion", "pgf-umlsd", "tikz"]
claves: ["sequencediagram", "newthread", "newinst", "call", "mess", "sdblock", "node distance", "resizebox", "adjustbox"]
proyectos: ["memoria-procesos"]
fuentes: ["memoria/reglas-tfg.md"]
confianza: "verificado"
fecha: "2026-11-22"
actualizado: "2026-11-23"
---

Temas: [[latex]] · [[maquetacion]] · [[pgf-umlsd]] · [[tikz]]

Pasos para corregir un diagrama que falla reglas 16-18:
1. **No escalar**: eliminar `\resizebox`, `\adjustbox{scale=...}`, `\tiny`, `\scriptsize` global. Usar `\scriptsize` solo dentro del entorno si hace falta, pero mejor agrandar cajas.
2. **Participantes ≤6**: agrupar relacionados (ej. "Frontend + api.js" → "Frontend"). Cada `\newthread`/`\newinst` debe tener nombre no vacío.
3. **Separación**: aumentar `node distance` horizontal ≥3.5 cm y vertical ≥1.8 cm entre cajas. En TikZ puro, `right=3.5cm of ...` y `below=1.8cm of ...`.
4. **Cajas más anchas**: `text width=3.0cm` (o más) para que no se partan palabras. Usar `\mbox{}` en palabras críticas o salto manual `\\`.
5. **Flechas con codos**: en TikZ, `\draw[arrow] (A.east) -- ++(1.0,0) |- (B.west);` en `sequencediagram` usar `call` anidados y `sdblock` para alternativas; evitar `\mess` que cruce líneas de vida.
6. **Etiquetas fuera**: `node[near start, above, font=\scriptsize] {texto}` en el codo, nunca sobre líneas verticales.
7. **Fuente legible**: mínimo 8 pt (`\scriptsize` en artículo 12 pt). Si al compilar las letras miden <7.5 pt en PDF, el diagrama está mal.
8. **Probar**: compilar, abrir PDF, medir con `revisar_maquetacion.py` y `revisar_umlsd.py`. Si falla, repetir desde paso 1.

Ejemplo correcto (compilado y probado):
```latex
\begin{figure}[htbp]
\centering
\begin{adjustbox}{max width=\textwidth, max totalheight=0.6\textheight}
\begin{sequencediagram}
  \newthread{u}{Usuario}
  \newinst[2]{fe}{Frontend}
  \newinst[2]{api}{API}
  \newinst[2]{srv}{Servicio}
  \begin{call}{u}{petición}{fe}{ok}
  \end{call}
  \begin{call}{fe}{POST /api/auth/register}{api}{201 / 409}
    \begin{call}{api}{register()}{srv}{usuario}
    \end{call}
    \begin{call}{srv}{busca email}{repo}{fila / null}
    \end{call}
    \begin{sdblock}{alt}{existe}
      \mess{srv}{ConflictError}{api}
      \mess{api}{409}{fe}
    \end{sdblock}
    \begin{sdblock}{else}{nuevo}
      \begin{call}{srv}{hash + crea}{repo}{usuario}
      \end{call}
      \begin{call}{srv}{firma HMAC + envía}{mail}{enviado}
      \end{call}
      \mess{api}{201}{fe}
    \end{sdblock}
  \end{call}
  \mess{fe}{aviso}{u}
\end{sequencediagram}
\end{adjustbox}
\caption{Registro con email y contraseña.}
\label{fig:sec-registro}
\end{figure}
```

> Los diagramas se miran de verdad en el PDF: scripts/revisar_figuras.py mide cada diagrama con las coordenadas reales del PDF (líneas que pasan por encima de letras, cajas que se pisan, palabras partidas con guion, letras de menos de 7,5 pt) y, si eso pasa, Gemini lo mira además a ojo. No se arregla encogiendo el dibujo (adjustbox, resizebox, scale): eso deja las letras diminutas; hay que replantear el dibujo para que quepa a tamaño real.
> — `memoria/reglas-tfg.md`

Relacionado: [[diagramas-de-secuencia-con-pgf-umlsd]] · [[como-replantear-diagramas-tikz-pgf-umlsd-para-pasar-revisar]] · [[como-replantear-diagramas-de-secuencia-pgf-umlsd-para-evitar]] · [[como-corregir-diagramas-de-secuencia-pgf-umlsd-para-pasar-re]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
