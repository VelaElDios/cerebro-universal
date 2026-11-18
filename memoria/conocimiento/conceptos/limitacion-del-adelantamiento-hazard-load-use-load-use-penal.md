---
tipo: "concepto"
titulo: "Limitación del adelantamiento: hazard load-use (load-use penalty)"
temas: ["ac", "hazard", "latencia carga", "load-use", "pipeline"]
claves: ["LD no tiene dato hasta final MEM", "DSUB lo necesita al principio", "detección hardware", "stall"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema2-Paralelismo a nivel de instruccion/Tema2-2026-2027.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[hazard]] · [[latencia carga]] · [[load-use]] · [[pipeline]]

Una instrucción de carga (LD) solo tiene el dato al final de la etapa MEM. La instrucción siguiente que usa ese registro (ej. DSUB) lo necesita al inicio de EX. El forwarding no llega a tiempo porque el dato aún no existe. Solución: hardware de detección de hazard load-use que inserta **una burbuja (stall)** deteniendo el pipeline un ciclo; la carga continúa, el consumidor y siguientes esperan. En RISC-V de 5 etapas clásico, la penalidad load-use es **1 ciclo de stall**.

> Desafortunadamente no todos los riesgos de datos se pueden resolver por adelantamiento • LD no tiene el dato hasta final MEM; DSUB lo necesita al principio • Las instrucciones de carga tienen un retraso o latencia que no se puede eliminar con adelantamiento • Necesitamos añadir un hardware para detectar los riesgos de datos y provocar una detención • la instrucción que debe producir el dato continuará, pero la que debe consumirlo y las siguientes se detendrán hasta que el dato esté disponible
> — `repo:datos/temarios/AC/Tema2-Paralelismo a nivel de instruccion/Tema2-2026-2027.pdf` (cita sin comprobar)

Relacionado: [[adelantamiento-forwarding-para-riesgos-raw]] · [[riesgo-load-use-en-pipeline-mips-con-forwarding]] · [[dependencia-de-datos-en-pipeline-riesgo-solo-si-instruccione]]
