---
tipo: "receta"
titulo: "Cálculo de CPI en bucle desenrollado superescalar con ancho 4"
temas: ["ac", "cpi", "rendimiento", "superescalar"]
claves: ["CPI = ciclos totales / instrucciones totales", "ancho 4", "36 instrucciones (6×6)", "planificación óptima"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2015.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[cpi]] · [[rendimiento]] · [[superescalar]]

**Fórmula:** CPI = (Número total de ciclos de reloj para ejecutar el fragmento desenrollado) / (Número total de instrucciones en el fragmento desenrollado).
- Fragmento desenrollado 6×: 6 iteraciones × 6 instrucciones/iteración = **36 instrucciones**.
- Se obtiene el número de ciclos de la planificación óptima (tabla ciclo a ciclo del apartado a).
- **CPI ideal** con ancho 4 y sin dependencias: 36 inst / (36/4) ciclos = **1.0** (pero CPI ideal real es 0.25 ciclos/inst = 4 inst/ciclo; CPI = ciclos/inst, so ideal CPI = 0.25). **Corrección:** CPI = ciclos / instrucciones. Ideal: 9 ciclos / 36 inst = **0.25**.
- **CPI real** será mayor por dependencias (latencias FP, dependencia R1 en DADDUI/BNE, puertos limitados 2 PF + 2 Int/Mem).
- Pasos:
  1. Construir la tabla de planificación ciclo a ciclo del apartado a.
  2. Contar el último ciclo en que se lanza una instrucción (o el ciclo en que termina la última WB).
  3. Dividir ciclos totales / 36.
- Ejemplo: si la planificación óptima toma 18 ciclos → CPI = 18/36 = **0.50**.
- El resultado numérico exacto depende de la planificación concreta; el examen pide mostrar la planificación y luego el CPI derivado.

> b) Calcula el CPI del fragmento
> — `repo:datos/temarios/AC/examenes/Enero2015.pdf`

Relacionado: [[planificacion-superescalar-mips64-4-vias-con-latencias-pf-pr]]
