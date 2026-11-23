---
titulo: "Cómo corregir diagramas de secuencia pgf-umlsd que desbordan o tienen cruces"
temas: ["latex", "pgf-umlsd", "diagramas-secuencia"]
claves: ["revisar_umlsd.py", "adjustbox", "resizebox", "node distance", "etiquetas"]
estado: "propuesta"
veces: 1
fecha: "2026-11-23"
proyectos: ["memoria-procesos"]
---

Temas: [[latex]] · [[pgf-umlsd]] · [[diagramas-secuencia]]

## Problema
Los diagramas de secuencia con `adjustbox`/`resizebox` escalan el dibujo y reducen el tamaño de fuente por debajo de 7,5 pt (regla 16). Etiquetas con acentos, paréntesis en `\mess`, comandos LaTeX o caracteres especiales (#, &, _, $, %) causan errores en `revisar_umlsd.py`. Flechas que cruzan cajas o textos violan regla 17.

## Solución
(1) Eliminar `adjustbox`/`resizebox`. (2) Aumentar separación horizontal con `\newinst[4]` o más (o `\newthread[4]`). (3) Acortar etiquetas: sin acentos, sin paréntesis en `\mess`, usar `\n` para saltos de línea. (4) Declarar todos los participantes antes de usarlos. (5) Usar `sdblock` para alternativas, no `alt` como entorno. (6) Si >6 participantes, agrupar o dividir en dos diagramas. (7) Verificar con `revisar_umlsd.py` antes de compilar.

## Ejemplo
|
  \begin{sequencediagram}
    \newthread{u}{Usuario}
    \newinst[4]{api}{API}
    \newinst[4]{srv}{Servicio}
    \begin{call}{u}{peticion}{api}{respuesta}
      \begin{call}{api}{procesa}{srv}{datos}
      \end{call}
    \end{call}
    \begin{sdblock}{alt}{error}
      \mess{api}{400 error}{u}
    \end{sdblock}
  \end{sequencediagram}

Origen: [[proyectos/memoria-procesos/bitacora|memoria-procesos]]
