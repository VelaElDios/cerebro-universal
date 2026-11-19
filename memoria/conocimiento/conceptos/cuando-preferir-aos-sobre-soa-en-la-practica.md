---
tipo: "concepto"
titulo: "Cuándo preferir AoS sobre SoA en la práctica"
temas: ["ac", "diseno-datos", "tradeoffs", "aos-soa"]
claves: ["AoS", "SoA", "locality", "encapsulation", "SIMD", "cache-line"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab4/tarea3_2_aos.cpp", "repo:datos/temarios/AC/Practicas/Code_Lab4.zip!tarea3_2_aos.cpp"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-19"
---

Temas: [[ac]] · [[diseno-datos]] · [[tradeoffs]]

Respuesta esperada en el análisis del alumno (extraída de la pregunta final del enunciado):
- **AoS** cuando se accede a **todos o la mayoría de los campos** de cada elemento (p. ej., renderizado de vértices: posición+normal+UV+color), ya que mantiene la localidad espacial del objeto completo y simplifica la encapsulación/serialización.
- **SoA** cuando los kernels usan **subconjuntos de campos** (columnares) o se busca vectorización SIMD ancha sobre un solo campo.
- Híbridos (AoSoA: tiles de 4-8 estructuras) son comunes en motores de partículas/gráficos para caber en L1 y permitir SOA dentro del tile.

> - ¿En qué escenarios prácticos sería preferible usar AoS sobre SoA?
> — `repo:datos/temarios/AC/Practicas/Code_Lab4/tarea3_2_aos.cpp`

Relacionado: [[aos-vs-soa-desperdicio-de-ancho-de-banda-en-cache]] · [[pointer-chasing-en-std-list-vs-acceso-contiguo-en-std-vector]] · [[transformacion-aos-a-soa-para-optimizacion-de-cache-esquema]] · [[tarea-3-2-aos-vs-soa-marcada-como-opcional-en-anexo-c]]

## Ampliación (2026-11-19, )
Razones para elegir AoS (Array of Structures) frente a SoA:
- **Localidad de objeto**: cuando se accede a *todos* o *la mayoría* de los campos de una entidad junta (p. ej., renderizado de partículas donde se leen posición, velocidad, color, vida a la vez).
- **Encapsulamiento y OOP**: código más limpio, constructores, destructores, invariantes de clase, herencia.
- **Serialización/deserialización**: volcar un array de structs contiguo es trivial (memcpy, writev, MPI, GPU buffers).
- **APIs y bibliotecas**: muchas esperan `std::vector<Particle>` o `Particle*`.
- **Pequeños conjuntos de datos**: si cabe en L1, el overhead de SoA (vectores separados, indirecciones) no compensa.
- **Actualizaciones atómicas/transaccionales**: modificar una partícula completa de forma consistente es más fácil en AoS.
SoA gana cuando hay **acceso selectivo a subconjuntos de campos** (columnar) y **grandes volúmenes** que saturan ancho de banda de memoria.
