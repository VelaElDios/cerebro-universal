---
tipo: "dato"
titulo: "Valores iniciales de memoria y registros para los dos casos del ejercicio (June 2025)"
temas: ["ac", "pipeline"]
claves: ["Mem(dir)=1", "read-only addresses", "initial state", "R1=0", "R1=5"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2025.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]]

Datos concretos del enunciado: direcciones 0 y 1 son de solo lectura; memoria inicializada a 1 en todas las direcciones (Mem(dir)=1). Caso a: R1=0, R2=0, R3=8 → Mem(R1) y Mem(R2) son dirección 0 → prohibited; Mem(R3)=Mem(8)=1. Caso b: R1=5, R2=0, R3=7 → Mem(R1)=Mem(5)=1, Mem(R2)=Mem(0)=prohibited, Mem(R3)=Mem(7)=1. Registros FP (F0,F2,F4,F6) inicializados a 0 en ambos casos.

> Addresses 0 and 1 are read-only, and the data memory has been initialised to 1 (i.e. Mem(dir)=1). a) First case Initial State R1 0 R2 0 R3 8 F0 0 F2 0 F4 0 F6 0 Mem(R1) prohibited Mem(R2) prohibited Mem(R3) 1 b) Second case Initial State R1 5 R2 0 R3 7 F0 0 F2 0 F4 0 F6 0 Mem(R1) 1 Mem(R2) prohibited Mem(R3) 1
> — `repo:datos/temarios/AC/examenes/June2025.pdf` (cita sin comprobar)

Relacionado: [[como-rellenar-tabla-de-ejecucion-con-bits-venenosos-casos-r1]] · [[planificacion-estatica-con-bits-venenosos-convencion-dirty-p]] · [[planificacion-estatica-con-poison-bits-en-mips64-reglas-de-e]] · [[estado-inicial-de-registros-y-memoria-para-problema-3-enero]]
