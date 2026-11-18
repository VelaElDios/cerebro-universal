---
tipo: "concepto"
titulo: "Diferencias entre ejecución en orden, fuera de orden sin renombramiento y con renombramiento"
temas: ["ac", "out-of-order", "pipeline", "planificacion-instrucciones", "renombramiento-registros"]
claves: ["in-order", "out-of-order", "register renaming", "hazard WAR", "hazard WAW", "ventana instrucciones"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2011.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[out-of-order]] · [[pipeline]] · [[planificacion-instrucciones]] · [[renombramiento-registros]]

a) En orden: las instrucciones se emiten en orden de programa, se detienen ante cualquier hazard (RAW resuelto con forwarding, WAR/WAW causan parada). b) Fuera de orden sin renombramiento: se pueden emitir fuera de orden pero los registros arquitectónicos son únicos; hazards WAR (lectura tras escritura) y WAW (escritura tras escritura) provocan paradas o serialización. c) Fuera de orden con renombramiento: cada escritura usa un registro físico distinto, eliminando WAR y WAW; solo quedan dependencias RAW reales. La ventana ilimitada permite ver las 8 instrucciones a la vez para maximizar paralelismo.

> Para los apartados b) y c), supón una ventana de instrucciones lo suficientemente grande como para poder considerar todas las instrucciones del código al mismo tiempo.
> — `repo:datos/temarios/AC/examenes/Junio2011.pdf`

Relacionado: [[algoritmo-tomasulo-origen-y-objetivo-cpi1]] · [[buffers-de-carga-y-almacenamiento-en-tomasulo]] · [[diferencia-clave-entre-ejecucion-fuera-de-orden-sin-y-con-re]] · [[diferencias-clave-entre-los-tres-modelos-de-ejecucion-supers]] · [[diagrama-pipeline-superscalar-ejecucion-fuera-de-orden-con-r]]
