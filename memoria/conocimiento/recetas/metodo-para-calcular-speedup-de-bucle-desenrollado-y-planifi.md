---
tipo: "receta"
titulo: "Método para calcular speedup de bucle desenrollado y planificado vs original (examen AC 2017/18)"
temas: ["ac", "desenrollado", "pipeline", "planificacion", "speedup"]
claves: ["speedup", "ciclos original", "ciclos desenrollado", "factor 4"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2018.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[desenrollado]] · [[pipeline]] · [[planificacion]] · [[speedup]]

Speedup = (Ciclos por iteración en código original) / (Ciclos totales del bucle desenrollado planificado / 4). Pasos: 1) Obtener CPI_original (ciclos/iteración) simulando el bucle original con emisión in-order dual y latencias dadas. 2) Planificar el bucle desenrollado 4 veces (4 copias con renombrado de registros PF: F2,F4,F6 → F2,F4,F6, F8,F10,F12, F14,F16,F18, F20,F22,F24; enteros reusan R1,R2,R4 pero con dependencias entre iteraciones). 3) Minimizar ciclos totales reordenando instrucciones (software pipelining / list scheduling). 4) Medir ciclos totales desde primera emisión hasta última escritura (S.D de 4ª iteración). 5) Speedup = CPI_original / (Ciclos_totales / 4).

> ¿Cuál es el speedup de la versión desenrollada y planificada con respecto al código original?
> — `repo:datos/temarios/AC/examenes/Junio2018.pdf`

Relacionado: [[problema-de-desenrollado-y-planificacion-de-bucle-superescal]] · [[como-calcular-ciclos-por-iteracion-en-codigo-original-con-la]] · [[speedup-teorico-del-desenrollado-4x-frente-a-codigo-original]] · [[calculo-de-speedup-entre-bucle-original-y-desenrollado-en-vl]] · [[calculo-de-speedup-para-bucle-desenrollado-en-pipeline-con-h]]
