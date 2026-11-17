---
tipo: "receta"
titulo: "Cómo evoluciona la tabla de estaciones de reserva en Tomasulo (ciclos 7-13)"
temas: ["ac", "estaciones-reserva", "simulacion", "tomasulo"]
claves: ["Suma 1", "Suma 2", "Suma 3", "Mult 1", "Mult 2", "Ocupada", "Op", "Vj", "Vk", "Qj", "Qk"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[estaciones-reserva]] · [[simulacion]] · [[tomasulo]]

Evolución clave ciclos 7→13:
- Ciclo 7: Suma1(Sub, Qj=M(34+x2), Qk=M(45+x3)), Suma2(Sum, Qk=M(45+x3), Qj=Suma1), Mult1(Mult, Vj=M(45+x3), Vk=R(f4)), Mult2(Div, Qj=M(34+x2), Qk=Mult1). Suma3 libre.
- Ciclo 8: Suma1 libre (completó sub). Suma2(Sum, Vj=M()-M(), Qk=M(45+x3)). Mult1 y Mult2 igual.
- Ciclo 9: Suma2 libre. Mult1 y Mult2 siguen ejecutando (latencias largas).
- Ciclos 10-13: Solo Mult1 y Mult2 ocupados. Contadores de ciclos restantes en columna "Ocupada" (Mult1: 8→7→6→5→4→3→2; Mult2: 8→7→6→5→4→3→2) indican latencia multiplicación=10 ciclos, división=10+ ciclos.
- Cuando una estación libera, Ocupada=NO y Op se borra.

> Estaciones de reserva        Nombre          Ocupada         Op                 Vj       Vk         Qj      Qk Suma 1              SI            Sub          M(34+x2) M(45+x3) Suma 2              SI            Sum                   M(45+x3) Suma 1 Mult 1              SI            Mult         M(45+x3)     R(f4) Mult 2              SI            DIv                     M(34+x2)      Mult 1
> — `repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf` (cita sin comprobar)

Relacionado: [[algoritmo-tomasulo-origen-y-objetivo-cpi1]] · [[buffers-de-carga-y-almacenamiento-en-tomasulo]]
