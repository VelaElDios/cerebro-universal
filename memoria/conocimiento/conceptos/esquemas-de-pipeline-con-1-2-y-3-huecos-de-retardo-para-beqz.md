---
tipo: "concepto"
titulo: "Esquemas de pipeline con 1, 2 y 3 huecos de retardo para beqz"
temas: ["ac", "beqz", "diagrama", "pipeline"]
claves: ["IF ID EX MEM WB", "MUX", "Adder", "Zero?", "RS1", "RS2", "Sign Extend"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[beqz]] · [[diagrama]] · [[pipeline]]

Tres diagramas de temporización (space-time diagrams) para la instrucción `beqz x3, direc` en un pipeline de 5 etapas con adelantamiento (forwarding): 1) **3 huecos de retardo** (sentido en EX, dirección en MEM): el salto resuelve en MEM; las 3 instrucciones siguientes (Siguiente, Siguiente+1, Siguiente+2) entran en IF pero se convierten en burbujas; la instrucción destino empieza en IF en el ciclo 5. 2) **1 hueco de retardo** (sentido y dirección en ID): se añade un sumador y MUX en ID para calcular PC+offset y evaluar condición; solo la instrucción inmediatamente siguiente entra en IF y se anula (burbuja); destino empieza en IF en el ciclo 3. 3) **2 huecos de retardo** (sentido en EX, dirección en ID): dirección lista en ID, pero condición en EX; dos instrucciones siguientes entran en IF y se anulan; destino empieza en IF en el ciclo 4. Los diagramas muestran las etapas IF, ID, EX, MEM, WB y las señales de control (MUX, Adder, Zero?, RegFile, ALU, Sign Extend).

> beqz x3, direc IF ID EX MEM WB Siguiente IF Siguiente + 1 Siguiente + 2 direc: destino salto IF ID EX MEM WB
> — `repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4.pdf`

Relacionado: [[calculo-de-penalizacion-de-salto-condicional-en-pipeline-de]] · [[definicion-de-latencia-de-salto-y-huecos-de-retardo]]
