---
tipo: "concepto"
titulo: "Diferencia entre buffers de carga y de almacenamiento en la simulación"
temas: ["ac", "almacenamiento", "buffers", "carga", "tomasulo"]
claves: ["Carga 1", "Carga 2", "Carga 3", "Almac 1", "Almac 2", "Almac 3", "Qi", "Direc"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[almacenamiento]] · [[buffers]] · [[carga]] · [[tomasulo]]

La tabla «Buffers de carga/almac.» tiene columnas: Nombre, Ocupada, Direc., Qi.
- Buffers de carga (Carga 1-3): Qi siempre vacío (la carga no depende de otra unidad; solo espera dirección). Cuando Ocupada=SI, Direc. tiene la dirección efectiva (80 o 72).
- Buffers de almacenamiento (Almac 1-3): Qi indica qué estación de reserva (Mult 1/2) proveerá el dato a almacenar. Direc. es la dirección efectiva. Almac 1 y 2 pasan a Ocupada=SI cuando su Mult correspondiente emite; Almac 3 nunca se usa en esta traza.

> Buffers de carga/almac.                                      Estaciones de reserva
> — `repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf`

Relacionado: [[flujo-de-datos-de-carga-multiplicacion-almacenamiento-en-buf]]
