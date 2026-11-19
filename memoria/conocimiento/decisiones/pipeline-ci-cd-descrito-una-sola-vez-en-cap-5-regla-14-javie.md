---
tipo: "decision"
titulo: "Pipeline CI/CD descrito una sola vez en Cap 5 (regla 14 Javier)"
temas: ["cicd", "coherencia", "latex", "pipeline", "memoria-procesos", "redaccion", "arquitectura", "memoria"]
claves: ["pipeline duplicado", "\\ref{fig:pipeline}", "coherencia entre capítulos"]
proyectos: ["memoria-procesos"]
fuentes: ["memoria/reglas-tfg.md"]
confianza: "propuesto"
fecha: "2026-11-19"
actualizado: "2026-11-19"
---

Temas: [[cicd]] · [[coherencia]] · [[latex]] · [[pipeline]]

|
  La descripción completa del pipeline CI/CD (Figura~\ref{fig:pipeline}, Tabla~\ref{tab:workflows}, captura Figura~\ref{fig:actions-verde}) va **solo en el Capítulo 5 (Evaluación)**.
  
  En el Capítulo 3 (Propuesta) y en el Anexo A1 (Desarrollo), donde se menciona el CI/CD:
  - **No** repetir la descripción del pipeline
  - **Sí** remitir con `\ref{fig:pipeline}` y `\ref{tab:workflows}` a la explicación del Cap 5
  - Ejemplo: "El pipeline completo (pruebas con PostgreSQL 17, imagen Docker y despliegue en Cloud Run) se describe una sola vez, en el Capítulo~\ref{cap:evaluacion}, Figura~\ref{fig:pipeline}."
  
  Esto evita duplicados, asegura coherencia y cumple la regla 14 de Javier.

> Coherencia: el mismo dato se cuenta igual en todos los capítulos, y sin repetir párrafos enteros entre capítulos (por ejemplo, la descripción del pipeline: se explica una vez y en el resto se remite a ella).
> — `memoria/reglas-tfg.md` (cita sin comprobar)

Relacionado: [[prosa-de-tfg-vs-lista-de-capturas]]

## Ampliación (2026-11-19, memoria-procesos)
|
  La descripción completa del pipeline (workflows, jobs, despliegue) va en el Capítulo 5 (Evaluación) con la Figura \ref{fig:pipeline}. En el Capítulo 3 (Propuesta) solo se cita: "El pipeline completo se describe en el Capítulo~\ref{cap:evaluacion}, Figura~\ref{fig:pipeline}." No se repite la tabla de workflows ni el diagrama.

## Ampliación (2026-11-19, memoria-procesos)
El pipeline completo (CI con PostgreSQL 17 + Docker build, deploy Cloud Run con WIF/Artifact Registry/Secret Manager, Render webhook paralelo) se describe **una sola vez** en el Capítulo 5 (Evaluación), Figura~\ref{fig:pipeline} y Tabla~\ref{tab:workflows}. En el Capítulo 3 (Propuesta) solo se cita con `\ref{fig:pipeline}` y `\ref{tab:workflows}`: «El pipeline completo se describe una sola vez, en el Capítulo~\ref{cap:evaluacion}, Figura~\ref{fig:pipeline}». No repetir la explicación ni la captura de GitHub Actions en el Cap 3.

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
