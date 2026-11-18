---
tipo: "dato"
titulo: "Latencias y grado de superescalaridad del Problema 3 AC Junio 2011"
temas: ["ac", "latencias", "parametros-procesador", "pipeline", "superescalar"]
claves: ["grado 2", "MEM 2 ciclos", "EX 2 ciclos", "adelantamiento", "superscalar"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2011.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[latencias]] · [[parametros-procesador]] · [[pipeline]] · [[superescalar]]

Parámetros fijos del problema: Superescalar grado 2 (emisión dual). Latencia MEM = 2 ciclos para instrucciones LW. Latencia EX = 2 ciclos para ADD/SUB. Adelantamiento (forwarding) disponible. Sin especificación de latencia para etapas IF, ID, WB (se asumen 1 ciclo cada una típicamente). Ventana de instrucciones ilimitada para apartados b y c.

> El procesador invierte 2 ciclos para la etapa MEM en las cargas y 2 ciclos para completar la etapa EX de las operaciones aritméticas. Además, implementa adelantamiento.
> — `repo:datos/temarios/AC/examenes/Junio2011.pdf`

Relacionado: [[ancho-y-tamano-en-bits-de-un-btb-implicito-con-1024-entradas]] · [[bucle-vectorial-de-referencia-para-desenrollado-y-planificac]] · [[latencias-de-etapas-memoria-y-ejecucion-en-superescalar-exam]] · [[planificacion-en-superescalar-grado-2-con-latencias-mem-2-y]] · [[parametros-de-pipeline-superescalar-mem-2-ciclos-ex-3-ciclos]]
