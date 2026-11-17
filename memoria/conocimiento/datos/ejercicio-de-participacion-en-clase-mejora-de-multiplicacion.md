---
tipo: "dato"
titulo: "Ejercicio de participación en clase: mejora de multiplicación para speedup 5x con 96s de 120s"
temas: ["ac", "rendimiento"]
claves: ["participación en clase", "Moodle", "speedup", "Ley de Amdahl"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema1-Introduccion/Tema1 2026-27.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[rendimiento]]

Datos: T = 120 s, T_mul = 96 s (80%), T_no_mul = 24 s. Speedup objetivo = 5 → T' = 24 s. Como la parte no multiplicación ya tarda 24 s, la parte de multiplicación debería tardar 0 s → speedup infinito. Imposible. El ejercicio ilustra el límite de Amdahl: si la fracción no mejorable es f, el speedup máximo es 1/f. Aquí f = 0.2 → speedup máx = 5, pero solo si la parte mejorable se hace instantánea.

> Supongamos que un programa tarda en ejecutarse en una máquina 2 minutos, de los cuales 96 segundos corresponden a operaciones de multiplicar. ¿Cuánto tengo que mejorar la velocidad de multiplicación si quiero que el programa se ejecute cinco veces más rápido? Subirlo a Moodle antes del domingo 20 a las 23:59
> — `repo:datos/temarios/AC/Tema1-Introduccion/Tema1 2026-27.pdf` (cita sin comprobar)

Relacionado: [[como-resolver-un-problema-de-la-ley-de-amdahl-con-fraccion-m]]
