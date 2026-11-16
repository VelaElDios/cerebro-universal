---
tipo: "receta"
titulo: "Definición de Hecho (DoD) para tareas e hitos"
temas: ["grada-colchonera", "metodologia", "saas", "scrum", "done", "memoria-procesos"]
claves: ["DoD", "Definición de hecho", "tarea hecha", "hito hecho", "rama", "PR", "CI", "pruebas", "main", "despliegue", "release", "README", ".env.example"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/docs/documentacion-tecnica.md"]
confianza: "verificado"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[grada-colchonera]] · [[metodologia]] · [[saas]] · [[scrum]]

DoD a dos niveles:

**Tarea hecha** cuando:
1. Código en su rama y en un PR con referencia a la tarea (ej. [T5])
2. Pruebas pasan en CI (check "Pruebas")
3. PR fusionado en la rama del hito (hito-N/integracion)
4. Documentación actualizada si hace falta (README, .env.example)

**Hito hecho** cuando:
1. Su rama (hito-N/integracion) está en main
2. Desplegada en la URL pública
3. Publicada como release (etiqueta hito-N)

Esto se refleja en el flujo GitHub Flow: las ramas main y hito-*/integracion están protegidas, solo admiten cambios por PR y exigen CI en verde.

> Una **tarea** está hecha cuando su código está en su rama y en un PR con la referencia a la tarea, las pruebas pasan en el CI (check **Pruebas**), el PR está fusionado en la rama del hito y la documentación (README, `.env.example`) está actualizada si hace falta. Un **hito** está hecho cuando su rama está en `main`, desplegada en la URL pública y publicada como release.
> — `repo:saas/docs/documentacion-tecnica.md`

Relacionado: [[cada-entrega-solo-lleva-lo-de-su-sprint-alcance-coherente]]

## Ampliación (2026-11-16, memoria-procesos)
DoD a dos niveles: **Tarea hecha** cuando: 1) Código en su rama y en un PR con referencia a la tarea (ej. [T5]); 2) Pruebas pasan en CI (check "Pruebas"); 3) PR fusionado en la rama del hito (hito-N/integracion); 4) Documentación actualizada si hace falta (README, .env.example). **Hito hecho** cuando: 1) Su rama (hito-N/integracion) está en main; 2) Desplegada en la URL pública; 3) Publicada como release (etiqueta hito-N). Esto se refleja en el flujo GitHub Flow: las ramas main y hito-*/integracion están protegidas, solo admiten cambios por PR y exigen CI en verde.

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
