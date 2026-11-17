---
tipo: "concepto"
titulo: "Actualización de la BTB tras ejecutar el salto"
temas: ["ac", "btb", "prediccion-saltos"]
claves: ["BTB", "bits predicción", "BTA", "dirección destino", "actualización"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[btb]] · [[prediccion-saltos]]

La BTB (Branch Target Buffer) se actualiza en dos pasos tras la ejecución real del salto:
1. Se actualizan los bits de predicción según el sentido real del salto (tomado/no tomado).
2. Se actualiza la BTA (Branch Target Address) con la dirección destino real del salto.
Esto permite que la predicción mejore con el historial de ejecución reciente.

> La BTB se actualiza después de ejecutar el salto y conocer – el sentido del salto (se actualizan los bits de predicción) – la dirección destino del salto (se actualiza la BTA)
> — `repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4.pdf`

Relacionado: [[btb-branch-target-buffer-fusion-de-btac-y-bits-de-prediccion]] · [[bht-branch-history-table-tabla-separada-para-bits-de-predicc]]
