---
tipo: "receta"
titulo: "Cómo calcular ciclos por iteración del código original con latencias dadas"
temas: ["ac", "cpi", "performance-analysis", "pipeline"]
claves: ["original loop", "cycles per iteration", "latency table"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2018.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[cpi]] · [[performance-analysis]] · [[pipeline]]

Para el código original sin desenrollar: se emiten instrucciones en orden, respetando latencias. Secuencia crítica: L.D F2 (ciclo 1) → MUL.D F4 (espera 1 ciclo por latencia L.D→ALU FP = 1, emite ciclo 2) → ADD.D F6 (espera 3 ciclos por latencia ALU FP→ALU FP = 3 desde MUL.D, emite ciclo 5) → S.D F6 (espera 2 ciclos por latencia ALU FP→S.D = 2 desde ADD.D, emite ciclo 7). Las instrucciones enteras (DADDUI, SLTI, BEQZ) tienen latencia 0 y 2 unidades, no añaden ciclos. El salto BEQZ se ignora. La iteración tarda 7 ciclos (desde emisión de primera L.D hasta emisión de S.D). CPI original = 7 ciclos/iteración.

> B) How many cycles per iteration does require the original code? Compute the speedup for the unrolled and scheduled version with respect the original code.
> — `repo:datos/temarios/AC/examenes/June2018.pdf`

Relacionado: [[bucle-vectorial-de-referencia-para-desenrollado-y-planificac]] · [[tabla-de-latencias-entre-instrucciones-productoras-y-consumi]] · [[como-calcular-ciclos-por-iteracion-en-codigo-original-con-la]] · [[desenrollado-4x-y-planificacion-minima-para-bucle-fp-con-lat]] · [[speedup-teorico-del-desenrollado-4x-frente-a-codigo-original]]
