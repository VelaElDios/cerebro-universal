---
tipo: "concepto"
titulo: "BTB con predictores de 4 bits: campos de cada entrada"
temas: ["ac", "btb", "prediccion-saltos"]
claves: ["BTB", "Branch Target Buffer", "predictor 4 bits", "campos entrada"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2012.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[btb]] · [[prediccion-saltos]]

Una entrada de BTB (Branch Target Buffer) que integra predicción de dirección y sentido típicamente contiene: 1) Etiqueta (tag): bits altos de la PC de la instrucción de salto para identificar la entrada (coincidencia). 2) Dirección de destino (target address): PC calculada del salto tomado (para saltos condicionales e incondicionales). 3) Predictor de 4 bits: autómata de 4 estados (ej. 00=fuertemente NT, 01=débilmente NT, 10=débilmente T, 11=fuertemente T) que predice tomado/no tomado. 4) Bits de validez/tipo: indican si la entrada es válida y si es salto condicional, incondicional, llamada, retorno. 5) Opcional: historia local o global si el predictor es híbrido/correlacionado, pero con predictor de 4 bits simple no hace falta.

> Si se emplease una BTB y predictores de 4 bits para predecir el sentido de las instrucciones de salto condicional, indica qué campos que contendría cada entrada.
> — `repo:datos/temarios/AC/examenes/Enero2012.pdf`

Relacionado: [[predictor-de-1-bit-inicializado-a-no-tomado-en-bucle-secuenc]]
