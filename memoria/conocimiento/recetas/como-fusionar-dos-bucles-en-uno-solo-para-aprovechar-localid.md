---
tipo: "receta"
titulo: "Cómo fusionar dos bucles en uno solo para aprovechar localidad temporal en L1"
temas: ["ac", "bucles", "cpp", "optimizacion"]
claves: ["loop fusion", "temporal locality", "L1 cache", "single pass"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab4/tarea3_1_lista.cpp"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[bucles]] · [[cpp]] · [[optimizacion]]

Transformación de dos bucles separados en uno solo:
- Original (dos pasadas):
  ```cpp
  for (auto it = lecturas.begin(); it != lecturas.end(); ++it) *it -= media;
  double suma = 0.0;
  for (auto it = lecturas.begin(); it != lecturas.end(); ++it) suma += static_cast<double>(*it) * static_cast<double>(*it);
  ```
- Optimizado (una pasada, índice en vector):
  ```cpp
  double suma = 0.0;
  for (std::size_t i = 0; i < N; ++i) {
      float val = lecturas[i] - media;   // normaliza
      suma += static_cast<double>(val) * static_cast<double>(val); // acumula
  }
  ```
Ventaja: el valor normalizado se usa inmediatamente mientras sigue en L1, sin esperar a que la segunda pasada lo traiga de nuevo desde memoria.

> Fusionar ambos bucles en una sola pasada para normalizar y acumular el dato mientras sigue caliente en L1.
> — `repo:datos/temarios/AC/Practicas/Code_Lab4/tarea3_1_lista.cpp` (cita sin comprobar)

Relacionado: [[como-transformar-std-list-a-std-vector-con-reserva-previa-pa]] · [[interpretacion-de-regiones-memory-bound-vs-compute-bound-en]]
