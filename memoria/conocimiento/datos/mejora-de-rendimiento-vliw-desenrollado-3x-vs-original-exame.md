---
tipo: "dato"
titulo: "Mejora de rendimiento VLIW desenrollado 3x vs original (examen Enero 2018)"
temas: ["ac", "rendimiento", "speedup", "vliw"]
claves: ["speedup", "CPI", "IPC", "desenrollado", "3x"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2018.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[rendimiento]] · [[speedup]] · [[vliw]]

Comparativa esperada (valores típicos para este problema de examen):
- Apartado A (bucle original): ~7 ciclos por iteración, 10 instrucciones → IPC = 10/7 ≈ 1.43 ops/ciclo (35.8% de ocupación de 4 slots).
- Apartado C (desenrollado 3x compactado): ~10-11 ciclos para 3 iteraciones → ~3.3-3.7 ciclos/iteración, ~24 instrucciones útiles/3 iteraciones → IPC ≈ 24/11 ≈ 2.18 ops/ciclo (54.5% ocupación).
- Speedup (mejora rendimiento) = (Ciclos_original_3iter / Ciclos_desenrollado_3iter) = 21 / 11 ≈ 1.91x (casi 2x).
- También se expresa como reducción de CPI o aumento de IPC: IPC mejora de 1.43 a 2.18 → factor 1.52x en throughput de instrucciones.
- La mejora viene de: (1) eliminar 2/3 de los saltos y overhead de bucle, (2) permitir interleaving de instrucciones de distintas iteraciones para ocultar latencias de MEM y MUL.D, (3) mejor utilización de los 4 slots VLIW.

> ¿Qué mejora en el rendimiento se ha obtenido si se compara el código del apartado A con el del C?
> — `repo:datos/temarios/AC/examenes/Enero2018.pdf`

Relacionado: [[desenrollado-de-bucle-3x-y-planificacion-vliw-compactada]]
