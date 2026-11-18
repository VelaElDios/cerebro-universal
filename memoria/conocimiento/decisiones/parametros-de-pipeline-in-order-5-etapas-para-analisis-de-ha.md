---
tipo: "decision"
titulo: "Parámetros de pipeline in-order 5 etapas para análisis de hazards (examen Junio 2026)"
temas: ["ac", "forwarding", "hazards", "pipeline"]
claves: ["IF ID EX MEM WB", "detección ID", "banco registros lectura/escritura mismo ciclo", "forwarding completo", "fsd consume dato en MEM", "saltos resueltos en ID", "UF entero 1 ciclo", "UF mul FP 5 ciclos", "UF add FP 4 ciclos", "totalmente segmentadas"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2026.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[forwarding]] · [[hazards]] · [[pipeline]]

Configuración exacta del procesador para el apartado 1a: pipeline 5 etapas in-order single-issue. Detección/resolución hazards en ID. Registro file: write/read mismo ciclo (evita WAR/WAW en WB/ID). Forwarding completo (ex/MEM y MEM/WB). fsd usa dato en MEM (no EX) -> reduce stalls por RAW en store. Saltos resueltos en ID -> penalty 1 ciclo si tomado (flush IF). UF enteros: latencia 1, II=1. UF FP mul: latencia 5, II=1 (totalmente segmentada). UF FP add: latencia 4, II=1 (totalmente segmentada).

> El bucle se ejecuta en un procesador RISC-V In-Order de emisión única (Single-Issue) con un cauce segmentado clásico de 5 etapas (IF, ID, EX, MEM, WB) donde a) las dependencias se detectan y resuelven en la etapa ID, b) el banco de registros permite escribir y leer en el mismo ciclo de reloj, c) soporta adelantamiento completo de operandos, d) la instrucción fsd consume el dato a almacenar directamente en la etapa MEM (no en EX) y e) los saltos condicionales se resuelven completamente en la etapa ID. Además, la UF de enteros y cálculo de direcciones require 1 ciclo de ejecución en EX, la UF de multiplicación FP tiene 5 ciclos de ejecución en EX, la UF de suma FP tiene 4 ciclos de ejecución en EX y todas está completamente segmentadas.
> — `repo:datos/temarios/AC/examenes/Junio2026.pdf`

Relacionado: [[alternativas-de-deteccion-de-instruccion-de-salto-en-pipelin]] · [[antidependencia-siempre-genera-hazard-war-en-pipeline-in-ord]] · [[configuracion-de-pipeline-mips64-para-problema-de-examen-lat]] · [[parametros-del-procesador-para-problema-1-ac-enero-2025]] · [[parametros-estandar-para-ejercicios-de-segmentacion-software]]
