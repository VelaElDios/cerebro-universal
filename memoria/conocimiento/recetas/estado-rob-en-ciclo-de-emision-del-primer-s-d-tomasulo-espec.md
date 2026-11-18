---
tipo: "receta"
titulo: "Estado ROB en ciclo de emisión del primer S.D (Tomasulo especulación)"
temas: ["ac", "rob", "tomasulo"]
claves: ["ROB", "Reorder Buffer", "10 entradas", "emisión S.D", "estado instrucciones"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2012.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[rob]] · [[tomasulo]]

En el ciclo donde se emite el primer S.D (S.D F8, 8(R1)), el ROB contiene las instrucciones emitidas hasta ese momento en orden de programa: 1) L.D F0,0(R1), 2) L.D F2,0(R2), 3) ADD.D F4,F0,F2, 4) L.D F6,0(R3), 5) MUL.D F8,F4,F6, 6) ADD.D F10,F6,F12, 7) S.D F8,8(R1) ← emitiéndose ahora. Cada entrada ROB: Ocupada=Sí, Instrucción, Estado (Ejecutando/Completado/Escribiendo/Confirmado), Destino (registro F8 para S.D, o dirección memoria para store), Valor (resultado o dirección efectiva calculada). Los stores en ROB esperan dato a almacenar (F8) y dirección efectiva. El ROB gestiona la confirmación en orden (commit) y la especulación (recuperación ante fallo predicción).

> Sólo para alumnos con Temas 4-6. Indica en la siguiente tabla el estado del ROB (suponiendo que tiene 10 entradas) en el ciclo en el que la primera instrucción S.D es emitida.
> — `repo:datos/temarios/AC/examenes/Enero2012.pdf`

Relacionado: [[configuracion-tomasulo-con-especulacion-para-examen-enero-20]] · [[rob-de-10-entradas-para-secuencia-de-8-instrucciones-en-exam]] · [[como-simular-tomasulo-especulativo-con-rob-de-4-entradas-y-l]] · [[como-resolver-tabla-de-estado-en-tomasulo-con-rob-y-especula]]
