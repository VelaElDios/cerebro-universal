---
tipo: "receta"
titulo: "Checklist previo a abrir Pull Request: npm test local obligatorio"
temas: ["git", "github-flow", "grada-colchonera", "scrum"]
claves: ["npm test", "CI", "pruebas", "pull request", "local"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/CONTRIBUTING.md"]
confianza: "verificado"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[git]] · [[github-flow]] · [[grada-colchonera]] · [[scrum]]

Antes de abrir cualquier PR, el desarrollador debe ejecutar `npm test` en local y verificar que todas las pruebas pasan. El CI repite la ejecución en el PR y bloquea la integración si hay fallos (CI en rojo). Esto garantiza que solo código que pasa tests llega a las ramas de integración.

> Las pruebas tienen que pasar en local. El CI las vuelve a ejecutar en cada PR y no se integra ningún PR con el CI en rojo.
> — `repo:saas/CONTRIBUTING.md`

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
