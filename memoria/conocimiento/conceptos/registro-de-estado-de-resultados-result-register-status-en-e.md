---
tipo: "concepto"
titulo: "Registro de estado de resultados (Result Register Status) en el marcador"
temas: ["ac", "registro-resultado", "scoreboard", "war", "waw"]
claves: ["f0", "f2", "f4", "f6", "f8", "f10", "f12", "UF", "escritura resultado"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[registro-resultado]] · [[scoreboard]] · [[war]] · [[waw]]

La tabla inferior "Estado de registros resultado" indica qué unidad funcional (UF) escribirá en cada registro flotante. En el ciclo 16: f0←UF2 (Mult1), f6←UF4 (Suma), f10←UF5 (Divide). Esto evita riesgos WAW y WAR: antes de emitir una instrucción que escribe Fi, se comprueba que no haya otra UF pendiente para ese registro; antes de leer Fj/Fk, se espera a que la UF productora termine (Rj/Rk=SI).

> Estado de registros resultado f0 f2 f4 f6 f8 f10 f12 UF 2 4 5
> — `repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf`

Relacionado: [[estado-de-registros-resultado-register-result-status-en-el-m]] · [[marcador-scoreboard-distingue-riesgos-raw-y-war-con-detencio]] · [[estructura-del-marcador-scoreboard-en-arquitectura-de-comput]]
