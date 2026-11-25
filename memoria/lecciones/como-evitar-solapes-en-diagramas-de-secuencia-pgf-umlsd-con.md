---
titulo: "Cómo evitar solapes en diagramas de secuencia pgf-umlsd con bloques alt"
temas: ["latex", "tikz", "pgf-umlsd"]
claves: ["sdblock", "alt", "flechas", "línea divisoria", "solape"]
estado: "propuesta"
veces: 1
fecha: "2026-11-25"
proyectos: ["memoria-procesos"]
---

Temas: [[latex]] · [[tikz]] · [[pgf-umlsd]]

## Problema
El bloque `alt` dibuja una línea horizontal divisoria que puede cortar la zona de interacción (llamadas `call` o `mess`) si no hay suficiente espacio vertical entre el final de la llamada anidada y el inicio del bloque. Además, las flechas (`mess`) dentro del bloque pueden cruzar los bordes del marco `alt` si el espacio es insuficiente.

## Solución
Insertar un mensaje vacío (`\mess{participante}{ }{otro}`) justo antes del primer `sdblock` para forzar un salto vertical. Aumentar la distancia entre instancias (`\newinst[4]...`) si el solape es horizontal. Evitar anidar `sdblock` dentro de `call`; colocar los bloques `alt` después de cerrar todas las llamadas. Comprobar visualmente en el PDF y, si persiste, dividir en dos diagramas (flujo normal y flujo de error).

## Ejemplo
|
  \begin{sequencediagram}
    \newthread{u}{Usuario}
    \newinst[3]{api}{API}
    \newinst[3]{srv}{Servicio}
    \begin{call}{u}{petición}{api}{respuesta}
      \begin{call}{api}{procesar}{srv}{ok}
      \end{call}
    \end{call}
    \mess{api}{ }{srv}  % espacio vertical
    \begin{sdblock}{alt}{error}
      \mess{srv}{Error}{api}
    \end{sdblock}
    \begin{sdblock}{else}{éxito}
      \mess{srv}{OK}{api}
    \end{sdblock}
  \end{sequencediagram}

Origen: [[proyectos/memoria-procesos/bitacora|memoria-procesos]]
