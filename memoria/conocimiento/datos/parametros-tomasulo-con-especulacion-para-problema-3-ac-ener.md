---
tipo: "dato"
titulo: "Parámetros Tomasulo con especulación para Problema 3 (AC Enero 2025)"
temas: ["ac", "cdb", "especulacion", "fp-units", "rob", "tomasulo"]
claves: ["L.S exec 1 ciclo", "MUL.S exec 5 ciclos", "ADD.S exec 2 ciclos", "CDB exclusivo", "recurso liberado disponible ciclo siguiente", "ROB", "especulación hardware"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2025.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[cdb]] · [[especulacion]] · [[fp-units]] · [[rob]] · [[tomasulo]]

Configuración exacta para simulación: Estaciones de reserva para FP Add, FP Mul, Load/Store. ROB para especulación (commit en orden). Latencias: Load/Store=1, Add=2, Mul=5. CDB: puerto único, arbitraje por orden de llegada/fin ejecución. Regla "liberado en ciclo N -> usable en ciclo N+1" aplica a unidades funcionales, registros (WB), entradas ROB, CDB.

> Tenemos un procesador MIPS64 que utiliza especulación por hardware y planificación dinámica de instrucciones mediante la técnica Tomasulo con especulación... La etapa de ejecución de carga y almacenamiento utiliza 1 ciclo. La etapa de ejecución de multiplicación en coma flotante (FP) utiliza 5 ciclos. La etapa de ejecución de la suma en coma flotante (FP) utiliza 2 ciclos. Cualquier paso de una instrucción que quiera escribir en el CDB (Common Data Bus) no puede hacerlo si otra instrucción ya lo está utilizando. En general, cualquier recurso que se libera en un ciclo de reloj no puede utilizarse hasta el siguiente ciclo de reloj.
> — `repo:datos/temarios/AC/examenes/Enero2025.pdf` (cita sin comprobar)

Relacionado: [[algoritmo-tomasulo-origen-y-objetivo-cpi1]] · [[configuracion-tomasulo-con-especulacion-para-examen-enero-20]] · [[contenido-de-una-estacion-de-reserva-en-tomasulo]] · [[parametros-de-recursos-y-latencias-para-tomasulo-con-especul]] · [[configuracion-de-procesador-tomasulo-con-especulacion-del-ej]]
