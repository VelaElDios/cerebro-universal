---
tipo: "receta"
titulo: "Penalización de salto tomado con condición en EX y dirección en MEM"
temas: ["ac", "pipeline", "prediccion-saltos"]
claves: ["penalización salto", "etapa EX", "etapa MEM", "pipeline 5 etapas"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2025.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]] · [[prediccion-saltos]]

Si la condición se evalúa en EX (fin de EX se sabe si tomado) pero la dirección destino no está lista hasta fin de MEM, el pipeline debe esperar la dirección. Instrucciones siguientes en IF/ID/EX se descartan. Penalización = 3 ciclos (burbujas en IF, ID, EX mientras salto en MEM). Opción correcta: c. 3 ciclos.

> En un pipeline de 5 etapas, si la condición del salto se comprueba en la etapa EX y la dirección destino del salto se calcula en MEM, ¿cuántos ciclos de penalización se introducen por salto tomado?
> — `repo:datos/temarios/AC/examenes/Junio2025.pdf`

Relacionado: [[alternativas-de-deteccion-de-instruccion-de-salto-en-pipelin]] · [[actualizacion-de-la-btb-tras-ejecutar-el-salto]]
