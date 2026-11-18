---
tipo: "concepto"
titulo: "Planificación de trazas (trace scheduling) para condicionales en bucles"
temas: ["ac", "ilp", "planificacion-estatica", "trace-scheduling"]
claves: ["planificación de trazas", "trace scheduling", "selección de trazas", "compactación de trazas", "movimiento especulativo", "predicción estática de saltos"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[ilp]] · [[planificacion-estatica]] · [[trace-scheduling]]

Combina dos fases: (1) Selección de trazas: identifica la secuencia más probable de bloques básicos usando predicción estática de saltos y desenrollamiento para crear trazas grandes. (2) Compactación de trazas: mueve instrucciones y las empaqueta asumiendo emisión múltiple. Las dependencias de datos imponen orden parcial; los saltos son barreras. Ejemplo del texto: mover carga de B[i] antes del chequeo `if (A[i]==0)` (movimiento especulativo) si B no causa excepciones y no altera flujo de datos; mover asignación de C[i] a la rama `then` y copiarla tras `X` (o moverla antes del chequeo si posible). Requiere soporte de anulación (squashing) para instrucciones especulativas en camino no tomado.

> Técnica para generar más paralelismo cuando el cuerpo del bucle contiene estructuras condicionales internas (if-then-else)
> — `repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf`

Relacionado: [[segmentacion-software-software-pipelining-en-bucles-sin-depe]] · [[trace-scheduling-traza-secuencia-mas-probable-de-bloques-bas]] · [[que-hace-la-planificacion-de-trazas-trace-scheduling]] · [[planificacion-de-trazas-trace-scheduling-elimina-saltos-inte]]
