---
tipo: "dato"
titulo: "Configuración hardware Tomasulo con especulación para examen Enero 2016 Problema 3"
temas: ["ac", "especulacion", "mips64", "tomasulo"]
claves: ["ROB 6 entradas", "buffer carga 1", "reserva suma FP 1", "reserva multiplicación FP 1", "reserva división FP 2", "BDC", "ciclos"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2016.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[especulacion]] · [[mips64]] · [[tomasulo]]

El procesador MIPS64 del examen tiene: ROB (Reorder Buffer) de 6 entradas; 1 Load Buffer; 1 Reservation Station para FP Add; 1 Reservation Station para FP Multiply; 2 Reservation Stations para FP Divide. Las unidades funcionales y sus latencias: FP Add (1 unidad, 2 ciclos, segmentada), FP Multiply (1 unidad, 6 ciclos, segmentada), FP Divide (1 unidad, 10 ciclos, no segmentada), LOAD/STORE (1 unidad, 2 ciclos, segmentada), INT ALU (1 unidad, 1 ciclo, no segmentada).

> El sistema cuenta con un ROB de 6 entradas, 1 buffer de carga, 1 estación de reserva para la suma FP, otra para la multiplicación FP y 2 para la división FP.
> — `repo:datos/temarios/AC/examenes/Enero2016.pdf`

Relacionado: [[configuracion-tomasulo-con-especulacion-para-examen-enero-20]] · [[algoritmo-tomasulo-origen-y-objetivo-cpi1]] · [[configuracion-tomasulo-con-especulacion-del-examen-ac-junio]] · [[configuracion-de-tomasulo-con-especulacion-para-examen-ac-ju]]
