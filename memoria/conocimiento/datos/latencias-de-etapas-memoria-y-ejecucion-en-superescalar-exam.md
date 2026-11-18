---
tipo: "dato"
titulo: "Latencias de etapas memoria y ejecución en superescalar examen Junio 2013"
temas: ["ac", "pipeline", "superscalar"]
claves: ["MEM 2 ciclos", "EX 2 ciclos", "LW", "DADD", "DSUB", "adelantamiento"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2013.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]] · [[superscalar]]

Valores numéricos fijos para el problema 3:
- **Etapa MEM (acceso memoria) en LW**: 2 ciclos de reloj (MEM1, MEM2). Dato disponible al final de MEM2 para forwarding / WB.
- **Etapa EX (ejecución ALU) en DADD / DSUB**: 2 ciclos de reloj (EX1, EX2). Resultado disponible al final de EX2 para forwarding / WB.
- **Adelantamiento (forwarding)**: Implementado. Permite pasar resultado de EX2 o MEM2 directamente a EX1 de instrucción dependiente en ciclo siguiente (o mismo ciclo si timing lo permite, pero típicamente ciclo siguiente).
- **Otras etapas** (implícitas estándar): IF=1, ID=1 (lectura registros), WB=1 (escritura registro).
- **Grado 2**: Hasta 2 instrucciones en cada etapa por ciclo (superscalar), salvo limitaciones estructurales (puertos memoria, UF).
Estos números determinan la longitud mínima de la planificación: una carga tarda IF+ID+MEM1+MEM2+WB = 6 ciclos hasta WB; una aritmética IF+ID+EX1+EX2+WB = 5 ciclos. Con forwarding, consumidor puede empezar EX1 en ciclo siguiente a EX2/MEM2 del productor.

> El procesador invierte 2 ciclos para la etapa MEM en las cargas y 2 ciclos para completar la etapa EX de las operaciones aritméticas.
> — `repo:datos/temarios/AC/examenes/Junio2013.pdf`

Relacionado: [[bucle-de-calculo-y-i-a-x-i-2-en-ensamblador-mips64]] · [[alternativas-de-deteccion-de-instruccion-de-salto-en-pipelin]]
