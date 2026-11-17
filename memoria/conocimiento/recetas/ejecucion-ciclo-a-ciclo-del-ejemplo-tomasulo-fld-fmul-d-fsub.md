---
tipo: "receta"
titulo: "Ejecución ciclo a ciclo del ejemplo Tomasulo (fld, fmul.d, fsub.d, fdiv.d, fadd.d)"
temas: ["ac", "arquitectura", "tomasulo"]
claves: ["ciclo 1", "ciclo 2", "ciclo 3", "ciclo 4", "ciclo 5", "ciclo 6", "fld", "fmul.d", "fsub.d", "fdiv.d", "fadd.d"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[arquitectura]] · [[tomasulo]]

Secuencia de 6 ciclos para 6 instrucciones:
- Ciclo 1: Emisión fld f6,34(x2) → Load Buffer 1 (dir 34+x2); Qi(f6)=Carga1.
- Ciclo 2: Emisión fld f2,45(x3) → Load Buffer 2 (dir 45+x3); Qi(f2)=Carga2. La primera carga empieza ejecución (2-3 ciclos).
- Ciclo 3: Emisión fmul.d f0,f2,f4 → Mult1; Vk=R(f4), Qj=Carga2. Emisión fsub.d f8,f6,f2 → Suma1; Qj=Carga1, Qk=Carga2. Primera carga termina (ciclo 3) y escribe f6.
- Ciclo 4: Emisión fdiv.d f10,f0,f6 → Mult2(DIV); Qj=Mult1, Qk=Carga1. Emisión fsub.d → Suma1; Vj=M(34+x2), Qk=Carga2. Segunda carga termina (ciclo 4) y escribe f2.
- Ciclo 5: Emisión fadd.d f6,f8,f2 → Suma2; Qj=Suma1, Qk=M(45+x3). Mult1 y Mult2 en ejecución. Qi(f0)=Mult1, Qi(f8)=Suma1, Qi(f10)=Mult2, Qi(f6)=Suma2.
- Ciclo 6: Emisión fadd.d → Suma2 ocupada. Mult1, Suma1, Mult2 ejecutando. No hay bloqueo estructural.

> ciclo 1 Instrucción Emisión Ejecución Escritura resultado fld f6, 34(x2) 1 fld f2, 45(x3) fmul.d f0, f2, f4 fsub.d f8, f6, f2 fdiv.d f10, f0, f6 fadd.d f6, f8, f2
> — `repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf` (cita sin comprobar)

Relacionado: [[estructura-de-una-estacion-de-reserva-en-tomasulo]] · [[fichero-de-registros-con-campo-qi-en-tomasulo]] · [[buffers-de-carga-y-almacenamiento-en-tomasulo]]
