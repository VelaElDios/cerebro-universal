---
tipo: "dato"
titulo: "Parámetros de temporización VLIW examen enero 2016"
temas: ["ac", "latencias", "parametros-temporizacion", "vliw"]
claves: ["MEM=2 ciclos", "EX=2 ciclos", "resto=1 ciclo", "L.D", "S.D", "ADD.D", "MUL.D", "DIV.D", "DADDUI", "BNEZ"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2016.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[latencias]] · [[parametros-temporizacion]] · [[vliw]]

Latencias oficiales del enunciado:
- L.D (carga FP): MEM = 2 ciclos → resultado disponible tras 2 ciclos desde emisión.
- S.D (almacenamiento FP): MEM = 2 ciclos.
- ADD.D, MUL.D, DIV.D (aritmética FP): EX = 2 ciclos → resultado disponible tras 2 ciclos.
- DADDUI (aritmética entera): "resto de steps" = 1 ciclo.
- BNEZ (salto): "resto de steps" = 1 ciclo (resolución en ID/EX).
Estas latencias determinan la distancia mínima entre productor y consumidor con forwarding.

> Assume the following timing parameters: 2 cycles for the MEM step of loads and stores, 2 cycles for the EX step of arithmetic operations, and 1 cycle for the rest of steps.
> — `repo:datos/temarios/AC/examenes/January2016.pdf`

Relacionado: [[problema-de-planificacion-vliw-con-desenrollado-de-bucle-exa]]
