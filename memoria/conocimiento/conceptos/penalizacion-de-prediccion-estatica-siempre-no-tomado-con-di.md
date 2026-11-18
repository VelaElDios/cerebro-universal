---
tipo: "concepto"
titulo: "Penalización de predicción estática \"siempre no tomado\" con dirección en ID y sentido en EX"
temas: ["ac", "pipeline", "prediccion-saltos"]
claves: ["predicción estática", "siempre no tomado", "dirección destino ID", "sentido EX", "penalización"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2013.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]] · [[prediccion-saltos]]

Si el predictor estático "siempre no tomado" acierta (salto no tomado), la instrucción siguiente ya está en pipeline y solo hay 1 ciclo de penalización por el cálculo de dirección en ID (burbuja). Si falla (salto tomado), se deben anular las instrucciones fetchadas incorrectamente y redirigir a la dirección calculada en ID, lo que cuesta 2 ciclos de penalización.

> En una implementación segmentada de MIPS en la que la dirección de destino de los saltos se calcula en la etapa ID y el sentido de los saltos se resuelve en la etapa EX, la estrategia de predicción fija "siempre no tomado": a. Tiene una penalización de 1 ciclo en caso de acierto y de 2 ciclos en caso de fallo
> — `repo:datos/temarios/AC/examenes/Junio2013.pdf`

Relacionado: [[bht-con-contadores-de-saturacion-de-2-bits-pregunta-17]] · [[prediccion-fija-siempre-no-tomado-con-calculo-destino-en-id]] · [[penalizacion-de-salto-en-mips-resuelto-en-id-sin-prediccion]] · [[penalizacion-de-salto-tomado-con-condicion-en-ex-y-direccion]]
