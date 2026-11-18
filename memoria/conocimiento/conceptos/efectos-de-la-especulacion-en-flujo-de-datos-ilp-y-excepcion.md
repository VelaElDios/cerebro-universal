---
tipo: "concepto"
titulo: "Efectos de la especulación en flujo de datos, ILP y excepciones"
temas: ["ac", "bits-venenosos", "especulacion", "excepciones", "ilp", "renombramiento"]
claves: ["especulacion", "renombramiento registros", "paralelismo instruccion", "excepciones diferidas"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2017.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[bits-venenosos]] · [[especulacion]] · [[excepciones]] · [[ilp]] · [[renombramiento]]

La especulación (ejecución de instrucciones antes de saber si son necesarias) usa renombramiento de registros para evitar dependencias falsas (WAR/WAW) y permitir fuera de orden → afecta al flujo de datos (a) y aumenta ILP (b). No evita excepciones; las retrasa con bits venenosos hasta commit (c es falsa). Las opciones a y b son verdaderas, pero en examen de opción única suele primar la más completa: «Incrementa el paralelismo a nivel de instrucción y computador» (b).

> La especulación: a) Afecta al flujo de datos del programa haciendo uso de renombramiento b) Incrementa el paralelismo a nivel de instrucción y computador c) Evita que se produzcan excepciones d) Ninguna es correcta
> — `repo:datos/temarios/AC/examenes/Junio2017.pdf`

Relacionado: [[bits-venenosos-en-carga-especulativa-excepcion-diferida-hast]] · [[bits-venenosos-en-especulacion-excepcion-no-recuperable-marc]] · [[buffer-de-reordenamiento-rob-en-tomasulo-con-especulacion-ca]]
