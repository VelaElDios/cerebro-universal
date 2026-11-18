---
tipo: "receta"
titulo: "Rellenar tabla de ejecución Tomasulo: columnas Issue, Execution, Write Result, Commit"
temas: ["ac", "tomasulo"]
claves: ["Issue", "Execution", "Write Result", "Commit", "ciclos", "RAW", "estructural", "orden programa"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2025.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[tomasulo]]

Formato de la tabla a rellenar para cada instrucción (L.D F0,0(R1); L.D F2,0(R2); ADD.D F6,F0,F2; S.D F6,0(R3)):
- Issue: ciclo en que se emite (requiere entrada libre en ROB, load buffer o reservation station, y operandos disponibles o renombrados).
- Execution: ciclo inicio y fin (latencia fija: load=1, FP add=2). Puede retrasarse por riesgo RAW (esperar operandos) o estructural (unidad funcional ocupada).
- Write Result: ciclo en que se escribe en CDB (requiere CDB libre y ejecución terminada). Puede retrasarse por contención CDB.
- Commit: ciclo en que sale del ROB en orden de programa (requiere instrucción en cabeza de ROB y Write Result completado). Puede retrasarse por orden de programa (instrucciones anteriores no commiteadas).
Debe anotarse el motivo de cada espera (RAW, estructural, CDB, orden programa).

> Indica el número de ciclo de inicio y fin para cada uno de los pasos de cada instrucción y, cuando corresponda, el motivo para detener la ejecución del paso en cuestión (un riesgo RAW, un riesgo estructural, el orden del programa, etc.).
> — `repo:datos/temarios/AC/examenes/Junio2025.pdf`

Relacionado: [[simulacion-tomasulo-con-especulacion-parametros-de-hardware]]
