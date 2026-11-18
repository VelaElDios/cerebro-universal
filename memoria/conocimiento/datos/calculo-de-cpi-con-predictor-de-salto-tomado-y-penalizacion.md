---
tipo: "dato"
titulo: "Cálculo de CPI con predictor de salto tomado y penalización por fallo"
temas: ["ac", "cpi", "penalizacion", "prediccion-saltos", "predictor-estatico"]
claves: ["CPI", "predictor salto tomado", "fallo predicción", "penalización 2 ciclos", "frecuencia saltos"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2011.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[cpi]] · [[penalizacion]] · [[prediccion-saltos]] · [[predictor-estatico]]

Fórmula general: CPI = CPI_base + (frecuencia_saltos × tasa_fallo × penalización). En el ejemplo: CPI_base = 1 (segmentado ideal), frecuencia_saltos = 0.2, predictor "siempre tomado" acierta en saltos tomados (70%) y falla en no tomados (30%), penalización = 2 ciclos. CPI = 1 + 0.2 × 0.3 × 2 = 1.12. La opción correcta es la c).

> Un computador segmentado de 5 etapas con predictor de salto tomado, ejecuta un código con un 20% de saltos, de los cuales el 70% de saltos es tomado. Se usa un predictor de saltos en el que si se acierta no se pierde ningún ciclo, pero si no se acierta se pierden 2 ciclos. El CPI del sistema será: a) CPI=0,8*1+0,2*0,7*3 b) CPI=0,8*1+0,2*0,3*2 c) CPI= 1*1 +0,2*0,3*2 d) Ninguna de las anteriores
> — `repo:datos/temarios/AC/examenes/Junio2011.pdf`

Relacionado: [[cpi-con-tecnica-parar-siempre-en-saltos-cpi-1-saltos-tomados]] · [[calculo-de-speedup-comparando-predictor-con-penalidad-variab]] · [[calculo-de-cpi-base-en-pipeline-con-penalizacion-por-saltos]]
