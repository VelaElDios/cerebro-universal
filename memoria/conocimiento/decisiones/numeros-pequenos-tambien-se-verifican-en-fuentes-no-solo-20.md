---
tipo: "decision"
titulo: "Números pequeños también se verifican en fuentes (no solo > 20)"
temas: ["fuentes", "numeros", "verificacion"]
claves: ["número «32» no aparece en las fuentes", "verificar.py", "cifras pequeñas"]
proyectos: ["memoria-procesos"]
fuentes: ["memoria/reglas-tfg.md (lección guardada)"]
confianza: "propuesto"
fecha: "2026-11-19"
actualizado: "2026-11-19"
---

Temas: [[fuentes]] · [[numeros]] · [[verificacion]]

|
  La verificación automática (`verificar.py`) comprueba TODOS los números del texto contra las fuentes, no solo los > 20. El mensaje de error "el número «XX» no aparece en las fuentes" sale para cualquier cifra.
  
  Antes de escribir cualquier número (fechas, conteos, porcentajes, versiones, IDs):
  1. Buscarlo en las fuentes (documentacion-tecnica.md, gestion/README.md, revision-entrega.md, hito4-configuracion.md, CONTRIBUTING.md, @arbol)
  2. Copiarlo tal cual (incluyendo formato: 29/10/2026, no 29-10-2026)
  3. Si hay que contar (ej. PBIs P1–P14 y P18), contarlos uno a uno y anotar la cuenta
  
  Cifras clave ya verificadas en fuentes previas:
  - Sprint 1: 19 PBIs (P1–P19), 32 tareas (T1–T32), 4 hitos, fechas 29/09–27/10/2026
  - Sprint 2: 29 PBIs (P20–P48), 50 tareas (T33–T82), fechas 23/10–29/10/2026
  - Total: 48 PBIs, 82 tareas, >50 PRs fusionados
  - Pruebas: 276 en main al cierre Sprint 2, 322 tras Fase 7
  - Burndown Sprint 1: 16 PBIs en alcance de entrega (P1–P14, P18, P19)
  - Migraciones SQL: 5 (001–005)
  - Endpoints API: 23
  - Líneas backend: ~2.300, frontend: ~1.150, juego: ~14.800, tests: ~5.050
  - Dependencias directas: 6
  - Contenido jugable: 36 jugadores, 2 entrenadores, 29 armas, 16 pasivas, 29 combinaciones, 6 ultras, 16 equipos, 10 jefes, 5 ambientes, 26 selecciones, 29 logros, 10 equipaciones

> El test solo comprueba los números mayores que 20, pero los pequeños también fallan: en la memoria de procesos se escribió «16 PBIs iniciales, 17 con P19» cuando las fuentes dicen 15 y 16, y el revisor lo dio por bueno.
> — `memoria/reglas-tfg.md (lección guardada)` (cita sin comprobar)

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
