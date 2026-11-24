---
tipo: "receta"
titulo: "Cómo evitar que diagramas de secuencia pgf-umlsd desborden la página"
temas: ["diagramas-secuencia", "latex", "pgf-umlsd"]
claves: ["newinst", "adjustbox", "resizebox", "overfull", "ancho"]
proyectos: ["memoria-procesos"]
fuentes: ["memoria/reglas-tfg.md (reglas 16-18) y revisar_maquetacion.py"]
confianza: "propuesto"
fecha: "2026-11-24"
actualizado: "2026-11-24"
---

Temas: [[diagramas-secuencia]] · [[latex]] · [[pgf-umlsd]]

|
  **Patrón correcto para diagrama de secuencia que cabe en página:**
  ```latex
  \begin{figure}[htbp]
  \centering
  \begin{sequencediagram}
    \newthread{u}{Usuario}
    \newinst[3]{fe}{Frontend}
    \newinst[3]{api}{API}
    \newinst[3]{srv}{Servicio}
    \begin{call}{u}{email, clave}{fe}{ok}
    \end{call}
    \begin{call}{fe}{POST register}{api}{201/409}
      \begin{call}{api}{register}{srv}{usuario}
        \begin{call}{srv}{busca email}{srv}{fila/null}
        \end{call}
        \begin{sdblock}{alt}{existe}
          \mess{srv}{ConflictError}{api}
        \end{sdblock}
      \end{call}
    \end{call}
  \end{sequencediagram}
  \caption{Registro con email y contraseña.}
  \label{fig:sec-registro}
  \end{figure}
  ```
  **Reglas de oro:**
  - Máx. 4-5 participantes visibles (agrupar el resto como llamadas internas).
  - `\newinst[3]` o `[4]` (no `[5]` ni más).
  - Etiquetas ≤ 20 chars, sin acentos, sin paréntesis en `\mess`, `\n` para saltos.
  - Llamadas anidadas (`call` dentro de `call`) para mostrar flujo interno sin nuevos participantes.
  - `sdblock` para alternativas (no entorno `alt`).
  - Verificar con `python scripts/revisar_umlsd.py` antes de compilar.
relacionado: Diagramas de secuencia pgf-umlsd — sintaxis válida y errores comunes, Prosa de TFG sin listas de capturas (regla 13 Javier)

> Diagramas de secuencia: como mucho 6 participantes. Si hay más, se agrupan o se parte en dos diagramas. \resizebox solo para encoger un poco, no para meter 9 columnas en el ancho de la página."
problema: Aumentar la separación horizontal con `\newinst[5]` o más para dar espacio a las etiquetas hace que el diagrama sea MÁS ancho y desborde la página. Usar `adjustbox`/`resizebox` escala el dibujo y reduce el tamaño de fuente por debajo de 7,5 pt (regla 16).
solucion: (1) Reducir participantes a 4-5 máximos agrupando actores (p.ej. Frontend+API → «Frontend», TokenSigner+Mailer internos a Servicio). (2) Usar `\newinst[3]` o `[4]` para separación ajustada. (3) Acortar etiquetas: sin acentos, sin paréntesis en `\mess`, sin comandos LaTeX, usar `\n` para saltos de línea. (4) Declarar todos los participantes antes de usarlos. (5) Usar `sdblock` para alternativas, no `alt` como entorno. (6) Si >6 participantes, dividir en dos diagramas. (7) Verificar con `revisar_umlsd.py` antes de compilar.
> — `memoria/reglas-tfg.md (reglas 16-18) y revisar_maquetacion.py` (cita sin comprobar)

Relacionado: [[como-replantear-diagramas-de-secuencia-pgf-umlsd-para-evitar]] · [[diagramas-de-secuencia-pgf-umlsd-reglas-para-pasar-revisar-m]] · [[diagramas-de-secuencia-legibles-max-6-participantes-flechas]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
