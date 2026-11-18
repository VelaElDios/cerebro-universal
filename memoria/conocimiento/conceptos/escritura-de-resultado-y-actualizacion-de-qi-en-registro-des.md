---
tipo: "concepto"
titulo: "Escritura de resultado y actualización de Qi en registro destino"
temas: ["ac", "arquitectura", "tomasulo"]
claves: ["escritura resultado", "write result", "Qi", "CDB"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[arquitectura]] · [[tomasulo]]

Al escribir resultado (Write Result), la estación de reserva pone su resultado en el CDB. El registro destino (cuyo Qi apuntaba a esa estación) recibe el valor y pone su Qi a 0. Simultáneamente, todas las estaciones de reserva que esperaban ese Qi capturan el valor. En el ejemplo: tras ciclo 4, Qi(f6)=M(34+x2) Suma1 (la carga escribió f6 y Suma1 espera f6); tras ciclo 5, Qi(f2)=M(45+x3) (carga 2 escribió f2).

> Qi Mult 1 M(45+x3) M(34+x2) Suma 1 Mult 2
> — `repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf`

Relacionado: [[fichero-de-registros-con-campo-qi-en-tomasulo]] · [[renombrado-de-registros-via-qi-register-status-en-tomasulo]] · [[evolucion-del-registro-base-x1-y-qi-de-registros-fp-en-el-ej]]
