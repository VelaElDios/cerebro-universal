---
tipo: "receta"
titulo: "Cómo comparar rendimiento de dos máquinas con mismo ISA usando tiempo de ejecución"
temas: ["ac", "ciclo-reloj", "cpi", "rendimiento"]
claves: ["tiempo ejecución", "IC", "CPI", "ciclo reloj", "ns"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2017.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[ciclo-reloj]] · [[cpi]] · [[rendimiento]]

Para comparar dos máquinas que ejecutan el mismo programa (mismo IC), calcular el tiempo de ejecución: T = IC × CPI × ciclo_reloj. La máquina con menor T es más rápida. El speedup = T_lenta / T_rápida. En el ejemplo: T_A = IC × 2.1 × 1.2ns = IC × 2.52ns; T_B = IC × 1.0 × 1.8ns = IC × 1.8ns. B es más rápida. Speedup = 2.52/1.8 = 1.40. Por tanto, B es 1.40 veces más rápida que A (opción b).

> Supongamos que se tiene dos realizaciones de la misma arquitectura del repertorio de instrucciones. La máquina A tiene un ciclo de reloj de 1,2 ns y un CPI de 2,1 para un programa concreto, mientras que la máquina B tiene un tiempo de ciclo de 1,8 ns y un CPI de 1,0 para el mismo programa. ¿Qué máquina es más rápida para este programa?, ¿cuánto más rápida?
> — `repo:datos/temarios/AC/examenes/Junio2017.pdf`

Relacionado: [[analisis-de-dependencias-en-bucle-con-add-d-y-s-d-misma-iter]] · [[bucle-de-calculo-y-i-a-x-i-2-en-ensamblador-mips64]]
