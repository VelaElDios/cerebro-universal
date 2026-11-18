---
tipo: "concepto"
titulo: "Recuperación ante fallo de predicción: descartar resultados especulativos y reanudar por camino correcto"
temas: ["ac", "especulacion", "prediccion-saltos"]
claves: ["fallo predicción", "recuperación", "resultados especulativos", "camino correcto"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2013.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[especulacion]] · [[prediccion-saltos]]

Cuando se detecta un fallo de predicción de salto, el procesador debe hacer un flush del pipeline: anular todas las instrucciones fetchadas y ejecutadas especulativamente por el camino erróneo, descartar sus resultados (no actualizar estado arquitectónico) y reiniciar la fetch desde la dirección correcta del salto.

> Ante un caso de fallo de predicción: a. Deben descartarse los resultados de las instrucciones ejecutadas especulativamente y reanudarse la ejecución del programa por el camino correcto
> — `repo:datos/temarios/AC/examenes/Junio2013.pdf`

Relacionado: [[accion-del-procesador-ante-fallo-de-prediccion-de-salto]] · [[bits-venenosos-en-especulacion-excepcion-no-recuperable-marc]]
