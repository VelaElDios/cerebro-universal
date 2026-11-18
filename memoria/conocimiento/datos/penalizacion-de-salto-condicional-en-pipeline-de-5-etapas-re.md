---
tipo: "dato"
titulo: "Penalización de salto condicional en pipeline de 5 etapas resuelto en ID = 1 ciclo"
temas: ["ac", "penalizacion", "pipeline", "prediccion-saltos"]
claves: ["pipeline 5 etapas", "ID", "salto condicional", "penalización", "1 ciclo"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2012.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[penalizacion]] · [[pipeline]] · [[prediccion-saltos]]

Si el salto se resuelve en ID, la instrucción siguiente (en IF) es la errónea cuando el salto es tomado. Se pierde 1 ciclo (burbuja) para ir a la dirección correcta. Si no se toma, no hay penalización. Penalización media = %tomados * 1 ciclo.

> Para una segmentación de 5 etapas (IF, ID, EX, MEM, WB), en la que en la etapa ID se genera la dirección destino y se resuelve la condición de salto, la penalización para los saltos condicionales es de: b) 1 ciclo
> — `repo:datos/temarios/AC/examenes/Junio2012.pdf` (cita sin comprobar)

Relacionado: [[accion-del-procesador-ante-fallo-de-prediccion-de-salto]] · [[alternativas-de-deteccion-de-instruccion-de-salto-en-pipelin]]
