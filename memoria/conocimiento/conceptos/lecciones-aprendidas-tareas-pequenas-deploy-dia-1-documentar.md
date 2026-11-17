---
tipo: "concepto"
titulo: "Lecciones aprendidas: tareas pequeñas, deploy día 1, documentar decisiones, verificación visual"
temas: ["cerebro", "grada-colchonera", "saas", "sprint"]
claves: ["tareas pequeñas", "automatizar despliegue", "documentar decisiones", "verificación visual", "clic perdido"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/docs/documentacion-tecnica.md"]
confianza: "verificado"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[cerebro]] · [[grada-colchonera]] · [[saas]] · [[sprint]]

Cuatro lecciones clave del proyecto:
1. **Dividir pronto en tareas pequeñas**: evita bloqueos, permite revisión incremental, mejora estimación.
2. **Automatizar despliegue desde día 1**: CI/CD (GitHub Actions → Cloud Run con WIF) listo antes de la primera feature; despliegue en cada merge a main.
3. **Documentar decisiones mientras se toman**: ADR implícitos en commits/PRs + documentación técnica viva; evita pérdida de contexto.
4. **Comprobar visualmente cada cambio de UI**: testing visual manual en cada PR detectó el "clic perdido de la sección 13" (bug de z-index/overlay en menú pausa/árbol de habilidades).
Aplicables a cualquier proyecto web full-stack con equipo pequeño.

> Lecciones: dividir pronto en tareas pequeñas, automatizar el despliegue desde el primer día, documentar las decisiones mientras se toman y comprobar visualmente cada cambio de interfaz (así apareció, por ejemplo, el clic perdido de la sección 13).
> — `repo:saas/docs/documentacion-tecnica.md`

Relacionado: [[deshacer-el-paso-entero-si-rompe-la-compilacion]] · [[tocar-trozos-con-cambiar-en-vez-de-reescribir-archivos-enter]] · [[estrategia-de-pruebas-error-first-y-ci-como-requisito-de-mer]] · [[estrategia-de-pruebas-niveles-y-enfoque-error-first]] · [[convencion-de-ramas-y-prs-por-sprint-sprint-1-vs-sprint-2]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
