---
tipo: "decision"
titulo: "Configuración de recursos para Tomasulo especulativo en examen June 2021 (ROB 5 entradas, 2 RS/FU, 2 load buffers)"
temas: ["ac", "pipeline", "prediccion-saltos", "tomasulo"]
claves: ["ROB", "Reorder Buffer", "reservation station", "load buffer", "speculative"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2021.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]] · [[prediccion-saltos]] · [[tomasulo]]

Parámetros para la parte 3 (Tomasulo especulativo): ROB de 5 entradas (limita instrucciones en vuelo a 5, aunque hay 7 en la secuencia), 2 estaciones de reserva por unidad funcional, buffer de carga con 2 entradas (no se menciona store buffer explícito; el store S.D probablemente usa una entrada de ROB y buffer de store implícito o la misma estructura). Inicialmente todo vacío. La especulación implica que los resultados se escriben en ROB y no en registro arquitectónico hasta Commit; hay renombrado de registros vía ROB; las excepciones (p.ej. fallo de página en carga) se marcan con bits venenosos y se resuelven en Commit.

> There is a 5-entry ROB (initially empty). / There are 2 reservation stations per functional unit and a load buffer with 2 entries. All of them are initially empty.
> — `repo:datos/temarios/AC/examenes/June2021.pdf` (cita sin comprobar)

Relacionado: [[bits-venenosos-en-carga-especulativa-excepcion-diferida-hast]] · [[buffer-de-carga-en-tomasulo-especulativo-pregunta-18]]
