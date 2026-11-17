---
tipo: "dato"
titulo: "Porcentaje de aprovechamiento de línea de caché en AoS accediendo solo a id"
temas: ["ac", "aos", "cache", "soa"]
claves: ["Particula.id", "línea de caché 64 Bytes", "porcentaje aprovechamiento", "3.2.c"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Practica4.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[aos]] · [[cache]] · [[soa]]

Pregunta de análisis (tarea 3.2.c): en la versión AoS (`std::vector<Particula>`), si el bucle solo lee `Particula.id`, ¿qué % de cada línea de caché de 64 Bytes se usa realmente? Requiere conocer el tamaño de `Particula` (incluyendo padding/alignment) para calcular: `(sizeof(int) / sizeof(Particula)) * 100%` si los objetos están contiguos, o `(elementos_por_línea * sizeof(int) / 64) * 100%`. La respuesta numérica no está en el texto; es ejercicio para el alumno.

> 3.2.c Si el algoritmo solo accede al campo Particula.id. ¿Qué porcentaje de espacio de cada línea de cache estamos aprovechando en la versión AoS?
> — `repo:datos/temarios/AC/Practicas/Practica4.pdf`

Relacionado: [[aos-vs-soa-desperdicio-de-ancho-de-banda-en-cache]] · [[transformacion-aos-a-soa-para-optimizacion-de-cache-esquema]]
