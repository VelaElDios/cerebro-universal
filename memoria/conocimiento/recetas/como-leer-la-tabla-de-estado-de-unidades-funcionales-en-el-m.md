---
tipo: "receta"
titulo: "Cómo leer la tabla de estado de unidades funcionales en el marcador de Tomasulo"
temas: ["ac", "lectura-tablas", "scoreboard", "tomasulo", "unidades-funcionales", "qj-qk-rj-rk"]
claves: ["UF", "Ocupada", "Op", "Fi", "Fj", "Fk", "Qj", "Qk", "Rj", "Rk", "ciclos que quedan"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[lectura-tablas]] · [[scoreboard]] · [[tomasulo]] · [[unidades-funcionales]]

Cada fila representa una unidad funcional. Columnas: Nombre (tipo UF), Ocupada (SI/NO), Op (operación en curso), Fi (registro destino), Fj/Fk (registros origen), Qj/Qk (número de UF que producirá el operando, 0 si ya disponible), Rj/Rk (bandera: SI si el operando aún no está listo, NO si ya lo está). "Ciclos que quedan" indica latencia restante de la operación actual. Ejemplo: Mult1 en ciclo 10 está ocupada haciendo fmul.d f0,f2,f4 con 10 ciclos restantes; Qj=Qk=SI indica que f2 y f4 aún no están listos (producidos por otras UF).

> Estado de las unidades funcionales                          UF           Nombre        Ocupada           Op       Fi    Fj        Fk   Qj Qk   Rj Rk                          1             Entera     10     2             Mult1            SI            Mult     f0    f2        f4           SI SI
> — `repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf` (cita sin comprobar)

## Ampliación (2026-11-17, )
Cada fila de unidad funcional muestra: UF (índice), Nombre (Entera, Mult1, Mult2, Suma, Divide), Ocupada (SI/NO o ciclos restantes), Op (operación), Fi (registro destino), Fj/Fk (registros fuente), Qj/Qk (índice de UF que producirá el operando, o vacío si ya disponible), Rj/Rk (banderas NO/SI indicando si el operando está listo). Ejemplo: Mult1 en ciclo 16 está ocupada (3 ciclos restantes), opera Mult, destino f0, fuentes f2 y f4, sin dependencias (Qj/Qk vacíos, Rj=NO, Rk=NO).
