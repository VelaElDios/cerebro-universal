---
tipo: "receta"
titulo: "CPI con técnica 'parar siempre' en saltos: CPI = 1 + (%saltos * %tomados * penalización)"
temas: ["ac", "cpi", "parar-siempre", "pipeline", "prediccion-saltos"]
claves: ["CPI", "parar siempre", "saltos condicionales", "penalización", "20%", "70%"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2012.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[cpi]] · [[parar-siempre]] · [[pipeline]] · [[prediccion-saltos]]

Técnica "parar siempre" = asumir no tomado y detener el pipeline hasta resolver. Penalización = 1 ciclo (pregunta 16). % saltos = 20%, % tomados = 70%. Ciclos extra por instrucción = 0.20 * 0.70 * 1 = 0.14. CPI = 1 + 0.14 = 1.14 → respuesta d) Ninguna de las anteriores (1.14 no está en opciones).

> Se usa la técnica de parar siempre y se asume un CPI de 1 para todas las instrucciones a excepción de los saltos condicionales. a) El CPI es 1,4 b) El CPI es 1,2 c) El CPI es 1 d) Ninguna de las anteriores
> — `repo:datos/temarios/AC/examenes/Junio2012.pdf`

Relacionado: [[penalizacion-de-salto-condicional-en-pipeline-de-5-etapas-re]] · [[accion-del-procesador-ante-fallo-de-prediccion-de-salto]] · [[calculo-de-cpi-con-predictor-de-salto-tomado-y-penalizacion]] · [[cpi-con-prediccion-de-saltos-en-pipeline-de-5-etapas-direcci]] · [[cpi-en-pipeline-con-penalizacion-por-saltos-tomados-y-delay]]
