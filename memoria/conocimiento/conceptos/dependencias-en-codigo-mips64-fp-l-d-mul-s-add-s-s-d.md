---
tipo: "concepto"
titulo: "Dependencias en código MIPS64 FP: L.D → MUL.S → ADD.S → S.D"
temas: ["ac", "dependencias", "mips64", "punto-flotante", "raw"]
claves: ["dependencia datos", "RAW", "L.D MUL.S ADD.S S.D", "registro F10 F4 F8"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2013.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[dependencias]] · [[mips64]] · [[punto-flotante]] · [[raw]]

Código: I1 L.D F10,10(R3); I2 MUL.S F4,F10,F10; I3 ADD.S F8,F4,F10; I4 S.D F8,10(R3). I3 (ADD.S) escribe F8, I4 (S.D) lee F8 → dependencia RAW (datos) en F8. I3 lee F4 (escrito por I2) y F10 (escrito por I1) → RAW. I4 escribe memoria 10(R3), I1 lee misma dirección → dependencia de memoria (RAW mem). Pregunta pide solo I3-I4: dependencia de datos (RAW) en registro F8.

> Entre la instrucción I3 e I4 existe solamente una dependencia: b) De datos
> — `repo:datos/temarios/AC/examenes/Enero2013.pdf` (cita sin comprobar)

Relacionado: [[antidependencia-war-y-dependencia-de-salida-waw-definiciones]] · [[dependencias-en-fragmento-de-codigo-fp-mips-l-d-add-s-add-s]] · [[tipos-de-dependencias-y-hazards-en-codigo-mips64-de-punto-fl]] · [[analisis-de-dependencias-entre-instrucciones-de-punto-flotan]]
