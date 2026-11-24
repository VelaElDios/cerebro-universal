---
tipo: "receta"
titulo: "Validación final del PDF antes de marcar TERMINADO"
temas: ["latex", "pdf", "verificacion", "calidad", "checklist"]
claves: ["revisar_maquetacion.py", "revisar_umlsd.py", "comando_prueba", "visual"]
proyectos: ["memoria-procesos"]
fuentes: ["memoria/reglas-tfg.md", "memoria/reglas-tfg.md § Cómo se comprueba"]
confianza: "verificado"
fecha: "2026-11-22"
actualizado: "2026-11-23"
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
> — `memoria/reglas-tfg.md`

Relacionado: Cómo replantear diagramas de secuencia pgf-umlsd para pasar revisar_maquetacion.py · [[checklist-final-antes-de-marcar-terminado-pdf-pagina-a-pagin]] · [[revision-visual-final-pagina-a-pagina-regla-15-javier]] · [[reglas-de-maquetacion-de-javier-resumen-accionable]] · [[verificacion-final-revision-pagina-a-pagina-revisar-maquetac]]

## Ampliación (2026-11-23, memoria-procesos)
Checklist obligatorio página a página (imprimir PDF o ver a 100% zoom):
1. **Portada única**: solo la de `elements/portada.tex` (escudo, UCLM, ESII, título, autor, fecha).
2. **Declaración de autoría, Resumen (≥150 pal), Abstract (≥120 pal), índices** — todos presentes y en orden.
3. **Sin páginas en blanco** entre capítulos (regla 4).
4. **Títulos negros negrita** (regla 3), enlaces sin recuadros (`hidelinks`).
5. **Tablas**: filas no se pisan (`p{}`, `\addlinespace`), anchos ≤ `\linewidth`, código con `\path{}`/`\texttt{}`+`\allowbreak`, `longtable` si > media página, última fila no sola (`\\*`).
6. **Figuras**: ninguna página con una sola imagen (regla 8) — capturas `height=0.42\textheight`, diagramas `max totalheight=0.6\textheight`, flotantes `[htbp]` con parámetros relajados.
7. **Sin secciones de 1-2 líneas** (regla 9) — fundir o convertir en lista.
8. **Sin figuras repetidas** (regla 10) — cada imagen una vez, `\ref` en el resto.
9. **Flechas reales** `$\rightarrow$` no `->` (regla 11).
10. **Diagramas legibles a tamaño real** (regla 16): letras ≥7.5 pt, sin flechas cruzando cajas/texto (regla 17), sin palabras partidas en cajas (regla 18), ≤6 participantes en secuencia.
11. **Todas las figuras/tablas** con `\caption`, `\label`, citadas con `\ref` en texto.
12. **Bibliografía**: `apalike`, autores corporativos con `{{}}`, `year` en todas (`{s.f.}` si no hay), URLs de fuentes.
13. **Cifras contrastadas**: cada número >20 en fuentes; números pequeños comprobados por revisor (25+ en COMPROBACIONES).
14. **Prosa TFG**: impersonal/tercera persona, explica porqué, sin adornos ("trasciende", "exhaustivo"...), rutas/código en `\texttt{}`.
15. **Ejecuta `comando_prueba`**: compila + `verificar.py` OK + `revisar_maquetacion.py` OK.
Solo marcar TERMINADO si **todo** lo anterior cumple.

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
