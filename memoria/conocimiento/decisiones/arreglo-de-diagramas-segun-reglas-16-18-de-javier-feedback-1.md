---
tipo: "decision"
titulo: "Arreglo de diagramas según reglas 16-18 de Javier (feedback 17/11)"
temas: ["diagramas", "latex", "pgf-umlsd", "tikz"]
claves: ["fig:capas", "fig:sec-registro", "fig:juego-arquitectura", "regla16", "regla17", "regla18"]
proyectos: ["memoria-procesos"]
fuentes: ["revisión humana (Javier) 2026-11-17"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[diagramas]] · [[latex]] · [[pgf-umlsd]] · [[tikz]]

Tres diagramas prioritarios a rehacer en siguiente fase (tras pasos 3-4 de texto):
1. **fig:capas** (04-descripcion.tex): separar cajas (node distance), flechas solo entre adyacentes (Lógica→Datos, Datos→Integraciones), ensanchar cajas (text width) o partir texto en dos líneas para rutas ("src/repositories", "src/services").
2. **fig:sec-registro** y demás diagramas de secuencia con >6 participantes: agrupar (ej. "Vista + api.js" → "Frontend") o partir en dos diagramas (cliente / servidor). Usar `\resizebox` solo para ajuste fino, no para meter 9 columnas.
3. **fig:juego-arquitectura** (04b-juego.tex): reordenar nodos (positioning library), separar bloques simulación/presentación/servidor, flechas entre cajas vecinas sin cruzar ninguna, evitar overlap con `node distance` suficiente.
Herramientas: TikZ con `positioning`, `fit`, `calc`; `sequencediagram` (pgf-umlsd) con máx 6 participantes; `adjustbox` para `max totalheight`.

> Figura 3.1 (arquitectura en capas): la flecha vertical de la Lógica a las Integraciones atraviesa la caja Datos. En las cajas se parten las rutas. Diagramas de secuencia con 9 participantes salen diminutos. Figura 4.7 (arquitectura del juego): caja config.js pisada por juego.js, flechas verticales atraviesan cajas.
> — `revisión humana (Javier) 2026-11-17` (cita sin comprobar)

Relacionado: [[diagramas-ninguna-linea-flecha-atraviesa-cajas-codos-y-dista]] · [[diagramas-de-secuencia-con-pgf-umlsd-sequencediagram]] · [[diagramas-de-secuencia-max-6-participantes-agrupar-o-partir]] · [[limites-y-calidad-de-diagramas-participantes-legibilidad-rou]] · [[validacion-visual-de-diagramas-tikz-pgf-umlsd-en-pdf-reglas]] · [[como-corregir-diagramas-de-secuencia-pgf-umlsd-para-pasar-re]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
