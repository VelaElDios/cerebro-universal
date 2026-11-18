---
tipo: "receta"
titulo: "Preguntas Problema 3: Tabla tiempos (Emisión, Ejecución, Escritura, Finalización) y ROB ciclo 12"
temas: ["ac", "pipeline-timing", "rob", "simulacion", "tomasulo"]
claves: ["ciclo inicio fin cada paso", "motivo detención RAW estructural orden programa", "ROB entrada instrucción etapa valor registro destino", "nomenclatura valor (Rx) (Fx) Mem(d) #ROBx #ROBx(data)"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2025.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline-timing]] · [[rob]] · [[simulacion]] · [[tomasulo]]

Pasos simulación: 1. Emisión (Issue): Chequear estación reserva libre + entrada ROB libre. Renombrar destinos (ROB#). Leer operandos (valor o tag ROB). 2. Ejecución (Execute): Esperar operandos (RAW) + Unidad libre (Estructural). Iniciar latencia fija. 3. Escritura CDB (Write Result/CDB): Esperar CDB libre + Fin ejecución. Broadcast tag/valor. 4. Finalización (Commit): Cabeza ROB + Instrucción completada (Escritura hecha). Actualizar registro arquitectónico / Memoria. Motivos stall: RAW (esperar tag), Estructural (unidad ocupada, CDB ocupado), Orden programa (Emisión en orden, Commit en orden). ROB Ciclo 12: Rellenar 7 entradas (ROB1-ROB7) con Instrucción, Etapa actual (ej: Ejecución c3/5, Escritura, Commit), Valor (según nomenclatura), Registro Destino (F1, F2, etc.).

> (a) Detalla la ejecución del siguiente código. Para ello, indica en la tabla siguiente el número de ciclo de inicio y fin para cada uno de los pasos de cada instrucción y, cuando corresponda, el motivo para detener la ejecución del paso en cuestión (un riesgo RAW, un riesgo estructural, el orden del programa, etc.). (b) Completa la siguiente tabla para mostrar el contenido del buffer de reorden (ROB) en el ciclo 12. a. Ten en cuenta que el campo Etapa mostrará el valor de la etapa en ejecución o de la última etapa completada. b. Utiliza esta nomenclatura para completar el campo Valor: i. (Rx) Contenido del registro entero Rx. ii. (Fx) Contenido del registro FP Fx. iii. Mem(d) Contenido de la dirección de memoria d. iv. #ROBx Valor que debe obtenerse de la entrada x del ROB. v. #ROBx(data) Datos leídos o recuperados del campo Valor de la entrada x del ROB.
> — `repo:datos/temarios/AC/examenes/Enero2025.pdf` (cita sin comprobar)

Relacionado: [[secuencia-de-10-instrucciones-para-simulacion-tomasulo-probl]] · [[pasos-para-simular-tomasulo-especulativo-con-rob-y-restricci]] · [[pasos-para-rellenar-tabla-de-estado-de-instrucciones-emision]] · [[como-abordar-la-simulacion-tomasulo-con-rob-para-examen-ac]]
