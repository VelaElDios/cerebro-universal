---
tipo: "decision"
titulo: "Política de BTB: solo entradas para saltos tomados, predicción NT en miss, eliminación sin penalidad en hit-pero-NT, actualización con 1 ciclo penalidad en miss-pero-tomado"
temas: ["ac", "prediccion-saltos"]
claves: ["BTB", "solo saltos tomados", "predicción no tomado", "miss", "hit", "penalización actualización", "eliminación entrada"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2016.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[prediccion-saltos]]

Decisiones de diseño de la BTB del enunciado: 1) Entradas solo para saltos que *son* tomados (condicionales tomados + incondicionales). No hay entradas para saltos no tomados. 2) Miss en BTB → predicción por defecto = No Tomado (NT). 3) Hit en BTB (predice Tomado) pero resultado real = NT → entrada eliminada, **sin penalidad** (el pipeline ya iba por camino secuencial correcto). 4) Miss en BTB (predice NT) pero resultado real = Tomado → entrada insertada/actualizada en BTB, **penalidad extra de 1 ciclo** además de la latencia normal de resolución del salto. Esto modela el coste de escribir en la BTB.

> b. Sólo almacena las direcciones de saltos tomados (incluyendo los saltos incondicionales). c. Si un salto condicional no está en BTB se predice como no tomado. d. Si una dirección se encuentra en el BTB pero el salto acaba siendo no tomado, la dirección es eliminada del BTB, sin penalización. e. Si una dirección no se encuentra en el BTB pero el salto finalmente es tomado (incluye los saltos incondicionales), el BTB se actualiza con un ciclo de penalización
> — `repo:datos/temarios/AC/examenes/Junio2016.pdf`

Relacionado: [[actualizacion-de-la-btb-tras-ejecutar-el-salto]] · [[bht-con-contadores-de-saturacion-de-2-bits-pregunta-17]] · [[accion-ante-fallo-en-btb-con-salto-tomado-real-predecir-nt-p]] · [[calculo-de-cpi-con-btb-que-almacena-solo-saltos-tomados-y-pr]] · [[mejora-prestaciones-btb-con-politica-solo-saltos-tomados-y-a]]
