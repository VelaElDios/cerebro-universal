---
tipo: "concepto"
titulo: "Estructuras hardware para predicción de saltos (BTAC, BHT, BTB, I-caché con índice sucesor)"
temas: ["ac", "arquitectura", "prediccion-saltos"]
claves: ["BTAC", "BHT", "BTB", "Branch Target Address Cache", "Branch History Table", "Branch Target Buffer", "índice sucesor", "I-caché"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[arquitectura]] · [[prediccion-saltos]]

El documento clasifica las estructuras hardware en dos categorías: (1) dónde guardar la dirección destino del salto: BTAC (caché dedicada) o I-caché con campo "índice sucesor" por línea; (2) dónde guardar los bits de predicción: BHT (tabla separada), bits en la I-caché, o BTB (que fusiona BTAC y bits de predicción en una sola estructura). La BTB es una BTAC que además lleva bits de predicción por entrada.

> Soporte hardware usado por las técnicas de predicción de saltos: Estructuras de predicción: ¿Dónde almacenar la dirección destino del salto? BTAC (Branch Target Address Cache) I-Cache (con índice sucesor) ¿Dónde almacenar los bits de predicción? BTB (Branch Target Buffer) (BTAC + bits predicción) BHT (Branch History Table) Bits de predicción en la I-cache
> — `repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4.pdf` (cita sin comprobar)

Relacionado: [[algoritmo-tomasulo-origen-y-objetivo-cpi1]] · [[alternativas-de-deteccion-de-instruccion-de-salto-en-pipelin]]
