---
tipo: "receta"
titulo: "Cómo fijar colocación de figura referenciada pero no aparecida en página"
temas: ["floatbarrier", "flotantes", "latex", "placeins"]
claves: ["FloatBarrier", "placeins", "figura-no-aparece", "referencia-cruzada"]
proyectos: ["memoria-procesos"]
fuentes: ["revisar_maquetacion.py (salida: \"No existe la Figura 4.7 en la página, a pesar de que el texto hace referencia a ella\")\nproblema: Una figura flotante (`figure[htbp]`) se desplaza a páginas posteriores y el texto la referencia en una página anterior, quedando la referencia «colgada» sin figura visible en esa página.\nsolucion: (1) Mover el entorno `figure` **justo antes** de la frase que la referencia por primera vez. (2) Si no es posible, añadir `\\FloatBarrier` (requiere `\\usepackage{placeins}`) antes de la referencia para forzar la colocación de todas las figuras pendientes. (3) Como último recurso, usar `[H]` (requiere `\\usepackage{float}`) para fijar la figura exactamente ahí, pero puede dejar huecos verticales."]
confianza: "propuesto"
fecha: "2026-11-24"
actualizado: "2026-11-24"
---

Temas: [[floatbarrier]] · [[flotantes]] · [[latex]] · [[placeins]]

|
  **Opción 1 (recomendada): Mover la figura antes de la referencia**
  ```latex
  % Texto que introduce la figura
  Esa división es la que se dibuja en la Figura~\ref{fig:juego-arquitectura}.
  
  % Figura AQUÍ, antes de la referencia o en el mismo párrafo
  \begin{figure}[htbp]
  \centering
  ...
  \caption{Arquitectura del juego...}
  \label{fig:juego-arquitectura}
  \end{figure}
  ```
  **Opción 2: FloatBarrier antes de la referencia**
  ```latex
  \usepackage{placeins}  % en preámbulo (ya está en include/extra.tex)
  ...
  \FloatBarrier
  Esa división es la que se dibuja en la Figura~\ref{fig:juego-arquitectura}.
  ```
  **Opción 3: [H] (último recurso)**
  ```latex
  \usepackage{float}  % en preámbulo
  ...
  \begin{figure}[H]
  ...
  \end{figure}
  ```
  **Verificación:** Compilar y buscar en el log «Figure X» para ver en qué página cae, y comprobar que la página de la referencia tiene la figura visible.
relacionado: Figuras flotando dentro de la bibliografía: \FloatBarrier antes, Reglas de maquetación de Javier (resumen accionable)

Relacionado: [[fijar-colocacion-de-figura-referenciada-con-floatbarrier]] · [[figuras-flotando-dentro-de-la-bibliografia-floatbarrier-ante]] · [[como-mover-una-figura-antes-de-su-primera-referencia-en-late]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
