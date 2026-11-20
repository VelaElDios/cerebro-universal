---
tipo: "decision"
titulo: "Pipeline CI/CD descrito una sola vez en Cap 5"
temas: ["arquitectura", "cicd", "coherencia"]
claves: ["pipeline", "fig:pipeline", "duplicado", "regla 14"]
proyectos: ["memoria-procesos"]
fuentes: ["chapters/03-propuesta.tex"]
confianza: "verificado"
fecha: "2026-11-19"
actualizado: "2026-11-19"
---

Temas: [[arquitectura]] · [[cicd]] · [[coherencia]]

La descripción completa del pipeline CI/CD (jobs, triggers, despliegue) va solo en el Capítulo 5 (Evaluación) con la Figura fig:pipeline. En el Capítulo 3 (Propuesta) y otros capítulos, solo se cita con `\ref{fig:pipeline}` y se remite a esa explicación. No se repite el texto ni la figura.

> El pipeline completo (pruebas con PostgreSQL 17, imagen Docker y despliegue en Cloud Run) se describe una sola vez, en el Capítulo~\ref{cap:evaluacion}, Figura~\ref{fig:pipeline}.
> — `chapters/03-propuesta.tex`

Relacionado: [[pipeline-ci-cd-descrito-una-sola-vez-en-cap-5-regla-14-javie]] · [[pipeline-ci-cd-github-actions-cloud-run-con-workload-identit]] · [[pipeline-ci-cd-github-actions-con-postgresql-17-real-docker]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
