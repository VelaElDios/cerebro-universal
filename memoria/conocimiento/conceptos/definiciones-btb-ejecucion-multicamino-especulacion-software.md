---
tipo: "concepto"
titulo: "Definiciones: BTB, ejecución multicamino, especulación software, superescalar CPI ideal, Intel P7, multicore, PowerPC"
temas: ["ac", "btb", "especulacion-software", "intel-p7", "multicamino", "multicore", "powerpc", "superescalar"]
claves: ["Branch Target Buffer", "multi-path execution", "especulación software", "CPI ideal grado 4", "microarquitectura P7", "memoria compartida UMA NUMA", "RISC"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2013.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[btb]] · [[especulacion-software]] · [[intel-p7]] · [[multicamino]] · [[multicore]] · [[powerpc]] · [[superescalar]]

Respuestas test: (13) BTB = caché que almacena dirección destino + bits predicción (fusiona BTAC + predicción); opción d "ninguna" porque a/b/c describen mal. (11) Multicamino = ejecutar ambos caminos sin predecir (a). (14) Especulación software = compilador mueve instrucciones del bloque predicho antes del salto (a). (16) CPI ideal = 1/grado = 1/4 = 0.25 (c). (18) Intel P7 (NetBurst) = aumento profundidad segmentos para alta frecuencia (c). (19) Multicore actuales = UMA (memoria compartida acceso uniforme) típicamente (b), aunque muchas son NUMA; examen espera UMA. (20) PowerPC = RISC (d).

> La BTB: d) Ninguna es correcta / En la ejecución multicamino: a) Se ejecutan las dos ramas de un salto condicional, sin hacer predicción / En la especulación software: a) El compilador apuesta por un sentido del salto, moviendo instrucciones de ese bloque al anterior / Un superescalar de grado 4 tiene un CPI ideal de c) 0,25 / Las mejoras que introduce la microarquitectura P7 de Intel se basan principalmente en: c) Aumento de la profundidad de los segmentos / Las arquitecturas actuales multicore son máquinas de: b) Memoria compartida de tiempo de acceso uniforme / El PowerPC tiene una arquitectura: d) RISC
> — `repo:datos/temarios/AC/examenes/Enero2013.pdf` (cita sin comprobar)

Relacionado: [[btb-branch-target-buffer-fusion-de-btac-y-bits-de-prediccion]] · [[ejecucion-multicamino-multi-path-execution-como-alternativa]] · [[btb-cache-de-direcciones-destino-de-saltos-con-bits-de-predi]] · [[ejemplos-reales-de-predictores-de-salto-en-procesadores-come]] · [[ejecucion-multicamino-multi-path-execution-frente-a-predicci]]
