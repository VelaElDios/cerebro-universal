---
tipo: "receta"
titulo: "Validación final del PDF antes de marcar TERMINADO"
temas: ["latex", "pdf", "verificacion"]
claves: ["revisar_maquetacion.py", "revisar_umlsd.py", "comando_prueba", "visual"]
proyectos: ["memoria-procesos"]
fuentes: ["memoria/reglas-tfg.md"]
confianza: "propuesto"
fecha: "2026-11-22"
actualizado: "2026-11-22"
---

Temas: [[latex]] · [[pdf]] · [[verificacion]]

Checklist obligatorio antes de TERMINADO:
1. `comando_prueba` → compila sin errores, `verificar.py` OK, `revisar_maquetacion.py` OK.
2. `revisar_umlsd.py` → sin errores en diagramas de secuencia (participantes declarados, sin &/_/# sueltos, sin paréntesis en \mess, etc.).
3. **Revisión visual página a página** del PDF:
   - Regla 8: ninguna página con una sola imagen (capturas ≤0.42\textheight, diagramas con max totalheight).
   - Regla 9: ninguna página casi vacía ni sección de 1-2 líneas.
   - Regla 10: ninguna imagen repetida (usar \ref).
   - Regla 11: flechas son $\rightarrow$, no ->.
   - Regla 16: diagramas legibles a tamaño real (letras ≥8 pt, sin flechas cruzando cajas, sin cajas pisadas, sin palabras partidas).
   - Tablas: filas no pisadas (p{}, \addlinespace), anchos ≤\linewidth, código con \allowbreak.
   - Bibliografía: autores corporativos con doble llave, year en todas, URLs de fuentes.
   - Resumen ≥150 palabras, Abstract ≥120 palabras, ambos con palabras clave.
   - Anexo desarrollo: dos sprints mismo esquema, explica recta Sprint 2.
   - Anexo trazabilidad: 82 tareas (T1–T82) con requisito→PBI→tarea→PR.
   - Mínimos capturas: app/ 4+, hito4/ 4+, juego/ 8+, donetonic/ 5+, produccion/ 2+, prueba-tecnica/ 1+.
4. Si todo pasa → TERMINADO = sí.

> Antes de marcar TERMINADO, el PDF se revisa página a página, y revisar_maquetacion.py debe salir en verde. Lo que no mide el script (que las tablas se lean bien y que el orden tenga sentido) lo comprueba el revisor.
> — `memoria/reglas-tfg.md` (cita sin comprobar)

Relacionado: [[como-replantear-diagramas-de-secuencia-pgf-umlsd-para-pasar]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
