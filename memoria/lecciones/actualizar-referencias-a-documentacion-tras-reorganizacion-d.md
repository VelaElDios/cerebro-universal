---
titulo: "Actualizar referencias a documentación tras reorganización del bundle"
temas: ["latex", "documentación", "mantenimiento"]
claves: ["docs/revision-entrega.md", "docs/documentacion-tecnica.md", "docs/gestion/README.md", "docs/arquitectura.md"]
estado: "propuesta"
veces: 1
fecha: "2026-11-21"
proyectos: ["memoria-procesos"]
---

Temas: [[latex]] · [[documentación]] · [[mantenimiento]]

## Problema
Tras la reorganización del bundle documental (2026-11-19), varios archivos de la memoria seguían referenciando la estructura antigua de `docs/` (ficheros que ya no existen). Esto rompía la trazabilidad y podía causar errores en la verificación automática.

## Solución
Sustituir sistemáticamente las rutas antiguas por las nuevas del bundle: `docs/revision-entrega.md` → `docs/sprint-1.md` (contiene la revisión frase a frase), `docs/documentacion-tecnica.md` → `docs/requisitos.md` (fuente de requisitos), `docs/gestion/README.md` → `docs/sprint-1.md` y `docs/sprint-2.md` (trazabilidad), y referencias a secciones numeradas de `docs/arquitectura.md` por las secciones actuales del bundle. Hacerlo en todos los capítulos y anexos afectados.

## Ejemplo
En `a4-trazabilidad.tex`: `\texttt{docs/documentacion-tecnica.md}` → `\texttt{docs/requisitos.md}`; `\texttt{docs/gestion/README.md}` → `\texttt{docs/sprint-1.md}` y `\texttt{docs/sprint-2.md}`. En `a3-uso-ia.tex`: `\texttt{docs/revision-entrega.md}` → `\texttt{docs/sprint-1.md}`. En `05-evaluacion.tex` y `a1-desarrollo.tex`: igual.
---

Origen: [[proyectos/memoria-procesos/bitacora|memoria-procesos]]
