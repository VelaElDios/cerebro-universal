---
tipo: "concepto"
titulo: "Definición de bloque básico en paralelismo a nivel de instrucción (pregunta 6)"
temas: ["ac", "bloque-basico", "ilp", "salto", "pipeline"]
claves: ["basic block", "instrucciones", "salto", "dependencias"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2022.pdf", "repo:datos/temarios/AC/examenes/Junio2011.pdf", "repo:datos/temarios/AC/examenes/Noviembre2014A.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[bloque-basico]] · [[ilp]]

Un basic block es una secuencia de instrucciones consecutivas sin saltos ni etiquetas de entrada/salida en medio; es decir, entre dos instrucciones de salto (o inicio/fin de programa). Opción b correcta.

> In the realm of instruction-level parallelism, the term \"basic block\" refers to: a) A sequence of branch instructions b) A sequence of instructions between two branch instructions c) A sequence of instructions between which there are no dependencies d) None of the above
> — `repo:datos/temarios/AC/examenes/June2022.pdf`

Relacionado: [[bucle-vectorial-de-referencia-para-desenrollado-y-planificac]] · [[que-es-un-bloque-basico-basic-block-en-ilp]] · [[definiciones-clave-basic-block-antidependencia-loop-unrollin]] · [[definicion-de-bloque-basico-test-ac-q7]]

## Ampliación (2026-11-18, )
Un bloque básico es una secuencia de instrucciones consecutivas que no contiene saltos (ni condicionales ni incondicionales) en su interior, salvo posiblemente al final. Es la unidad básica para la planificación local y la predicción de saltos.

## Ampliación (2026-11-18, )
Un bloque básico es una secuencia de instrucciones consecutivas sin saltos ni etiquetas en medio; solo la primera instrucción puede ser destino de un salto y solo la última puede ser un salto. El tamaño medio del bloque básico limita el ILP explotable sin predicción de saltos.
