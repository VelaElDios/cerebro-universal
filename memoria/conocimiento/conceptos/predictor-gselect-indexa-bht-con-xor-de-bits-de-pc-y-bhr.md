---
tipo: "concepto"
titulo: "Predictor gselect: indexación de BHT mediante XOR de bits de PC y BHR"
temas: ["ac", "bht", "gselect", "prediccion-saltos"]
claves: ["gselect", "predictor", "BHT", "XOR", "PC", "BHR", "indexado", "predictor correlacionado"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2015.pdf", "repo:datos/temarios/AC/examenes/Enero2015.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[bht]] · [[gselect]] · [[prediccion-saltos]]

Temas: [[ac]] · [[bht]] · [[gselect]] · [[prediccion-saltos]]

El predictor **gselect** (global selection) combina el historial global de saltos (BHR) con **algunos bits del PC** mediante una operación **XOR** para indexar la tabla de patrones (BHT/PHT). Esto permite distinguir contextos de salto diferentes que compartan el mismo historial global.

**Diferencia clave con gshare:** gshare usa XOR del PC completo (o más bits) con el BHR completo; gselect usa solo una parte del PC.

**Pregunta de examen (Junio 2015):**
> El predictor gselect indexa la BHT con los bits que resultan de:
> — `repo:datos/temarios/AC/examenes/Junio2015.pdf`
> **Opción correcta:** b) XOR de algunos bits del PC y BHR.

**Pregunta de examen (Enero 2015):**
> El predictor gselect indexa la BHT con los bits que resultan de:
> a) AND de algunos bits del PC y BHR
> b) XOR de algunos bits del PC y BHR
> c) Concatenar algunos bits de PC y BHR
> d) Ninguna es correcta
> — `repo:datos/temarios/AC/examenes/Enero2015.pdf`
> **Opción correcta:** b) XOR de algunos bits del PC y BHR.

Relacionado: [[bht-branch-history-table-tabla-separada-para-bits-de-predicc]] · [[bht-en-predictor-dinamico-de-3-bits-contadores-de-saturacion]] · [[predictor-gselect-indice-mediante-xor-de-bits-de-pc-y-bhr]] · [[predictor-gselect-concatenacion-vs-gshare-xor-para-indexar-b]] · [[seleccion-de-entrada-en-bht-branch-history-table]]

> El predictor gselect indexa la BHT con los bits que resultan de:
> — `repo:datos/temarios/AC/examenes/Junio2015.pdf`
> El predictor gselect indexa la BHT con los bits que resultan de: a) AND de algunos bits del PC y BHR b) XOR de algunos bits del PC y BHR c) Concatenar algunos bits de PC y BHR d) Ninguna es correcta
> — `repo:datos/temarios/AC/examenes/Enero2015.pdf`

Fusionada con: Predictor gselect indexa la BHT con XOR de bits del PC y del BHR
