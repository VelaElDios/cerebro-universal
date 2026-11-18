---
tipo: "decision"
titulo: "Configuración de recursos para Tomasulo básico en examen June 2021 (2 RS/FU, 2 load buffers, 1 store buffer)"
temas: ["ac", "pipeline", "tomasulo"]
claves: ["reservation station", "load buffer", "store buffer", "functional unit"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2021.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]] · [[tomasulo]]

Parámetros estructurales para la parte 2 (Tomasulo básico sin especulación): 2 estaciones de reserva por cada unidad funcional (asumiendo al menos una FP add y una FP mul), buffer de carga con 2 entradas, buffer de almacenamiento con 1 entrada. Todos vacíos inicialmente. Esto limita el paralelismo: solo 2 cargas simultáneas, 1 store en vuelo, y 2 operaciones por tipo de unidad funcional. La instrucción S.D (store) debe esperar entrada en store buffer; las 3 cargas compiten por 2 load buffers; las 2 MUL.D compiten por 2 RS de multiplicador; la ADD.D usa RS de sumador.

> There are two reservation stations per functional unit, a load buffer with 2 entries and a store buffer with 1 entry. All of them are initially empty.
> — `repo:datos/temarios/AC/examenes/June2021.pdf`

Relacionado: [[buffers-de-carga-y-almacenamiento-en-tomasulo]] · [[configuracion-de-procesador-tomasulo-con-especulacion-del-ej]]
