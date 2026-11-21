---
tipo: "receta"
titulo: "Cómo mapear este documento a los capítulos de la memoria TFG"
temas: ["grada-colchonera", "latex", "saas", "tfg"]
claves: ["capítulos memoria", "mapeo secciones", "diagrama mermaid", "capturas", "graphicspath"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/docs/documentacion-tecnica.md"]
confianza: "propuesto"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[grada-colchonera]] · [[latex]] · [[saas]] · [[tfg]]

Guía directa para volcar el contenido de esta documentación técnica en la memoria LaTeX del TFG. Cada fila indica: capítulo de la memoria, fichero .tex destino, y qué secciones numeradas de este documento (y a veces ficheros extra como `docs/gestion/README.md`) lo alimentan. Además: los diagramas Mermaid se exportan a PDF/PNG con `npx @mermaid-js/mermaid-cli -i diagrama.mmd -o diagrama.pdf` y se guardan en `memoria/figuras/`; las capturas ya están referenciadas por `\graphicspath` en `memoria/main.tex` buscando en `docs/capturas/app/`, `docs/capturas/hito4/` y `docs/capturas/produccion/`, por lo que basta usar `\includegraphics{07-panel-admin}`; la lista completa de capturas está en la sección 16.

> Esta tabla dice qué secciones de este documento alimentan cada capítulo:
| Capítulo de la memoria | Fichero | Secciones de este documento |
|---|---|---|
| Resumen / abstract | `preliminares/resumen.tex` | 2, 14 y 15 |
| 1. Introducción | `capitulos/01-introduccion.tex` | 2 y 3 |
| 2. Gestión del proyecto | `capitulos/02-gestion.tex` | 4 (y [`docs/gestion/README.md`](gestion/README.md)) |
| 3. Arquitectura | `capitulos/03-arquitectura.tex` | 5 y 6.1–6.3 |
| 4. Implementación | `capitulos/04-implementacion.tex` | 6, 7, 8 y 9 |
| 5. Pruebas, errores y logs | `capitulos/05-pruebas.tex` | 10 y 12 |
| 6. CI/CD | `capitulos/06-cicd.tex` | 11 |
| 7. Conclusiones | `capitulos/07-conclusiones.tex` | 13, 14 y 15 |
| Anexo A. Manual de usuario | `anexos/A-manual-usuario.tex` | 9.2 y 16 (capturas) |
| Anexo B. Trazabilidad | `anexos/B-trazabilidad.tex` | 3 y 4.4 |
> — `repo:saas/docs/documentacion-tecnica.md`

Relacionado: [[como-se-pone-la-portada-oficial-del-tfg-esiiab-uclm]] · [[comprobar-la-maquetacion-de-un-tfg-automaticamente]] · [[como-exportar-diagramas-mermaid-para-la-memoria-latex]] · [[estructura-de-8-capitulos-para-la-memoria-tfg-esiiab-uclm]] · [[como-referenciar-capturas-de-pantalla-en-la-memoria-sin-copi]] · [[estructura-de-la-memoria-tfg-esiiab-uclm-plantilla-oficial]] · [[rutas-de-documentacion-tras-reorganizacion-del-bundle-2026-1]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]

> ⚠️ Posible contradicción con [[estructura-de-8-capitulos-para-la-memoria-tfg-esiiab-uclm]]: La Nota B afirma que la memoria TFG debe tener **exactamente 8 capítulos** con nombres y orden fijos (1.Introducción…, 2.Antecedentes, 3.Propuesta…, 4.Descripción…, 5.Evaluación, 6.Conclusiones…, 7.Bibliografía, 8.Anexos). La Nota A presenta una estructura distinta: 7 capítulos numerados más Resumen y dos anexos, con títulos como «Gestión del proyecto», «Arquitectura», «Implementación», «CI/CD», etc., que no coinciden con los 8 capítulos obligatorios de la Nota B.
