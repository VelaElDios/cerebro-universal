---
tipo: "receta"
titulo: "Simulación Tomasulo con especulación: parámetros de hardware y restricciones de ciclo"
temas: ["ac", "pipeline", "tomasulo"]
claves: ["ROB", "buffer de carga", "estaciones de reserva", "CDB", "ciclos ejecución FP", "liberación recursos"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2025.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]] · [[tomasulo]]

Parámetros fijos para la simulación:
- ROB: 32 entradas.
- Load Buffer: 16 entradas.
- Reservation Stations: 2 para FP add (ADD.D), 4 para FP mul/div.
- Latencias de ejecución: Load/Store = 1 ciclo; FP Add = 2 ciclos; FP Mul = 4 ciclos.
- CDB: puerto único, una escritura por ciclo. Si hay contención, la instrucción espera en Write Result hasta que el CDB libre.
- Liberación de recursos: una unidad funcional o entrada de buffer liberada en ciclo N solo puede reutilizarse en ciclo N+1.
- Pasos a rellenar por instrucción: Issue (emisión), Execution (inicio-fin), Write Result (escritura en CDB), Commit (finalización).
- Código a simular: L.D F0,0(R1); L.D F2,0(R2); ADD.D F6,F0,F2; S.D F6,0(R3). Asumir sin excepciones.

> Tenemos un ROB con capacidad para 32 instrucciones, un buffer de carga con 16 entradas y estaciones de reserva de 2 entradas para la suma y 4 para la multiplicación y la división. La etapa de ejecución de carga y almacenamiento utiliza 1 ciclo. La etapa de ejecución de multiplicación en coma flotante (FP) utiliza 4 ciclos. La etapa de ejecución de la suma en coma flotante (FP) utiliza 2 ciclos. Cualquier paso de una instrucción que quiera escribir en el CDB (Common Data Bus) no puede hacerlo si otra instrucción ya lo está utilizando. En general, cualquier recurso que se libera en un ciclo de reloj no puede utilizarse hasta el siguiente ciclo de reloj.
> — `repo:datos/temarios/AC/examenes/Junio2025.pdf` (cita sin comprobar)

Relacionado: [[algoritmo-tomasulo-los-resultados-se-difunden-por-el-bus-com]] · [[buffer-de-reordenamiento-rob-en-tomasulo-con-especulacion-ca]] · [[configuracion-de-procesador-tomasulo-con-especulacion-del-ej]] · [[parametros-de-tomasulo-con-especulacion-para-problema-2-exam]] · [[simulacion-tomasulo-con-especulacion-parametros-clave-y-rest]]
