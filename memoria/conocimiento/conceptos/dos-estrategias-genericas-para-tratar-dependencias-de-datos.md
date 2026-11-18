---
tipo: "concepto"
titulo: "Dos estrategias genéricas para tratar dependencias de datos"
temas: ["ac", "dependencias-datos", "paralelismo-instruccion", "riesgos-datos"]
claves: ["mantener-dependencia-evitar-riesgo", "eliminar-dependencia-transformar-codigo", "forwarding", "renombrado", "desenrollado"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema2-Paralelismo a nivel de instruccion/Tema2-2026-2027.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[dependencias-datos]] · [[paralelismo-instruccion]] · [[riesgos-datos]]

Frente a una dependencia de datos real (RAW), la primera vía conserva la dependencia lógica pero evita el riesgo mediante técnicas hardware (forwarding/bypass, detección de riesgos y parada, predicción de valores) o software (planificación de instrucciones). La segunda vía elimina la dependencia reescribiendo el código: renombrado de registros (para WAR/WAW), desenrollado de bucles, inversión de bucles, cambio de algoritmo, etc.

> Hay dos formas de tratarlas: Mantener la dependencia pero evitar el riesgo; Eliminar la dependencia transformando el código
> — `repo:datos/temarios/AC/Tema2-Paralelismo a nivel de instruccion/Tema2-2026-2027.pdf` (cita sin comprobar)

Relacionado: [[renombrado-de-registros-para-eliminar-dependencias-de-nombre]] · [[eliminacion-de-dependencias-de-control-mediante-desenrollado]] · [[las-dependencias-de-datos-no-siempre-generan-riesgos-y-se-el]] · [[tipos-de-dependencia-y-riesgos-asociados-en-segmentacion]] · [[dependencia-de-datos-en-pipeline-riesgo-solo-si-instruccione]]
