---
tipo: "concepto"
titulo: "Patrón de saltos en bucle MIPS64 secuencia 0,1,0,2 (examen Enero 2012)"
temas: ["ac", "prediccion-saltos"]
claves: ["B1", "B2", "B3", "BEQZ", "BEQ", "J", "secuencia periódica"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2012.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[prediccion-saltos]]

El bucle tiene tres instrucciones de salto etiquetadas: B1 (BEQZ R2, next), B2 (BEQZ R4, next), B3 (BEQ R1, R3, fin) más un J loop incondicional. La secuencia de datos 0,1,0,2 hace que R2 tome valores 0,1,0,2,... B1 salta cuando R2==0 (dos de cada cuatro iteraciones). B2 salta cuando R4==0 tras ANDI R4,R2,#1, es decir, cuando R2 es par (0 o 2): tres de cada cuatro iteraciones. B3 salta solo en la última iteración cuando R1==R3. Este patrón determina el comportamiento de los predictores.

> El siguiente bucle MIPS64 recorre la secuencia de enteros 0, 1, 0, 2, 0, 1, 0, 2, 0, 1, 0, 2,... Suponemos que R1 y R3 han sido inicializados con las direcciones del primer y del último elemento de la secuencia, respectivamente.
> — `repo:datos/temarios/AC/examenes/Enero2012.pdf`

Relacionado: [[comportamiento-real-de-saltos-b1-beqz-y-b2-beq-en-bucle-mips]] · [[resultados-reales-de-saltos-b1-y-b2-en-bucle-mips64-secuenci]] · [[ejercicio-2-analisis-de-prediccion-de-saltos-en-bucle-contad]]
