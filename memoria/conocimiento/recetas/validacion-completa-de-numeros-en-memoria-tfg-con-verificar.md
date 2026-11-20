---
tipo: "receta"
titulo: "Validación completa de números en memoria TFG con verificar.py"
temas: ["fuentes", "memoria-tfg", "numeros", "test", "verificacion"]
claves: ["verificar.py", "número no aparece en las fuentes", "fuentes obligatorias", "repo:saas/docs/"]
proyectos: ["memoria-procesos"]
fuentes: ["memoria-procesos (este proyecto)"]
confianza: "propuesto"
fecha: "2026-11-20"
actualizado: "2026-11-20"
---

Temas: [[fuentes]] · [[memoria-tfg]] · [[numeros]] · [[test]] · [[verificacion]]

Para que `verificar.py` pase, TODAS las fuentes listadas en el SPEC bajo "Fuentes: la única verdad" deben estar disponibles en el mensaje al revisor. Las 4 fuentes del repositorio (`documentacion-tecnica.md`, `gestion/README.md`, `revision-entrega.md`, `hito4-configuracion.md`) son críticas porque contienen los datos numéricos (PBIs, tareas, fechas, PRs, pruebas, métricas) que el test valida. Sin ellas, el test fallará siempre con errores de "número no aparece en las fuentes". Solución: antes de pedir revisión, confirmar que el constructor ha incluido los 4 bloques <<<FUENTE repo:saas/docs/...>>> ... <<<FIN>>> en el mensaje. Si faltan, el revisor debe marcar "cambios" y listar las fuentes faltantes como TAREA CRÍTICA 1.

> Causa raíz confirmada: 4 fuentes críticas no proporcionadas (repo:saas/docs/documentacion-tecnica.md, repo:saas/docs/gestion/README.md, repo:saas/docs/revision-entrega.md, repo:saas/docs/hito4-configuracion.md). Sin ellas, verificar.py no puede validar ningún número >20.
> — `memoria-procesos (este proyecto)` (cita sin comprobar)

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
