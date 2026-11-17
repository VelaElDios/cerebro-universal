---
tipo: "receta"
titulo: "Estructura del procesador Tomasulo: CDB, estaciones de reserva y buffers"
temas: ["ac", "arquitectura", "bus-comun-datos", "planificacion-dinamica", "tomasulo"]
claves: ["CDB", "bus común de datos", "estaciones de reserva", "buffers carga", "buffers almacenamiento", "sumadores FP", "multiplicadores FP"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[arquitectura]] · [[bus-comun-datos]] · [[planificacion-dinamica]] · [[tomasulo]]

Componentes clave:
- Cola de instrucciones (operaciones FP) alimentada desde la unidad de instrucción.
- Registros FP conectados por dos buses a unidades funcionales y uno a buffers de almacenamiento.
- Estaciones de reserva para sumadores FP y multiplicadores FP (cada una con sus buffers).
- Buffers de carga y buffers de almacenamiento para tráfico memoria.
- Bus Común de Datos (CDB): único canal por el que TODOS los resultados (UF y memoria) viajan al banco de registros FP, a las estaciones de reserva y a los buffers de almacenamiento que los esperan.
- Cada entrada (estación o buffer) lleva un campo de etiqueta (tag) para seguimiento de dependencias.

> Todos los resultados de las unidades funcionales y de memoria se envían al bus común de datos (CDB), que van al fichero de registros FP, a las estaciones de reserva y buffers de almacenamiento. Todos los buffers y estaciones de reserva tienen campos de tipo etiqueta, empleados para el control de riesgos
> — `repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf` (cita sin comprobar)
