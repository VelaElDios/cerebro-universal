---
tipo: "receta"
titulo: "Cálculo de operaciones por ciclo (IPC) en planificación VLIW"
temas: ["ac", "ipc", "metricas", "rendimiento", "vliw"]
claves: ["operations per cycle", "IPC", "throughput", "VLIW width", "scheduling efficiency"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2016.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[ipc]] · [[metricas]] · [[rendimiento]] · [[vliw]]

Para responder a la parte (b), una vez completado el diagrama de 20 ciclos:
1. Contar total de operaciones emitidas en los 20 ciclos (cada paquete VLIW puede tener 1-4 ops).
2. Dividir: operaciones_totales / 20_ciclos = ops/ciclo medio.
3. Comparar con el máximo teórico (4 ops/ciclo) para obtener eficiencia: (ops/ciclo_real / 4) × 100%.
En este tipo de problemas, el desenrollado 4× suele permitir acercarse a 3-4 ops/ciclo si las latencias se esconden bien. El límite lo marcan las dependencias de recurrencia (R1, R2, R10 se actualizan cada iteración) y la latencia de DIV.D (2 ciclos EX) que crea una cadena crítica.

> b) How many operations per cycle are reached?
> — `repo:datos/temarios/AC/examenes/January2016.pdf`

Relacionado: [[problema-de-planificacion-vliw-con-desenrollado-de-bucle-exa]]
