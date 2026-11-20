---
tipo: "concepto"
titulo: "Glosario técnico del proyecto (22 términos definidos)"
temas: ["grada-colchonera", "latex", "memoria", "saas", "tfg"]
claves: ["PBI", "DoD", "GitHub Flow", "CI/CD", "OAuth 2.0", "state", "HMAC", "bcrypt", "baja lógica", "WIF", "concurrencia optimista", "survivor", "paso fijo", "procedural", "chiptune"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/docs/documentacion-tecnica.md"]
confianza: "verificado"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[grada-colchonera]] · [[latex]] · [[memoria]] · [[saas]] · [[tfg]]

Glosario de 22 términos técnicos usados en la documentación y el TFG, categorizados:
**Gestión ágil**: PBI, Historia de usuario, DoD, GitHub Flow, CI/CD.
**Auth/Seguridad**: OAuth 2.0 (auth code flow), state (CSRF), HMAC (firma enlaces), bcrypt (hash passwords), WIF (GitHub→GCP sin secrets).
**Patrones BD**: Baja lógica, Concurrencia optimista (version number).
**Juego**: Survivor (género), Paso fijo (fixed timestep 1/60s), Procedural (mapa desde semilla), Chiptune (audio 8-bit).
Sirve como anexo de definiciones en la memoria del TFG y para onboarding de nuevas IAs/desarrolladores.

> | Término | Significado |
|---|---|
| **PBI** | *Product Backlog Item*: elemento del backlog (requisito) con criterios de aceptación |
| **Historia de usuario** | Requisito escrito desde el punto de vista de quien lo usa: «Como … quiero … para …» |
| **DoD** | *Definition of Done*: condiciones para dar una tarea o un hito por terminados |
| **GitHub Flow** | Flujo de trabajo con ramas cortas y pull requests hacia una rama principal siempre desplegable |
| **CI/CD** | Integración continua (pruebas automáticas en cada cambio) y despliegue continuo (publicar sin intervención manual) |
| **OAuth 2.0** | Protocolo de autorización; aquí, el flujo de «código de autorización» para entrar con Google |
| **`state`** | Valor aleatorio que protege el flujo OAuth contra CSRF |
| **HMAC** | Código de autenticación de mensajes con clave: permite firmar los enlaces de confirmación |
| **bcrypt** | Función de hash lenta y con sal, pensada para contraseñas |
| **Baja lógica** | Marcar un registro como eliminado en lugar de borrarlo |
| **WIF** | *Workload Identity Federation*: GitHub obtiene credenciales temporales de Google Cloud sin claves guardadas |
| **Concurrencia optimista** | Detectar escrituras simultáneas con un número de versión en lugar de bloquear |
| **Survivor** | Género de videojuego en el que el jugador aguanta oleadas crecientes de enemigos con armas que atacan solas |
| **Paso fijo** | La simulación avanza siempre el mismo tiempo (1/60 s), independientemente de los FPS |
| **Procedural** | Contenido (aquí, el mapa) generado por algoritmo a partir de una semilla |
| **Chiptune** | Música al estilo de las consolas de 8 bits, con ondas simples |
> — `repo:saas/docs/documentacion-tecnica.md`

Relacionado: [[requisitos-funcionales-del-sprint-1-13-rf-con-trazabilidad]] · [[requisitos-funcionales-del-juego-sprint-2-20-rj-con-trazabil]] · [[estrategia-de-pruebas-niveles-y-enfoque-error-first]] · [[definicion-de-hecho-dod-para-tareas-hitos-y-fases]] · [[desglose-del-alcance-del-sprint-1-por-hitos-y-fechas]] · [[definicion-de-hecho-dod-para-tareas-e-hitos]] · [[estado-de-completitud-de-sprints-y-trazabilidad]] · [[tabla-de-trazabilidad-sprint-2-pbi-etiqueta-titulo-tareas-pr]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
