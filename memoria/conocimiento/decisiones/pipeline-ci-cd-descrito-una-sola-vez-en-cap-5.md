---
tipo: "decision"
titulo: "Pipeline CI/CD descrito una sola vez en el Capítulo 5 (Regla 14 Javier)"
temas: ["arquitectura", "cicd", "coherencia", "latex", "memoria", "memoria-procesos", "pipeline", "redaccion"]
claves: ["pipeline duplicado", "\\ref{fig:pipeline}", "coherencia entre capítulos", "pipeline", "fig:pipeline", "duplicado", "regla 14"]
proyectos: ["memoria-procesos"]
fuentes: ["memoria/reglas-tfg.md", "chapters/03-propuesta.tex"]
confianza: "propuesto"
fecha: "2026-11-19"
actualizado: "2026-11-21"
---

Temas: [[arquitectura]] · [[cicd]] · [[coherencia]] · [[latex]] · [[memoria]] · [[memoria-procesos]] · [[pipeline]] · [[redaccion]]

**Temas:** [[cicd]] · [[coherencia]] · [[latex]] · [[pipeline]] · [[arquitectura]]

**Regla principal**
La descripción completa del pipeline CI/CD (jobs, triggers, despliegue, workflows, captura de GitHub Actions) va **exclusivamente en el Capítulo 5 (Evaluación)**:
- Figura `\ref{fig:pipeline}` (diagrama)
- Tabla `\ref{tab:workflows}` (detalle de workflows)
- Captura `\ref{fig:actions-verde}` (ejecución exitosa)

En el **Capítulo 3 (Propuesta)**, **Anexo A1 (Desarrollo)** y **cualquier otro capítulo**, donde se mencione el CI/CD:
- **No** repetir la descripción del pipeline, ni la tabla de workflows, ni el diagrama, ni la captura de GitHub Actions.
- **Sí** remitir con `\ref{fig:pipeline}` y `\ref{tab:workflows}` a la explicación única del Cap 5.
- Texto de referencia sugerido:
  > «El pipeline completo (pruebas con PostgreSQL 17, imagen Docker y despliegue en Cloud Run) se describe una sola vez, en el Capítulo~\ref{cap:evaluacion}, Figura~\ref{fig:pipeline}.»
  > — `chapters/03-propuesta.tex`

**Detalle técnico del pipeline (para la descripción única del Cap 5)**
- **CI:** PostgreSQL 17 real + Docker build.
- **Deploy:** Cloud Run con Workload Identity Federation, Artifact Registry, Secret Manager.
- **Extra:** Render webhook en paralelo.

**Fundamento de coherencia**
> Coherencia: el mismo dato se cuenta igual en todos los capítulos, y sin repetir párrafos enteros entre capítulos (por ejemplo, la descripción del pipeline: se explica una vez y en el resto se remite a ella).
> — `memoria/reglas-tfg.md` (Regla 14 de Javier)

**Relacionado**
[[prosa-de-tfg-vs-lista-de-capturas]] · [[pipeline-ci-cd-descrito-una-sola-vez-en-cap-5]] · [[una-imagen-en-un-solo-sitio-y-en-el-resto-una-referencia]] · [[pipeline-ci-cd-github-actions-con-postgresql-17-real-docker]] · [[pipeline-ci-cd-github-actions-cloud-run-con-workload-identit]] · [[pipeline-ci-cd-descrito-una-sola-vez-en-cap-5]]

**Origen**
[[proyectos/memoria-procesos/estado|memoria-procesos]]

> Coherencia: el mismo dato se cuenta igual en todos los capítulos, y sin repetir párrafos enteros entre capítulos (por ejemplo, la descripción del pipeline: se explica una vez y en el resto se remite a ella).
> — `memoria/reglas-tfg.md` (cita sin comprobar)
> El pipeline completo (pruebas con PostgreSQL 17, imagen Docker y despliegue en Cloud Run) se describe una sola vez, en el Capítulo~\ref{cap:evaluacion}, Figura~\ref{fig:pipeline}.
> — `chapters/03-propuesta.tex`

Fusionada con: Pipeline CI/CD descrito una sola vez en Cap 5 (regla 14 Javier)

Relacionado: [[como-mapear-este-documento-a-los-capitulos-de-la-memoria-tfg]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
