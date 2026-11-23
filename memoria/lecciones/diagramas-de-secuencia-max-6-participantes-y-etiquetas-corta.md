---
titulo: "Diagramas de secuencia: máx. 6 participantes y etiquetas cortas"
temas: ["latex", "pgf-umlsd", "diagramas-secuencia"]
claves: ["\\newthread", "\\newinst", "\\mess", "call", "sdblock", "participantes"]
estado: "propuesta"
veces: 1
fecha: "2026-11-23"
proyectos: ["memoria-procesos"]
---

Temas: [[latex]] · [[pgf-umlsd]] · [[diagramas-secuencia]]

## Problema
Los diagramas de secuencia con más de 6 participantes o etiquetas largas no caben en el ancho de página sin escalar, lo que reduce el tamaño de fuente por debajo de 7,5 pt (regla 16). Además, etiquetas con acentos, paréntesis, comandos LaTeX o caracteres especiales (#, &, _, $, %) causan errores en revisar_umlsd.py.

## Solución
(1) Limitar a 6 participantes por diagrama; si hay más, agrupar (ej. «Frontend» = Vista + api.js) o dividir en dos diagramas (cliente/servidor). (2) Etiquetas en \mess, call, callself, \newinst: sin acentos, sin paréntesis en \mess, sin comandos LaTeX, sin # & _ $ % sueltos. Usar saltos de línea \n en etiquetas largas. (3) Declarar todos los participantes con \newthread/\newinst antes de usarlos. (4) Usar \resizebox{\textwidth}{!}{...} solo para encoger un poco, no para meter 9 columnas.

## Ejemplo
|
  \begin{sequencediagram}
    \newthread{u}{Usuario}
    \newinst[2]{api}{API}
    \newinst[2]{srv}{Servicio}
    \newinst[2]{bd}{BD}
    \begin{call}{u}{petición}{api}{respuesta}
      \begin{call}{api}{procesa}{srv}{datos}
        \begin{call}{srv}{query}{bd}{filas}
        \end{call}
      \end{call}
    \end{call}
    \begin{sdblock}{alt}{error}
      \mess{api}{400 error}{u}
    \end{sdblock}
  \end{sequencediagram}

Origen: [[proyectos/memoria-procesos/bitacora|memoria-procesos]]
