---
tipo: "receta"
titulo: "Cómo corregir diagramas de secuencia pgf-umlsd para pasar reglas 16-18 de Javier"
temas: ["diagramas-secuencia", "latex", "maquetacion", "pgf-umlsd", "diagramas"]
claves: ["\\newthread", "\\newinst", "call", "\\mess", "sdblock", "adjustbox", "max totalheight"]
proyectos: ["memoria-procesos"]
fuentes: ["memoria/reglas-tfg.md"]
confianza: "propuesto"
fecha: "2026-11-19"
actualizado: "2026-11-19"
---

Temas: [[diagramas-secuencia]] · [[latex]] · [[maquetacion]] · [[pgf-umlsd]]

|
  Reglas obligatorias para diagramas de secuencia en esta plantilla:
  
  1. **Máximo 6 participantes** por diagrama. Si hay más, agrupar (ej. "Vista + api.js" → "Frontend") o dividir en dos diagramas (cliente / servidor).
  
  2. **Separación suficiente**: `node distance` vertical ≥ 1.5cm, horizontal ≥ 2.5cm entre columnas. Usar `\newinst[2]` para añadir espacio extra.
  
  3. **Flechas con codos** para evitar cruzar cajas: en TikZ usar `|-` y `-|`; en pgf-umlsd las flechas son automáticas pero se controla con la posición de los participantes.
  
  4. **Etiquetas fuera de líneas verticales**: no poner texto de \mess/\call sobre la línea vertical de un lifeline. Mover el participante o usar `callself` para llamadas internas.
  
  5. **Sin participantes vacíos**: cada `\newthread{name}{Label}` y `\newinst[n]{name}{Label}` debe tener `name` no vacío.
  
  6. **Sin bloques vacíos**: eliminar `\mess{a}{}{a}` y `sdblock` que solo contienen mensajes vacíos.
  
  7. **Escalado controlado**: envolver en `\begin{adjustbox}{max width=\textwidth, max totalheight=0.6\textheight}` y dentro `\resizebox{\textwidth}{!}{...}` solo si cabe. Si las letras quedan < 8pt, rediseñar el diagrama.
  
  8. **Validar antes de compilar**: ejecutar `scripts/revisar_umlsd.py` que comprueba:
     - Todos los participantes declarados
     - Sin caracteres prohibidos en mensajes (#, &, _, $, %, {, }, \, paréntesis en \mess)
     - Sintaxis correcta de call/sdblock
  
  Ejemplo correcto (del spec):
  ```latex
  \begin{figure}[htbp]
  \centering
  \resizebox{\textwidth}{!}{%
  \begin{sequencediagram}
    \newthread{nav}{Navegador}
    \newinst[2]{api}{API (Express)}
    \newinst[2]{srv}{userService}
    \newinst[2]{bd}{PostgreSQL}
    \begin{call}{nav}{POST /api/auth/login}{api}{200 o 401}
      \begin{call}{api}{authenticate(email, contraseña)}{srv}{usuario}
        \begin{call}{srv}{SELECT por email}{bd}{fila}
        \end{call}
      \end{call}
    \end{call}
    \begin{sdblock}{alt}{cuenta pendiente}
      \mess{api}{403 + enlace de reenvío}{nav}
    \end{sdblock}
  \end{sequencediagram}}
  \caption{Inicio de sesión local.}
  \label{fig:sec-login}
  \end{figure}
  ```

> Diagramas de secuencia: como mucho 6 participantes. Si hay más, se agrupan o se parte en dos diagramas. \resizebox solo para encoger un poco, no para meter 9 columnas en el ancho de la página.
> — `memoria/reglas-tfg.md` (cita sin comprobar)

Relacionado: [[diagramas-de-secuencia-pgf-umlsd-sintaxis-correcta]] · [[como-evitar-cruces-en-diagramas-tikz-pgf-umlsd]]

## Ampliación (2026-11-19, memoria-procesos)
|
  Pasos para arreglar un diagrama que falla en revisar_maquetacion.py (Gemini):
  1. Contar participantes: si hay más de 6, agrupar (ej. "Frontend" = Vista + api.js) o dividir en dos diagramas (cliente / servidor).
  2. Aumentar `node distance` vertical (≥1.5cm) y horizontal (≥2.5cm) en las opciones de `sequencediagram` o con `\begin{sequencediagram}[node distance=...]`.
  3. Usar flechas con codos (`|-` o `-|`) para evitar cruzar cajas: en TikZ dentro del diagrama no se puede, pero en `sequencediagram` las flechas son rectas; si hace falta rodear, separar más los participantes.
  4. Mover etiquetas de `\mess` y `call` lejos de líneas verticales: añadir espacios o reordenar llamadas.
  5. Reducir tamaño de fuente en nodos y etiquetas con `font=\footnotesize` o `\small` en los estilos de nodo.
  6. Envolver todo el diagrama en `\begin{adjustbox}{max width=\textwidth, max totalheight=0.6\textheight}` para que quepa sin encoger demasiado.
  7. Comprobar en PDF: ninguna flecha atraviesa una caja, ninguna etiqueta pisa una flecha o caja, letras ≥8pt.
  8. Si persiste, simplificar el diagrama: mostrar solo lo esencial.

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
