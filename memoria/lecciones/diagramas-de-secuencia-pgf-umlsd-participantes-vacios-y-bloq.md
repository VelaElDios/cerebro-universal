---
titulo: "Diagramas de secuencia pgf-umlsd: participantes vacíos y bloques vacíos rompen la compilación"
temas: ["latex", "pgf-umlsd", "diagramas-secuencia"]
claves: ["el participante «» no está declarado", "\\newinst", "\\mess", "sdblock"]
estado: "propuesta"
veces: 1
fecha: "2026-11-19"
proyectos: ["memoria-procesos"]
---

Temas: [[latex]] · [[pgf-umlsd]] · [[diagramas-secuencia]]

## Problema
Al reescribir diagramas de secuencia, el constructor dejó instancias \newinst sin nombre (participante vacío) y bloques \mess{} vacíos, lo que hace fallar a revisar_umlsd.py y a LaTeX con "el participante «» no está declarado".

## Solución
En pgf-umlsd, cada \newthread/\newinst debe tener un nombre no vacío entre llaves. No se pueden usar \mess{} ni \call{} con participantes no declarados. Los bloques sdblock vacíos (solo \mess{a}{}{a}) se eliminan. Antes de compilar, pasar revisar_umlsd.py que valida la sintaxis completa.

## Ejemplo
|
  \begin{sequencediagram}
    \newthread{u}{Usuario}
    \newinst[2]{api}{API}
    \begin{call}{u}{petición}{api}{respuesta}
    \end{call}
    \begin{sdblock}{alt}{caso error}
      \mess{api}{400 error}{u}
    \end{sdblock}
  \end{sequencediagram}

Origen: [[proyectos/memoria-procesos/bitacora|memoria-procesos]]
