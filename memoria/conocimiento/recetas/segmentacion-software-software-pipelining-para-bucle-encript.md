---
tipo: "receta"
titulo: "Segmentación software (software pipelining) para bucle encriptación MIPS64"
temas: ["ac", "mips", "pipeline", "software-pipelining"]
claves: ["software pipelining", "start-up", "finish-up", "planificación", "latencias"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2018.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[mips]] · [[pipeline]] · [[software-pipelining]]

Pasos típicos para este bucle (6 instrucciones, latencias: LB 2 ciclos, DADD 1, DADDUI 1, SB 1, BNEZ 1 con salto retardado): 
1. Desenrollar y reordenar para separar instrucciones dependientes. 
2. Crear kernel prologue (start-up), kernel steady-state (bucle pipelinado) y epilogue (finish-up). 
3. Usar renombrado de registros (R2, R3, R1) para evitar WAW/WAR. 
4. Planificar con adelantamiento (forwarding) y slot de retardo de salto. 
Ejemplo de kernel steady-state (iniciando nueva iteración cada ciclo): 
Iteración n:   LB R2_n, 0(R1_n)
Iteración n+1: DADD R3_n, R2_n, R0
Iteración n+2: DADDUI R2_n, R2_n, #5
Iteración n+3: SB R2_n, 0(R1_n)
Iteración n+4: DADDUI R1_n, R1_n, #1
Iteración n+5: BNEZ R3_n, loop
Start-up: 5 instrucciones iniciales (llenar pipeline). Finish-up: 5 instrucciones finales (vaciar pipeline). La planificación exacta depende de latencias asumidas (ej. LB latencia 2, uso en DADD requiere 1 ciclo de adelantamiento).

> b) Muestra el bucle modificado que resulta al aplicar segmentación software (usa el espacio disponible). c) Muestra, junto con el bucle modificado, el código de start-up y finish-up (usa el espacio disponible). d) Planifica el programa obtenido en el apartado anterior para evitar el mayor número de detenciones posibles. Haz las suposiciones usuales: adelantamiento, salto retardado, latencia de instrucciones…
> — `repo:datos/temarios/AC/examenes/Enero2018.pdf`

Relacionado: [[antidependencia-war-y-dependencia-de-salida-waw-definiciones]] · [[algoritmo-tomasulo-origen-y-objetivo-cpi1]] · [[como-resolver-segmentacion-software-software-pipelining-en-m]] · [[segmentacion-software-software-pipelining-para-bucle-conteo]] · [[conversion-de-codigo-vliw-compactado-a-bucle-mips64-segmenta]]
