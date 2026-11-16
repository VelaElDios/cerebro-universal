---
tipo: "concepto"
titulo: "Definición de Hecho (DoD) para tareas, hitos y fases"
temas: ["donetonic", "grada-colchonera", "saas", "scrum"]
claves: ["DoD", "definición de hecho", "tarea", "hito", "fase", "CI", "deploy", "documentación"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/docs/gestion/README.md"]
confianza: "verificado"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[donetonic]] · [[grada-colchonera]] · [[saas]] · [[scrum]]

Criterios obligatorios para considerar completado un elemento:
- **Tarea**: (1) Código en PR con referencia a la tarea (título del PR en Sprint 1, descripción de la tarea en Sprint 2). (2) CI verde (check "Pruebas") y pruebas propias para código nuevo. (3) PR fusionado y desplegado en URL pública de Cloud Run. (4) Documentación actualizada (README, docs/, .env.example) si procede.
- **Hito (Sprint 1)**: Rama del hito en `main` + desplegada + publicada como release en GitHub (tags hito-1, hito-2, hito-3, hito-4).
- **Fase del juego (Sprint 2)**: PR de la fase en `main` + desplegado + probado manualmente en navegador.

> Un **hito** (Sprint 1) está hecho cuando su rama está en `main`, desplegada y publicada como release. Una **fase del juego** (Sprint 2) está hecha cuando su PR está en `main`, desplegado y probado a mano en el navegador.
> — `repo:saas/docs/gestion/README.md`

Relacionado: [[estrategia-de-pruebas-error-first-y-ci-como-requisito-de-mer]] · [[como-se-pone-la-portada-oficial-del-tfg-esiiab-uclm]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
