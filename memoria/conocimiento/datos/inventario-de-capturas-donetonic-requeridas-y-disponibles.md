---
tipo: "dato"
titulo: "Inventario de capturas DoneTonic requeridas y disponibles"
temas: ["capturas", "donetonic", "memoria", "trazabilidad"]
claves: ["donetonic", "backlog", "tablero", "graficas", "pbi-detalle", "tareas"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/@arbol y repo:saas/docs/documentacion-tecnica.md §16"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[capturas]] · [[donetonic]] · [[memoria]]

8 capturas disponibles en `figs/capturas/donetonic/` (copiadas del repo). El test `verificar.py` exige al menos 5 distintas en el PDF. Distribución canónica tras paso 2:
- Capítulo 3 (propuesta): fig:donetonic-tablero (01-tablero-sprint.png), fig:donetonic-backlog (03-backlog.png)
- Anexo A1 (desarrollo): fig:donetonic-graficas-s1 (02-graficas-sprint.png), fig:donetonic-s2-graficas (06-graficas-sprint2.png), fig:donetonic-s2-tablero (04-tablero-sprint2.png), fig:donetonic-pbi-detalle (08-pbi-detalle.png), fig:donetonic-s2-tareas (05-sprint2-tareas-hechas.png)
- Capítulo 4 (descripción) y Anexo A2 (material): solo referencias `\ref` a las anteriores.
Total en PDF: 7 figuras distintas → cumple mínimo 5.

> DoneTonic (docs/capturas/donetonic/, 29/10/2026): 01-tablero-sprint.png, 02-graficas-sprint.png, 03-backlog.png, 04-tablero-sprint2.png, 05-sprint2-tareas-hechas.png, 06-graficas-sprint2.png, 07-graficas-backlog.png, 08-pbi-detalle.png
> — `repo:saas/@arbol y repo:saas/docs/documentacion-tecnica.md §16` (cita sin comprobar)

## Ampliación (2026-11-17, memoria-procesos)
8 capturas disponibles en `figs/capturas/donetonic/`. El test `verificar.py` exige al menos 5 distintas en el PDF. Distribución canónica tras paso 2: Capítulo 3 (propuesta): fig:donetonic-tablero (01-tablero-sprint.png), fig:donetonic-backlog (03-backlog.png), fig:donetonic-graficas-s1 (02-graficas-sprint.png). Anexo A1 (desarrollo): fig:donetonic-s2-graficas (06-graficas-sprint2.png), fig:donetonic-s2-tablero (04-tablero-sprint2.png), fig:donetonic-pbi-detalle (08-pbi-detalle.png), fig:donetonic-s2-tareas (05-sprint2-tareas-hechas.png). Total en PDF: 7 figuras distintas → cumple mínimo 5.
relacionado: Inventario de capturas de pantalla con trazabilidad a requisitos y fechas

Relacionado: [[capturas-de-donetonic-disponibles-en-el-repo]] · [[inventario-de-capturas-de-pantalla-con-trazabilidad-a-requis]] · [[cada-imagen-aparece-una-sola-vez-en-el-capitulo-canonico]] · [[inventario-de-capturas-de-pantalla-con-trazabilidad-a-requis]] · [[inventario-de-capturas-con-trazabilidad-a-requisitos-y-fecha]] · [[capturas-disponibles-por-carpeta-minimos-requeridos]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]

> ⚠️ Posible contradicción con [[cada-imagen-aparece-una-sola-vez-en-el-capitulo-canonico]]: Nota A sitúa la captura **Backlog (03-backlog.png)** en el **Capítulo 3 (propuesta)** con label `fig:donetonic-backlog`. Nota B la sitúa en el **Anexo A1 (a1-desarrollo.tex)** con el mismo label. Ambas notas hablan de la misma imagen y discrepan en su capítulo canónico.
