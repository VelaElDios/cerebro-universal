---
tipo: "concepto"
titulo: "Trade-offs de programación branchless vs condicional"
temas: ["ac", "pipeline", "rendimiento"]
claves: ["branchless tradeoff", "cmov", "predication", "instruction count", "latency"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab4.zip!tarea4_2_branchless.cpp"]
confianza: "verificado"
fecha: "2026-11-19"
actualizado: "2026-11-19"
---

Temas: [[ac]] · [[pipeline]] · [[rendimiento]]

La versión branchless **no es siempre mejor**. Consideraciones:
- **Ventaja branchless**: tiempo constante, inmune a fallos de predicción, bueno para datos impredecibles
- **Desventaja branchless**: siempre ejecuta ambas vías (calcula `x * 0` o `x * 1`), puede aumentar instrucciones y uso de registros
- **Cuándo usar branch**: datos con patrón muy predecible (casi siempre tomado o casi nunca), predictor acierta >95%
- **Cuándo usar branchless**: datos aleatorios, patrones complejos, código en hot path donde la variabilidad de latencia es crítica
- **Arquitectura importa**: en CPUs con predicción muy buena y penalización baja, el salto puede ganar; en CPUs con penalización alta o predictores simples, branchless gana

> ¿Es siempre preferible una versión branchless en cualquier caso?
> — `repo:datos/temarios/AC/Practicas/Code_Lab4.zip!tarea4_2_branchless.cpp`

Relacionado: [[implementacion-branchless-de-suma-condicional-con-multiplica]] · [[penalizacion-de-fallo-de-prediccion-de-salto-en-pipeline]]
