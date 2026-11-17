---
tipo: "concepto"
titulo: "Uso de buffers de carga en Tomasulo (Load Buffers)"
temas: ["ac", "buffer-carga", "direccion-efectiva", "tomasulo"]
claves: ["Carga 1", "Carga 2", "Carga 3", "Direccion", "M(34+x2)", "M(45+x3)"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[buffer-carga]] · [[direccion-efectiva]] · [[tomasulo]]

Tres buffers de carga (Carga 1, 2, 3). En ciclo 7 todos están libres (Ocupada=NO, Dirección vacía).
- Las dos cargas (fld f6,34(x2) y fld f2,45(x3)) se emitieron en c1 y c2, usaron buffers (probablemente Carga 1 y 2), calcularon direcciones efectivas M(34+x2) y M(45+x3) en emisión, y completaron en c4 y c5.
- En c7 los buffers ya se liberaron para siguientes cargas/almacenamientos.
- La dirección efectiva se pasa a estaciones de reserva como Vj/Vk (valor) o Qj/Qk (tag) según esté lista. En c7, Suma1 y Suma2 aún tienen Qj/Qk=M(34+x2) y M(45+x3) porque las cargas acaban de terminar (c4/c5) y el CDB aún no ha propagado los valores a todas las estaciones.

> Buffers de carga               Nombre      Ocupada     Dirección Carga 1        NO                   Carga 2        NO                   Carga 3        NO
> — `repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf` (cita sin comprobar)

Relacionado: [[buffers-de-carga-y-almacenamiento-en-tomasulo]] · [[algoritmo-tomasulo-origen-y-objetivo-cpi1]]
