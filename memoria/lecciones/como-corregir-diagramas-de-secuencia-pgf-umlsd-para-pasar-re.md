---
titulo: "Cómo corregir diagramas de secuencia pgf-umlsd para pasar revisar_maquetacion.py"
temas: ["latex", "tikz", "pgf-umlsd", "maquetacion"]
claves: ["revisar_maquetacion.py", "reglas 16-18", "flechas cruzan cajas", "etiquetas superpuestas", "participantes vacíos"]
estado: "propuesta"
veces: 1
fecha: "2026-11-19"
proyectos: ["memoria-procesos"]
---

Temas: [[latex]] · [[tikz]] · [[pgf-umlsd]] · [[maquetacion]]

## Problema
Los diagramas de secuencia en pgf-umlsd fallan la revisión visual (reglas 16-18 de Javier) cuando: (1) las flechas atraviesan cajas en lugar de ir de caja en caja con codos (|- / -|), (2) las etiquetas de flechas se superponen a cajas o líneas verticales, (3) los nodos están demasiado juntos (node distance insuficiente), (4) hay más de 6 participantes, (5) hay participantes declarados con nombre vacío (\newinst{}{...}).

## Solución
Antes de compilar, revisar cada diagrama: (a) aumentar node distance vertical ≥ 1.5cm y horizontal ≥ 2.5cm; (b) usar flechas con codos: \draw[arrow] (A.east) -- ++(1.5,0) |- (B.west); (c) mover etiquetas con node[near start, above/left/right, font=\footnotesize] {texto} fuera de líneas verticales; (d) agrupar participantes relacionados (ej. "Vista + api.js" → "Frontend") si hay >6; (e) verificar que cada \newthread/\newinst tiene nombre no vacío; (f) compilar y abrir el PDF para comprobar visualmente que no hay cruces y las letras se leen (≥ 8pt).

## Ejemplo
|
  \begin{sequencediagram}
    \newthread{u}{Usuario}
    \newinst[2]{fe}{Frontend}
    \newinst[2]{api}{API}
    \newinst[2]{srv}{Servicio}
    \begin{call}{u}{petición}{fe}{ok}
    \end{call}
    \begin{call}{fe}{POST}{api}{200}
      \begin{call}{api}{procesar}{srv}{resultado}
      \end{call}
    \end{call}
    \begin{sdblock}{alt}{error}
      \mess{api}{400 error}{fe}
    \end{sdblock}
  \end{sequencediagram}

Origen: [[proyectos/memoria-procesos/bitacora|memoria-procesos]]
