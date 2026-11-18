---
tipo: "concepto"
titulo: "Penalización de salto en MIPS resuelto en ID sin predicción"
temas: ["ac", "mips", "pipeline", "prediccion-saltos"]
claves: ["branch penalty", "ID stage", "salto retardado", "branch delay slot"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2011.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[mips]] · [[pipeline]] · [[prediccion-saltos]]

Si la dirección y el sentido del salto se calculan en ID, la instrucción siguiente (en IF) ya se ha cogido. Si el salto se toma, esa instrucción es incorrecta y hay que anularla: 1 ciclo de penalización (burbuja). Si no se toma, continua sin penalización.

> Tienen una penalización de 1 ciclo
> — `repo:datos/temarios/AC/examenes/Enero2011.pdf`

Relacionado: [[penalizacion-de-salto-en-mips-con-resolucion-en-id-y-salto-r]] · [[prediccion-fija-siempre-no-tomado-con-calculo-destino-en-id]] · [[penalizacion-de-salto-condicional-en-pipeline-de-5-etapas-re]]
