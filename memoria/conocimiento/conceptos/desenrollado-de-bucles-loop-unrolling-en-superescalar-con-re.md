---
tipo: "concepto"
titulo: "Desenrollado de bucles (loop unrolling) en superescalar con renombrado de registros"
temas: ["ac", "loop unrolling", "pipeline", "register renaming", "superscalar"]
claves: ["loop unrolling", "register renaming", "ILP", "superscalar scheduling", "dependency elimination"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2020.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[loop unrolling]] · [[pipeline]] · [[register renaming]] · [[superscalar]]

Técnica de **loop unrolling** (desenrollado) para superescalar:
1. **Replicar** el cuerpo del bucle N veces (aquí N=2).
2. **Renombrar registros** en cada réplica para eliminar dependencias falsas (WAW, WAR) entre iteraciones. Ej: si la iteración 1 usa F0, F2, F4, la iteración 2 usa F6, F8, F10, etc. (o registros temporales distintos).
3. **Eliminar** el salto de fin de bucle de la primera réplica (cae por su peso a la segunda). Mantener solo un salto condicional al final del bloque desenrollado que salte al inicio del bloque si quedan iteraciones.
4. **Ajustar** contadores de bucle: en lugar de decrementar 1 por iteración, decrementar N (o comparar con límite ajustado).
5. **Planificar** el bloque resultante como código lineal (sin saltos internos) en el superescalar, aprovechando que ahora hay más instrucciones independientes para rellenar huecos de latencia FP (ADD.D=2, MUL.D=4) y mantener ocupadas las 3 tuberías.
Beneficio: reduce overhead de saltos, aumenta ventana de instrucciones para el planificador estático (compilador), permite mejor uso de forwarding y oculta latencias FP.
Coste: mayor presión de registros (necesita más registros FP/enteros), mayor tamaño de código.

> Unroll now the two first iterations of the loop and schedule the resulting code for the same superscalar.
> — `repo:datos/temarios/AC/examenes/January2020.pdf`

Relacionado: [[criterio-de-desenrollamiento-de-bucles-loop-unrolling]] · [[configuracion-vliw-de-6-unidades-funcionales-con-latencias-a]] · [[clasificacion-de-dependencias-en-bucle-antidependencia-war-e]]
