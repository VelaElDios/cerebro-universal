---
tipo: "dato"
titulo: "Evolución de la dirección base x1 en las dos iteraciones del ejemplo"
temas: ["ac", "bucle", "direccionamiento", "tomasulo"]
claves: ["x1", "80", "72", "direccion base", "carga", "almacenamiento"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[bucle]] · [[direccionamiento]] · [[tomasulo]]

El registro base `x1` vale 80 durante los ciclos 2-5 (primera iteración) y cambia a 72 a partir del ciclo 6 (segunda iteración). Los buffers de carga reflejan este cambio: «Carga 1» tiene dirección 80; «Carga 2» (ciclo 6) tiene dirección 72. Los buffers de almacenamiento «Almac 1» y «Almac 2» reciben las mismas direcciones 80 y 72 respectivamente cuando sus correspondientes multiplicaciones completan y pasan el resultado al buffer de almacenamiento.

> x1 = 80                                                           x1 = 72
> — `repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf` (cita sin comprobar)

Relacionado: [[buffers-de-carga-y-almacenamiento-en-tomasulo]] · [[valores-concretos-de-x1-y-direcciones-de-memoria-en-la-simul]] · [[evolucion-del-registro-base-x1-y-qi-de-registros-fp-en-el-ej]] · [[gestion-de-buffers-de-carga-almacenamiento-con-direcciones-d]]
