---
tipo: "receta"
titulo: "Cómo leer la tabla de estado de Tomasulo en ciclos consecutivos"
temas: ["ac", "depuracion", "simulacion", "tomasulo"]
claves: ["estado instrucciones", "buffers carga almacenamiento", "estaciones reserva", "registro estado", "Qi", "Vj Vk Qj Qk"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[depuracion]] · [[simulacion]] · [[tomasulo]]

Para interpretar la simulación:
1. **Estado de instrucciones**: columnas Emisión, Ejecución, Escritura resultado muestran cuándo entra en cola, cuándo empieza ejecución y cuándo escribe en CDB.
2. **Buffers carga/almacén**: "Ocupada=SI" indica buffer activo; "Direc." es dirección efectiva (aquí 80, 72, 64); "Qi" etiqueta la estación que consumirá el dato (para cargas) o el productor (para almacenes).
3. **Estaciones de reserva**: "Op" muestra operación y ciclos restantes (ej. "Mult 4" = 4 ciclos para terminar). "Vj/Vk" = valor disponible; "Qj/Qk" = etiqueta del productor pendiente. Cuando Qj/Qk se resuelven, la estación pasa a "SI" en Vj/Vk y Op decrementa cada ciclo.
4. **Estado de registros**: "Qi" por registro indica qué estación/buffer producirá el próximo valor (renombrado). Cuando Qi se vacía, el valor real está en el registro arquitectónico.

> Buffers de carga/almac. Estaciones de reserva Nombre Ocupada Direc. Qi Nombre Ocupada Op Vj Vk Qj Qk Carga 1 SI 80 Suma 1 NO Mult 1 SI Mult R(f2) Carga 1
> — `repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf` (cita sin comprobar)

Relacionado: [[buffers-de-carga-y-almacenamiento-en-tomasulo]] · [[como-leer-la-tabla-de-estado-de-instrucciones-en-simulacion]] · [[tabla-de-estado-de-estacion-de-reserva-en-tomasulo-campos-y]] · [[como-se-traza-la-ejecucion-ciclo-a-ciclo-en-el-algoritmo-de]]
