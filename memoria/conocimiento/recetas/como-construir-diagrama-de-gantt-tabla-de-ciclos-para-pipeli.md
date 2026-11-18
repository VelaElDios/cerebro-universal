---
tipo: "receta"
titulo: "Cómo construir diagrama de Gantt / tabla de ciclos para pipeline superescalar"
temas: ["ac", "pipeline", "superscalar"]
claves: ["diagrama Gantt", "ciclos reloj", "etapas IF ID EX MEM WB", "emisión dual", "forwarding", "stall"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2013.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]] · [[superscalar]]

Plantilla para resolver planificación superescalar grado 2:
1. **Identificar recursos**: 2 slots emisión/ciclo, 1 puerto MEM (¿o 2? enunciado dice "cualquier tipo", asumir 2 puertos MEM o 1 con cola), UF enteras (¿cuántas? asumir 2 ALU para grado 2).
2. **Listar dependencias** (RAW, WAR, WAW) entre las 7 instrucciones.
3. **Definir latencias**: IF=1, ID=1, EX=2 (aritmética), MEM=2 (LW), WB=1. Forwarding: resultado EX disponible al final del 2º ciclo EX para siguiente instr en EX; resultado MEM disponible al final del 2º ciclo MEM.
4. **Simular ciclo a ciclo** (tabla filas=instr, columnas=ciclos):
   - **Caso a (En orden)**: Emite 2/ciclo en orden si ID libre y sin hazard estructural. Si RAW no resuelto por forwarding → stall en ID (burbuja). Ejecuta en orden. Commit en orden.
   - **Caso b (OOO sin renombrar)**: Emite en orden (2/ciclo) si RS libre. Despacha a EX fuera de orden cuando operandos listos (forwarding o valor en registro). **Respeta WAR/WAW**: no ejecutar escritura hasta que lecturas previas hechas; no emitir escritura si hay escritura posterior pendiente (WAW). Commit en orden.
   - **Caso c (OOO con renombrar)**: Emite 2/ciclo, renombra destinos a registros físicos. Despacha a EX cuando operandos listos (tags resueltos). Sin WAR/WAW. Commit en orden vía ROB.
5. **Dibujar**: Para cada instr, marcar ciclos IF, ID, EX1, EX2, MEM1, MEM2, WB. Indicar forwarding con flechas.
Truco: En examen, basta tabla compacta: Ciclo | Slot0 | Slot1 | Notas (stall, forward, commit).

> Muestra una planificación de instrucciones para los siguientes casos: a) Ejecución en orden b) Ejecución fuera de orden, sin capacidad de renombramiento. c) Ejecución fuera de orden, con capacidad de renombramiento.
> — `repo:datos/temarios/AC/examenes/Junio2013.pdf`

Relacionado: [[bucle-de-calculo-y-i-a-x-i-2-en-ensamblador-mips64]] · [[analisis-de-dependencias-en-bucle-con-add-d-y-s-d-misma-iter]] · [[planificacion-en-superescalar-grado-2-con-sin-renombramiento]] · [[planificacion-en-superescalar-grado-2-en-orden-fuera-de-orde]] · [[planificacion-en-superescalar-grado-2-con-latencias-mem-2-y]]
