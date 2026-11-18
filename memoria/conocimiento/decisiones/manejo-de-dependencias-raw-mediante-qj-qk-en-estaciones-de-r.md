---
tipo: "decision"
titulo: "Manejo de dependencias RAW mediante Qj/Qk en estaciones de reserva"
temas: ["ac", "arquitectura", "tomasulo"]
claves: ["RAW", "Qj", "Qk", "dependencia", "forwarding"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[arquitectura]] · [[tomasulo]]

Cuando un operando no está listo, su Qj/Qk apunta a la estación de reserva que lo producirá. Cuando esa estación termina, difunde el resultado en el bus común (CDB) y todas las estaciones con ese Qj/Qk capturan el valor (Vj/Vk) y ponen Qj/Qk a 0. Ejemplo: Mult1 espera Qj=Carga2 (f2) y tiene Vk=R(f4); Suma1 espera Qj=Carga1 (f6) y Qk=Carga2 (f2); Mult2(DIV) espera Qj=Mult1 (f0) y Qk=Carga1 (f6).

> Mult 1 SI Mult R(f4) Carga 2 Suma 1 SI Sub M(34+x2) Carga 2 Mult 1 SI Mult M(45+x3) R(f4) Mult 2 SI DIv M(34+x2) Mult 1
> — `repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf` (cita sin comprobar)

Relacionado: [[estructura-de-una-estacion-de-reserva-en-tomasulo]] · [[campos-qj-y-qk-en-estaciones-de-reserva-de-tomasulo]] · [[tabla-de-estado-de-estacion-de-reserva-en-tomasulo-campos-y]]
