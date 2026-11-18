---
tipo: "concepto"
titulo: "Por qué -O1 evita que el compilador enmascare la optimización manual de ILP"
temas: ["ac", "compilacion", "optimizacion-compilador"]
claves: ["-O1", "-O2", "-O3", "auto-unrolling", "compiler optimization", "ILP"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab4/tarea4_1_ilp.cpp"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[compilacion]] · [[optimizacion-compilador]]

Los flags de optimización altos (-O2, -O3) activan **auto-unrolling** y **vectorización automática** del compilador. Si se compila el código base con -O3, GCC/Clang transformarán automáticamente el bucle secuencial en uno desenrollado con múltiples acumuladores, haciendo que la versión "base" ya sea rápida y ocultando el efecto pedagógico de la optimización manual.

**-O1** habilita optimizaciones básicas (eliminación de código muerto, propagación de constantes, etc.) pero **desactiva transformaciones agresivas de bucles** como unrolling automático y vectorización. Esto garantiza que:
- La versión base refleje verdaderamente el cuello de botella de dependencia de datos
- La versión optimizada muestre la mejora real de la técnica manual
- La comparación sea justa y educativa

> Compilar: Generar ambos ejecutables usando el flag de optimización -O1 // (evita que el auto-unrolling del compilador enmascare la prueba):
> — `repo:datos/temarios/AC/Practicas/Code_Lab4/tarea4_1_ilp.cpp`

Relacionado: [[optimizacion-ilp-mediante-desenrollado-de-bucle-con-4-acumul]] · [[compilar-con-o1-para-desactivar-auto-unrolling-y-reordenacio]] · [[desenrollamiento-de-bucles-loop-unrolling-permite-planificar]] · [[proposito-del-desenrollado-de-bucles-loop-unrolling]]
