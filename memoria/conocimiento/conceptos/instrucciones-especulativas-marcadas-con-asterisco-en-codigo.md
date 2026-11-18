---
tipo: "concepto"
titulo: "Instrucciones especulativas marcadas con asterisco en código MIPS64"
temas: ["ac", "pipeline", "tomasulo"]
claves: ["especulativa", "L.D*", "ADD.D*", "BNEZ", "poison bits", "planificación estática"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2025.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]] · [[tomasulo]]

En el fragmento de código del ejercicio, las instrucciones L.D F2, 0(R2) y ADD.D F6, F0, F2 llevan un asterisco (*) indicando que son especulativas. Esto significa que se ejecutan antes de saber si el salto BNEZ R1, salto se tomará o no. En planificación estática con poison bits, estas instrucciones no deben causar excepciones inmediatas ante fallos (ej. dirección prohibida), sino marcar registros destino como "sucios". La instrucción ADD.D F6, F0, F4 (sin asterisco) y S.D F6, 0(R3) son no especulativas (en el camino correcto tras resolver el salto).

> Las instrucciones marcadas con * son especulativas.
> — `repo:datos/temarios/AC/examenes/Junio2025.pdf`

Relacionado: [[planificacion-estatica-con-poison-bits-en-mips64-reglas-de-e]] · [[bits-venenosos-en-carga-especulativa-excepcion-diferida-hast]] · [[instrucciones-especulativas-marcadas-con-en-codigo-mips64-ex]] · [[especulacion-estatica-con-poison-bits-en-mips64-lw]]
