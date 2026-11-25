---
tipo: "receta"
titulo: "Cómo corregir solapes en diagramas de secuencia pgf-umlsd con bloques alt"
temas: ["latex", "pgf-umlsd", "tikz"]
claves: ["sdblock", "alt", "flechas", "línea divisoria", "solape", "revisar_maquetacion.py"]
proyectos: ["memoria-procesos"]
fuentes: ["chapters/04-descripcion.tex (diagrama fig:sec-baja)"]
confianza: "propuesto"
fecha: "2026-11-25"
actualizado: "2026-11-25"
---

Temas: [[latex]] · [[pgf-umlsd]] · [[tikz]]

Cuando `revisar_maquetacion.py` detecta solapes en un diagrama de secuencia con bloques `alt`:
1. Añadir un mensaje vacío (`\mess{participante}{ }{otro}`) justo antes del primer `sdblock` para crear espacio vertical y bajar la línea divisoria.
2. Si el solape es horizontal, aumentar la distancia entre instancias con `\newinst[4]{...}` (en lugar de `[3]` o `[2]`).
3. Evitar anidar `sdblock` dentro de `call`; cerrar todas las llamadas antes de abrir el primer `alt`.
4. Si el problema persiste, dividir el diagrama en dos: uno para el flujo normal y otro para el flujo de error, cada uno sin `alt`.
5. Volver a compilar y ejecutar `revisar_maquetacion.py` hasta que no reporte fallos en ese diagrama.

> Las flechas discontinuas del bloque alt inferior ('403' y la respuesta desde el Servicio) cruzan por encima del texto o de los bordes internos del frame alt sin dejar espacio adecuado.; La línea horizontal punteada divisoria del bloque 'alt / ultimo admin' corta la zona visual de interacción de la API y el Servicio.
> — `chapters/04-descripcion.tex (diagrama fig:sec-baja)` (cita sin comprobar)

Relacionado: [[diagramas-de-secuencia-con-pgf-umlsd-entorno-sequencediagram]] · [[como-corregir-solapes-en-diagramas-de-secuencia-pgf-umlsd]] · [[como-corregir-diagramas-de-secuencia-pgf-umlsd-para-que-no-c]] · [[como-replantear-diagramas-de-secuencia-pgf-umlsd-para-evitar]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
