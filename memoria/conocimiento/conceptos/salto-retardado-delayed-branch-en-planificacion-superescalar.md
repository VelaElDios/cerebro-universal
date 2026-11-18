---
tipo: "concepto"
titulo: "Salto retardado (delayed branch) en planificación superescalar"
temas: ["ac", "pipeline", "salto-retardado", "superescalar"]
claves: ["delayed branch", "slot de retardo", "instrucción útil en slot", "desenrollado", "BNE"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2015.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]] · [[salto-retardado]] · [[superescalar]]

En arquitecturas con salto retardado (como MIPS clásico), la instrucción inmediatamente posterior a una instrucción de salto (en orden de programa) se ejecuta **siempre**, independientemente de si el salto se toma o no. Esta instrucción ocupa el "slot de retardo". En el contexto del Problema 4:
- El bucle original termina en `BNE R1, R2, Bucle`. La instrucción en el slot de retardo sería la primera del bucle (`L.D F4, 0(R1)`) si no hay nop.
- Al desenrollar 6 veces, se tienen 6 instrucciones BNE en secuencia. Cada BNE (excepto posiblemente el último) tiene la siguiente instrucción del código desenrollado como su slot de retardo.
- **Aprovechamiento en planificación:** Al generar el código desenrollado lineal, se debe colocar una instrucción útil (que no dependa del salto) en el slot de retardo de cada BNE. Típicamente, la `L.D` de la siguiente iteración es candidata ideal, ya que es independiente del resultado del BNE (solo usa R1 que ya está actualizado por la DADDUI previa). Esto evanta burbujas y mejora CPI.
- El último BNE (del que se sale del bucle) también tiene slot de retardo; se puede poner la primera instrucción posterior al bucle o un NOP si no hay nada útil.

> Se asume que existen adelantamientos, salto retardado y que todas las unidades funcionales están segmentadas.
> — `repo:datos/temarios/AC/examenes/Enero2015.pdf`

Relacionado: [[planificacion-superescalar-mips64-4-vias-con-latencias-pf-pr]] · [[desenrollado-6-y-renombrado-de-registros-pf-para-superescala]] · [[uso-de-ranura-de-retardo-de-1-ciclo-en-superescalar-para-ocu]] · [[delayed-branch-en-vliw-y-su-efecto-en-planificacion]] · [[salto-retardado-delayed-branch-en-bucle-con-bne-y-daddui]]
