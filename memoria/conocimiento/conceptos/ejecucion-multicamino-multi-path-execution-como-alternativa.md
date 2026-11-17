---
tipo: "concepto"
titulo: "Ejecución multicamino (multi-path execution) como alternativa a la predicción"
temas: ["ac", "ejecucion-multicamino", "ibm", "mainframes", "prediccion-saltos"]
claves: ["multicamino", "ambas ramas", "cancelar", "especulativo", "IBM mainframes", "investigación"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[ejecucion-multicamino]] · [[ibm]] · [[mainframes]] · [[prediccion-saltos]]

Técnica que evita predecir: el procesador **ejecuta ambas ramas** del salto de forma especulativa en paralelo. Cuando la condición del salto se resuelve, se confirman los resultados del camino correcto y se **cancelan (squash)** los del camino incorrecto.
- **Ventaja**: cero fallos de predicción (CPI ideal en saltos).
- **Coste**: duplica (o más) el consumo de recursos (unidades funcionales, ancho de banda, energía) mientras ambas ramas corren.
- **Implementación real**: muy rara; solo algunos mainframes IBM y prototipos de investigación la han incluido. No es viable en procesadores de propósito general por coste de hardware y energía.

> Se ejecutan las dos ramas de una bifurcación sin hacer predicción Cuando se resuelve el salto, se cancelan las instrucciones del camino no tomado Raramente implementado • IBM mainframes y proyectos de investigación
> — `repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4.pdf` (cita sin comprobar)

Relacionado: [[instrucciones-predicadas-convertir-dependencias-de-control-e]]
