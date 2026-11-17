---
tipo: "concepto"
titulo: "Predictor dinámico de 2 bits (Jim Smith, 1981): máquina de 4 estados y inercia"
temas: ["ac", "arquitectura-computadores", "prediccion-saltos"]
claves: ["predictor 2 bits", "Jim Smith 1981", "máquina 4 estados", "contador saturado", "inercia predicción"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[arquitectura-computadores]] · [[prediccion-saltos]]

El predictor de 2 bits implementa una máquina de 4 estados con inercia: fuertemente no tomado (00), débilmente no tomado (01), débilmente tomado (10), fuertemente tomado (11). La predicción se basa en el bit más significativo del contador saturado de 2 bits: 0 predice no tomado, 1 predice tomado. Los estados débiles dan una "segunda oportunidad" antes de cambiar la predicción, evitando cambios bruscos por ejecuciones atípicas únicas. Se inicializa en "débilmente no tomado" (01).

> Una segunda oportunidad antes de cambiar la predicción (inercia) • Usa dos bits de predicción por cada instrucción de salto • Los bits reflejan el comportamiento de las últimas ejecuciones del salto • IDEA: Un salto se predice Tomado si fue tomado repetidamente y No tomado si repetidamente fue no tomado • Si un salto toma una dirección inusual una sola vez, se mantiene la predicción de la dirección usual
> — `repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4.pdf`
