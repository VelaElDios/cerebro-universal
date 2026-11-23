---
tipo: "receta"
titulo: "Revisión visual final página a página (regla 15 Javier)"
temas: ["latex", "maquetacion", "pdf"]
claves: ["revisar_maquetacion.py", "regla-8", "regla-9", "regla-10", "regla-11", "regla-15"]
proyectos: ["memoria-procesos"]
fuentes: ["memoria/reglas-tfg.md"]
confianza: "propuesto"
fecha: "2026-11-23"
actualizado: "2026-11-23"
---

Temas: [[latex]] · [[maquetacion]] · [[pdf]]

Checklist de revisión visual final (obligatorio antes de TERMINADO):
1. **Regla 8**: Ninguna página con una sola imagen. Capturas ≤ `height=0.42\textheight`; diagramas grandes con `max totalheight`; flotantes `[htbp]` con parámetros relajados.
2. **Regla 9**: Ninguna página casi vacía ni con sección de 1–2 líneas. Fundir secciones cortas o convertir en lista.
3. **Regla 10**: Sin figuras repetidas. Cada imagen una sola vez; en el resto `\ref`.
4. **Regla 11**: Flechas con `$\rightarrow$` (LaTeX), nunca `->` (ASCII).
5. **Regla 12**: Prosa de TFG, no listas de capturas. Capturas integradas en párrafos explicando qué hace el usuario y por qué la app responde así. Agrupar relacionadas con `subfigure`.
6. **Regla 13**: Nada de "La figura X muestra..." suelto.
7. **Regla 14**: Todo tiene sentido: cada figura/tabla citada y explicada, sin relleno, orden lógico.
8. **Regla 15**: PDF revisado página a página + `revisar_maquetacion.py` en verde.
9. **Reglas 16-18**: Diagramas legibles a tamaño real (≥7.5 pt), sin cruces, sin palabras partidas, flechas con codos.
10. **Regla 19**: Revisión visual de TODOS los diagramas en PDF (Gemini 404 no exime).

> Antes de marcar TERMINADO, el PDF se revisa página a página, y revisar_maquetacion.py debe salir en verde. Lo que no mide el script (que las tablas se lean bien y que el orden tenga sentido) lo comprueba el revisor.
> — `memoria/reglas-tfg.md` (cita sin comprobar)

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
