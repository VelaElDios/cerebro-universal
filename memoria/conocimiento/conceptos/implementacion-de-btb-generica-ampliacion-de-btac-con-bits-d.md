---
tipo: "concepto"
titulo: "Implementación de BTB genérica: ampliación de BTAC con bits de predicción"
temas: ["ac", "btac", "btb", "prediccion-saltos"]
claves: ["Branch Target Buffer", "BTAC", "bits predicción", "dirección destino"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2026.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[btac]] · [[btb]] · [[prediccion-saltos]]

Una BTB genérica se implementa extendiendo una BTAC (que solo guarda direcciones destino) añadiendo bits de predicción (ej. contadores de saturación) en cada entrada. Así almacena conjuntamente: dirección del salto (tag), dirección destino (target) y predicción (tomado/no tomado). La opción d describe esto exactamente.

> ¿Cómo se implementa y qué almacena una BTB (Branch Target Buffer) genérica? ... d. Ampliando la BTAC (Branch Target Address Cache) con bits de predicción para guardar conjuntamente la dirección destino y la predicción de los últimos saltos.
> — `repo:datos/temarios/AC/examenes/Junio2026.pdf` (cita sin comprobar)

Relacionado: [[ancho-y-tamano-en-bits-de-un-btb-implicito-con-1024-entradas]] · [[actualizacion-de-la-btb-tras-ejecutar-el-salto]] · [[comportamiento-de-la-btb-en-caso-de-acierto-test-ac-q14]] · [[btb-cache-de-direcciones-destino-de-saltos-con-bits-de-predi]] · [[estructura-de-btb-tabla-de-destinos-y-tabla-separada-de-bits]]
