---
tipo: "decision"
titulo: "ROB de 4 entradas limita ventana de instrucciones en vuelo (examen AC 2014)"
temas: ["ac", "pipeline", "tomasulo"]
claves: ["ROB 4 entradas limite ventana", "emision bloqueada ROB lleno"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2014.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]] · [[tomasulo]]

El ROB de solo 4 entradas es un cuello de botella estructural severo. En la simulación de la parte b), la emisión (Issue) de una instrucción se bloquea si el ROB está lleno (4 instrucciones en vuelo sin haber hecho commit). Dado que la terminación (commit) es en orden y requiere que la instrucción esté en cabeza de ROB y haya escrito resultado, las instrucciones de larga latencia (MUL.D 4 ciclos ejecución + escritura + commit) ocupan entradas ROB muchos ciclos. Esto causa paradas de emisión (structural hazard por ROB lleno) que hay que reflejar en la tabla de ciclos. Ejemplo: si se emiten 4 instrucciones seguidas, la 5ª espera a que la 1ª haga commit.

> ROB de 4 entradas" y "Supón que el ROB tiene inicialmente todas sus entradas vacías.
> — `repo:datos/temarios/AC/examenes/Junio2014.pdf` (cita sin comprobar)

Relacionado: [[buffer-de-reordenamiento-rob-en-tomasulo-con-especulacion-ca]] · [[analisis-de-dependencias-en-bucle-con-add-d-y-s-d-misma-iter]]
