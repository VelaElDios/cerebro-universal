---
tipo: "decision"
titulo: "Cada cifra del documento sale de las fuentes, también las pequeñas"
temas: ["memoria", "verificacion", "fuentes"]
claves: ["verificar.py", "fuentes", "cifras"]
proyectos: ["memoria-procesos"]
fuentes: ["memoria/reglas-tfg.md"]
confianza: "propuesto"
fecha: "2026-11-20"
actualizado: "2026-11-20"
---

Temas: [[memoria]] · [[verificacion]]

Antes de escribir cualquier cifra (también las pequeñas, y las que salen de sumar), buscarla en las fuentes y copiarla tal cual. Si hay que contar elementos de una lista (P1–P14 y P18), contarlos uno a uno y comprobarlo con la tabla de la fuente. Lo que no está en las fuentes no se escribe. Ejemplo: "80 pruebas" → guia.md §7 "Total 80 pruebas automatizadas"; "15 PBIs al inicio" → gestion.md, tabla "Evolución del sprint", fila "Inicio del Sprint 1".

> Lo que no hayas comprobado, dilo: "no comprobado". Un "aprobado" sin comprobaciones no cuenta.
> — `memoria/reglas-tfg.md` (cita sin comprobar)

Relacionado: [[numeros-clave-del-proyecto-verificados-en-fuentes]] · [[numeros-en-la-memoria-deben-aparecer-tal-cual-en-las-fuentes]] · [[cada-cifra-de-un-documento-sale-de-las-fuentes-tambien-las-p]] · [[numeros-pequenos-tambien-se-verifican-en-fuentes]]

## Ampliación (2026-11-20, memoria-procesos)
|
  Regla obligatoria para el revisor: contrastar **al menos 25 datos** repartidos por todos los capítulos y anexos (cifra o hecho → sección de la fuente), incluidos números pequeños.
  Ejemplos de comprobación:
  - U1: impares (5−1)+(5−1)+(4−1)+(5−1)+(5−1)=19; pares (5−1)+(5−1)+(5−2)+(5−1)+(5−1)=19; (19+19)×2,5=95 → coincide con el documento.
  - 80 pruebas → guia.md §7: «80 pruebas automatizadas».
  - 15 PBIs al inicio → sprint-1.md tabla «Evolución del Sprint 1», fila «Inicio del Sprint 1».
  - 19 PBIs Sprint 1 → sprint-1.md tabla «Backlog y estado del Sprint 1».
  - 29 PBIs Sprint 2 → sprint-2.md tabla «Backlog y estado del Sprint 2».
  - 82 tareas totales → sprint-1.md (32) + sprint-2.md (50).
  - 276 pruebas cierre S2 → procesos.md tabla «Pruebas por fichero», fila Total.
  - 322 pruebas tras Fase 7 → log.md entrada 2026-11-03.
  - 5 migraciones → arquitectura.md lista migraciones 001–005.
  - 23 endpoints API → arquitectura.md tabla «Resumen» de rutas.
  - 36 jugadores/29 armas/6 ultras/10 jefes/5 ambientes/26 selecciones/29 logros/10 equipaciones → juego.md tabla sistemas + sprint-2.md métricas.

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
