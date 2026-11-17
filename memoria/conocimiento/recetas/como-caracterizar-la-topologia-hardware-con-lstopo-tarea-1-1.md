---
tipo: "receta"
titulo: "Cómo caracterizar la topología hardware con lstopo (Tarea 1.1)"
temas: ["ac", "cachés", "hardware", "topología"]
claves: ["lstopo", "hwloc", "P-cores", "E-cores", "L1", "L2", "L3", "sockets"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Practica3.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[cachés]] · [[hardware]] · [[topología]]

Ejecutar `lstopo` (o `lstopo -v`) para obtener la topología completa. Rellenar una tabla con: número de cores, tamaños de caché L1 (instrucción y datos), L2, L3, y si alguna caché es compartida. Esta información es base para interpretar luego los saltos de latencia en la Tarea 1.2 y para calcular el techo de memoria en el modelo Roofline.

> Utilizando el comando lstopo identificaremos la topología de hardware del sistema: número de sockets, distribución de los núcleos físicos (distinguiendo entre núcleos de alto rendimiento o P-cores y núcleos eficientes o E-cores) y los tamaños de los niveles de caché L1, L2 y L3.
> — `repo:datos/temarios/AC/Practicas/Practica3.pdf`

Relacionado: [[aos-vs-soa-desperdicio-de-ancho-de-banda-en-cache]]
