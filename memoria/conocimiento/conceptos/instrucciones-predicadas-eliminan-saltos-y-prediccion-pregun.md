---
tipo: "concepto"
titulo: "Instrucciones predicadas: eliminan saltos y predicción (pregunta 14)"
temas: ["ac", "epics", "instrucciones-predicadas", "prediccion-saltos"]
claves: ["instrucciones predicadas", "predicado", "salto", "penalización", "EPIC"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2017.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[epics]] · [[instrucciones-predicadas]] · [[prediccion-saltos]]

Las instrucciones predicadas (predication) convierten dependencias de control en dependencias de datos: cada instrucción lleva un bit de predicado; si es 1 se ejecuta, si es 0 se anula (no-op). Esto elimina la instrucción de salto y, por tanto, la necesidad de predecirla (respuesta c). La a) es cierta pero no la definición principal; la b) describe ejecución multicamino (multi-path), no predicación. Usado en arquitectura EPIC/IA64 (Itanium).

> Indicate the correct statement: a) Predicated instructions reduce the misprediction recovery penalty b) Predicated instructions execute both branch directions, without prediction c) Predicated instructions eliminate branch instructions (and the corresponding prediction) d) None of the above
> — `repo:datos/temarios/AC/examenes/January2017.pdf`

Relacionado: [[arquitectura-epic-ia64-y-procesadores-itanium]] · [[instrucciones-predicadas-convertir-dependencias-de-control-e]] · [[arquitectura-que-implementa-instrucciones-predicadas-de-form]] · [[salto-retardado-y-instrucciones-predicadas-como-alternativas]]
