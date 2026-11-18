---
tipo: "concepto"
titulo: "Estructura del marcador (scoreboard) en arquitectura de computadores"
temas: ["ac", "arquitectura", "pipeline", "scoreboard"]
claves: ["marcador", "scoreboard", "estado instrucciones", "unidades funcionales", "registros resultado", "Qj", "Qk", "Rj", "Rk"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[arquitectura]] · [[pipeline]] · [[scoreboard]]

El marcador (scoreboard) es una técnica de planificación dinámica que permite ejecución fuera de orden manteniendo las dependencias de datos. Consta de tres tablas principales que se actualizan cada ciclo:

1. **Estado de las instrucciones**: cuatro columnas por instrucción — Emisión (cuándo se emite), Lectura Operandos (cuándo lee sus operandos), Ejecución completa (cuándo termina la ALU), Escritura resultado (cuándo escribe en registro).

2. **Estado de las unidades funcionales (UF)**: una fila por UF con campos:
   - Ocupada (SI/NO)
   - Op (operación en curso: Carga, Mult, Sub, Div, etc.)
   - Fi (registro destino)
   - Fj, Fk (registros fuente)
   - Qj, Qk (número de UF que producirá Fj/Fk; 0 si ya disponible)
   - Rj, Rk (banderas SI/NO: ¿el operando ya está listo para leer?)

3. **Estado de registros resultado**: indica qué UF escribirá en cada registro (0 si ninguno). Permite detectar riesgos WAW (dos escrituras al mismo registro) y WAR (escritura antes de que otros lean).

El ejemplo muestra 6 instrucciones (2 fld, fmul.d, fsub.d, fdiv.d, fadd.d) y 5 UF (Entera para cargas, Mult1, Mult2, Suma, Divide) a lo largo de 7 ciclos (3–9).

> Estado de las instrucciones Lectura Ejecución Escritura ciclo 3 Instrucción Emisión Operandos completa resultado
> — `repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf`

Relacionado: [[planificacion-dinamica-de-instrucciones-con-marcador-scorebo]] · [[estructuras-de-datos-del-marcador-scoreboard]] · [[pasos-de-ejecucion-en-el-algoritmo-del-marcador-scoreboard]]
