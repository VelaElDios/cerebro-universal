---
tipo: "concepto"
titulo: "Predictor correlacionado (1,2): BHR = 11 tras dos saltos tomados"
temas: ["ac", "bhr", "correlacionado", "prediccion-saltos"]
claves: ["predictor correlacionado", "BHR", "history register", "saltos tomados"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2019.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[bhr]] · [[correlacionado]] · [[prediccion-saltos]]

Un predictor (m, n) usa m bits de historia local y n bits de historia global (BHR). Aquí (1,2): BHR de 2 bits. Si los dos últimos saltos fueron tomados (T), el BHR se actualiza desplazando e insertando 1 por cada tomado → "11". Respuesta correcta: b.

> In a (1, 2) correlating predictor where the two last executed branches were taken, the value of the BHR is… a) 10 b) 11 c) 00 d) None of the above
> — `repo:datos/temarios/AC/examenes/June2019.pdf`

Relacionado: [[predictor-correlacionado-2-1-bhr-tras-dos-saltos-tomados-des]] · [[interpretacion-del-bhr-en-predictor-correlativo-2-3]] · [[interpretacion-del-bhr-en-predictor-correlacionado-m-n-test]]
