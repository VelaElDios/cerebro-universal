---
tipo: "receta"
titulo: "Proceso de 4 pasos para cerrar un hito y actualizar DoneTonic"
temas: ["donetonic", "git", "github-flow", "grada-colchonera", "scrum", "sprint"]
claves: ["cierre hito", "PR", "merge", "etiqueta", "tag", "despliegue", "DoneTonic", "Hecho"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/CONTRIBUTING.md"]
confianza: "verificado"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[donetonic]] · [[git]] · [[github-flow]] · [[grada-colchonera]] · [[scrum]] · [[sprint]]

Proceso formal de cierre de hito:
1. **Verificación**: todas las tareas del hito integradas en `hito-N/integracion` con CI verde.
2. **PR de hito**: abrir PR de `hito-N/integracion` → `main`.
3. **Merge y etiquetado**: tras merge, etiquetar el commit en `main` con tag `hito-N` y verificar despliegue automático.
4. **Sincronización DoneTonic**: mover tareas y PBIs del hito a estado *Hecho* en DoneTonic.
Esto alinea el estado del repositorio (git tags, main) con la herramienta de gestión de proyecto (DoneTonic).

> 1. Todas las tareas del hito están integradas en `hito-N/integracion` y el CI está en verde. 2. PR de `hito-N/integracion` a `main`. 3. Tras el merge, se etiqueta el commit de `main` como `hito-N` y se comprueba que el despliegue funciona. 4. En DoneTonic, las tareas y PBIs del hito pasan a *Hecho*.
> — `repo:saas/CONTRIBUTING.md`

Relacionado: [[fases-del-sprint-2-y-prs-asociados]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
