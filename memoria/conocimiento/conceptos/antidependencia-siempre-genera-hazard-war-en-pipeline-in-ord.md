---
tipo: "concepto"
titulo: "Antidependencia siempre genera hazard WAR en pipeline in-order"
temas: ["ac", "dependencias", "pipeline"]
claves: ["antidependencia", "WAR", "hazard", "pipeline"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2018.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[dependencias]] · [[pipeline]]

Una antidependencia (WAR - Write After Read) ocurre cuando una instrucción escribe en un registro/ubicación que una instrucción anterior necesita leer. En pipelines in-order sin renombramiento, esto siempre genera un hazard WAR porque la escritura posterior podría sobrescribir el valor antes de que la instrucción anterior lo haya leído. La respuesta correcta es c) Riesgo WAR.

> Toda antidependencia produce siempre un: a) Riesgo WAW b) RAW c) WAR d) Ninguna es correcta
> — `repo:datos/temarios/AC/examenes/Junio2018.pdf` (cita sin comprobar)

Relacionado: [[antidependencia-war-en-bucle-entre-carga-y-actualizacion-de]] · [[antidependencia-war-siempre-genera-hazard-war]] · [[antidependencia-entre-iteraciones-en-bucle-con-store-y-actua]] · [[que-es-un-riesgo-war-y-a-que-dependencia-corresponde]] · [[hazard-war-corresponde-a-antidependencia-dependencia-de-nomb]]
