---
tipo: "receta"
titulo: "Simulación Tomasulo con especulación: parámetros clave y restricciones de temporización"
temas: ["ac", "especulacion", "mips64", "rob", "simulacion", "tomasulo"]
claves: ["Tomasulo especulación", "ROB 4 entradas", "reservation stations 2/unidad", "load buffer 2", "latencias FP", "CDB", "recurso libre siguiente ciclo"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2022.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[especulacion]] · [[mips64]] · [[rob]] · [[simulacion]] · [[tomasulo]]

Parámetros fijos del enunciado: LD/ST exec=1c, FP MUL=6c, FP ADD=4c, ROB=4 entries, 2 RS por unidad FP, 2 load buffers. Restricciones críticas: 1) Write-back en CDB en ciclo N → dependent exec puede empezar en N+1 (no en N). 2) Recurso liberado en ciclo N → disponible en N+1. 3) Especulación: instrucciones tras salto prediccionado entran en ROB/RS, se marcan especulativas. 4) Excepción/fallo predicción → flush ROB, poison bits. Tabla a rellenar: Emisión (inicio/fin), Ejecución (inicio/fin), Escritura Resultados (inicio/fin).

> La etapa de ejecución de una instrucción que está esperando un resultado no puede comenzar en el mismo ciclo en el que se escribe el resultado en el CDB (Common Data Bus). Un recurso que se libera en un ciclo de reloj no puede usarse hasta el siguiente ciclo de reloj.
> — `repo:datos/temarios/AC/examenes/Enero2022.pdf` (cita sin comprobar)

Relacionado: [[configuracion-tomasulo-con-especulacion-para-examen-enero-20]] · [[contenido-de-una-estacion-de-reserva-en-tomasulo]] · [[buffers-de-carga-y-almacenamiento-en-tomasulo]] · [[parametros-de-simulacion-tomasulo-especulativo-para-mips64-e]] · [[simulacion-tomasulo-con-especulacion-parametros-de-hardware]] · [[parametros-de-tomasulo-con-especulacion-para-problema-2-exam]]
