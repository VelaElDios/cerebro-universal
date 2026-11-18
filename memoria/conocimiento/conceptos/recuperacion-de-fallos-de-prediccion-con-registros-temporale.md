---
tipo: "concepto"
titulo: "Recuperación de fallos de predicción con registros temporales"
temas: ["ac", "arquitectura", "buffer-reordenamiento", "prediccion-saltos", "recuperacion", "registros-renombramiento"]
claves: ["recuperación fallo", "registros temporales", "renombramiento", "buffer reordenamiento", "Tema 5", "camino alternativo", "prebuscar"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[arquitectura]] · [[buffer-reordenamiento]] · [[prediccion-saltos]] · [[recuperacion]] · [[registros-renombramiento]]

Durante la ejecución especulativa, los resultados se guardan en registros temporales (registros de renombramiento o buffer de reordenamiento/ROB), sin modificar registros arquitectónicos ni memoria. Si la predicción fue correcta: se actualizan registros/memoria. Si fue incorrecta: se descartan los resultados temporales. Para reanudar por el camino correcto, el procesador debe guardar al menos la dirección de comienzo del camino alternativo. Si se predijo "no tomado": calcular y almacenar dirección destino del salto (+ opcionalmente prebuscar primeras instrucciones del destino). Si se predijo "tomado": almacenar dirección de la instrucción siguiente al salto (+ opcionalmente prebuscar primeras instrucciones secuenciales).

> Los resultados de esas instrucciones especulativas se almacenan en registros temporales – registros de renombramiento, o – buffer de reordenamiento (Tema 5) – Las instrucciones no modifican los contenidos de los registros de la arquitectura ni de la memoria
> — `repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4.pdf` (cita sin comprobar)

Relacionado: [[costes-de-recuperacion-de-fallos-de-prediccion-por-procesado]] · [[planteamiento-general-de-prediccion-de-saltos-con-ejecucion]] · [[recuperacion-ante-fallo-de-prediccion-de-salto-misprediction]] · [[mecanismos-de-recuperacion-ante-fallos-de-prediccion-de-salt]] · [[recuperacion-ante-fallo-de-prediccion-descartar-resultados-e]]
