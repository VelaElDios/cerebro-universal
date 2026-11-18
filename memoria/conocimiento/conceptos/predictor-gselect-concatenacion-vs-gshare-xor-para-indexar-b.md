---
tipo: "concepto"
titulo: "Predictor gselect (concatenación) vs gshare (XOR) para indexar BHT"
temas: ["ac", "gselect", "gshare", "prediccion-saltos"]
claves: ["gselect", "gshare", "concatenación PC+BHR", "XOR PC+BHR", "McFarling"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[gselect]] · [[gshare]] · [[prediccion-saltos]]

Dos formas de combinar historia global (BHR) y dirección de salto (PC) para indexar una BHT global:
- gselect (GAg en notación Yeh-Patt): concatena los n bits bajos del PC con los m bits del BHR → índice de n+m bits. Ejemplo: PC[9:0] + BHR[11:0] = 22 bits.
- gshare: hace XOR bit a bit entre los n bits bajos del PC y los m bits del BHR (alineados a la derecha) → índice de n bits. Reduce interferencia (aliasing) entre saltos distintos que caen en la misma entrada.
Estudio de McFarling: gshare es algo mejor que gselect porque el XOR dispersa mejor los patrones.

> Predictor gselect: indexa la BHT concatenando bits de PC con BHR Predictor gshare: indexa la BHT con XOR de bits del PC y BHR
> — `repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4.pdf` (cita sin comprobar)

Relacionado: [[predictor-gselect-indexa-bht-con-xor-de-bits-de-pc-y-bhr]] · [[predictor-gselect-indice-mediante-xor-de-bits-de-pc-y-bhr]] · [[seleccion-de-entrada-en-bht-branch-history-table]]
