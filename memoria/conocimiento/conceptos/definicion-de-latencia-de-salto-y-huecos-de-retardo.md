---
tipo: "concepto"
titulo: "Definición de latencia de salto y huecos de retardo"
temas: ["ac", "pipeline", "saltos"]
claves: ["latencia salto", "huecos retardo", "IF", "ID", "EX", "MEM", "WB"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[pipeline]] · [[saltos]]

La latencia de un salto son los ciclos extra que transcurren desde que la instrucción de salto está en la etapa IF (Instruction Fetch) hasta que se resuelve (se sabe si se toma y a dónde). Esos ciclos de latencia se llaman "huecos de retardo" porque el cauce (pipeline) debe esperar o se llenan con instrucciones inútiles (burbujas) hasta que se conoce el resultado del salto.

> Latencia del salto: Ciclos adicionales entre la etapa IF de salto y su resolución. Se denominan huecos de retardo a los ciclos de latencia
> — `repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4.pdf` (cita sin comprobar)
