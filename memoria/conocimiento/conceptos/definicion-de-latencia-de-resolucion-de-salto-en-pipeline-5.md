---
tipo: "concepto"
titulo: "Definición de latencia de resolución de salto en pipeline 5 etapas IF/ID/EX/MEM/WB"
temas: ["ac", "pipeline", "prediccion-saltos"]
claves: ["salto condicional", "salto incondicional", "dirección conocida MEM", "sentido conocido EX", "dirección conocida ID"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2016.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]] · [[prediccion-saltos]]

En este pipeline de 5 etapas: Salto condicional: dirección objetivo lista al final de MEM, condición (tomado/no tomado) lista al final de EX. Si se predice no tomado y resulta tomado, se detecta en EX pero la dirección no se sabe hasta MEM → penalidad efectiva 3 ciclos (burbujas en IF, ID, EX mientras se resuelve). Salto incondicional: dirección objetivo lista al final de ID. Si se predice no tomado (secuencial) y es tomado, se detecta en ID → penalidad 1 ciclo (burbuja en IF). Estas latencias determinan la penalidad base por fallo de predicción sin BTB.

> Tenemos un procesador segmentado con 5 etapas IF, ID, EX, MEM y WB, donde para una instrucción de salto condicional la dirección del salto es conocida al final de la etapa MEM y el sentido al final de la etapa EX, y para una instrucción de salto incondicional la dirección del salto es conocida al final de la etapa ID.
> — `repo:datos/temarios/AC/examenes/Junio2016.pdf`

Relacionado: [[alternativas-de-deteccion-de-instruccion-de-salto-en-pipelin]] · [[accion-del-procesador-ante-fallo-de-prediccion-de-salto]]
