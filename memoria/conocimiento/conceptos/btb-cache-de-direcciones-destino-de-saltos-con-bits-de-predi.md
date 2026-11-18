---
tipo: "concepto"
titulo: "BTB: cache de direcciones destino de saltos con bits de predicción"
temas: ["ac", "btb", "prediccion-saltos"]
claves: ["BTB", "Branch Target Buffer", "cache instrucciones", "bits predicción"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2018.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[btb]] · [[prediccion-saltos]]

La Branch Target Buffer (BTB) es una caché que almacena la dirección destino (target) de instrucciones de salto tomadas recientemente, junto con bits de predicción. Permite obtener el target en la etapa fetch sin esperar a decode. La opción a) describe una estructura híbrida (BTB + BHT separada). La opción c) describe bits de predicción en la I-cache. La BTB típica integra target y predicción en una misma entrada cacheada. Respuesta correcta: d) Ninguna es correcta (ninguna describe exactamente la BTB estándar).

> La BTB: a) Almacena en una tabla la dirección destino para las últimas instrucciones de salto y, en una tabla diferente, los bits de predicción para todas las instrucciones de salto condicionales. b) Es una memoria cache que almacena solamente los bits de predicción de los últimos saltos tomados c) Añade a la cache de instrucciones los bits de predicción que se usan cuando la instrucción es un salto condicional d) Ninguna es correcta
> — `repo:datos/temarios/AC/examenes/Junio2018.pdf`

Relacionado: [[actualizacion-de-la-btb-tras-ejecutar-el-salto]] · [[ancho-y-tamano-en-bits-de-un-btb-implicito-con-1024-entradas]] · [[estructura-que-almacena-direccion-destino-de-saltos-tomados]] · [[estructura-de-btb-tabla-de-destinos-y-tabla-separada-de-bits]] · [[proposito-del-branch-target-buffer-btb-ademas-de-bits-de-pre]]
