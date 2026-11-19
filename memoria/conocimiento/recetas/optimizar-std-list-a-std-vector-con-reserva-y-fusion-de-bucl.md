---
tipo: "receta"
titulo: "Optimizar std::list a std::vector con reserva y fusión de bucles (Tarea 3.1 AC)"
temas: ["ac", "cache", "cpp", "memoria", "optimizacion"]
claves: ["std::list", "std::vector", "reserve", "loop fusion", "pointer chasing", "cache miss", "temporal locality", "hyperfine", "perf"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab4.zip!tarea3_1_lista.cpp"]
confianza: "propuesto"
fecha: "2026-11-19"
actualizado: "2026-11-19"
---

Temas: [[ac]] · [[cache]] · [[cpp]] · [[memoria]] · [[optimizacion]]

**Problema base**: Código que usa `std::list<float>` para 20M elementos, con dos bucles separados: (1) normalización restando media, (2) suma de cuadrados. Cada `push_back` hace `new` individual; iteradores saltan entre nodos dispersos en heap → *pointer chasing* y *cache misses*. Dos pasadas rompen localidad temporal: al empezar la segunda, los primeros elementos ya salieron de L1/L2.

**Optimización en dos pasos (TODOs):**

1. **TODO1 - Contenedor contiguo + reserva única**  
   ```cpp
   // Antes
   std::list<float> lecturas;
   for (size_t i = 0; i < N; ++i) lecturas.push_back(dist(rng));

   // Después
   std::vector<float> lecturas;
   lecturas.reserve(N);           // una sola asignación de N*4 bytes
   for (size_t i = 0; i < N; ++i) lecturas.push_back(dist(rng));
   ```
   - `reserve(N)` evita reasignaciones y copia de elementos al crecer.
   - `std::vector` garantiza contigüidad → prefetching hardware, acceso secuencial predecible.

2. **TODO2 - Fusión de bucles (loop fusion / loop jamming)**  
   ```cpp
   // Antes: dos bucles
   for (auto it = lecturas.begin(); it != lecturas.end(); ++it) *it -= media;
   double suma = 0.0;
   for (auto it = lecturas.begin(); it != lecturas.end(); ++it)
       suma += static_cast<double>(*it) * static_cast<double>(*it);

   // Después: un solo bucle índice
   double suma = 0.0;
   for (size_t i = 0; i < N; ++i) {
       float norm = lecturas[i] - media;   // normaliza
       lecturas[i] = norm;                 // opcional: guarda normalizado si se necesita luego
       suma += static_cast<double>(norm) * static_cast<double>(norm);
   }
   ```
   - El elemento se lee, normaliza, eleva al cuadrado y acumula mientras sigue en L1.
   - Elimina la segunda pasada completa sobre 80 MB (20M × 4 B).

**Compilación y verificación:**
```bash
g++ -O2 -o lista tarea3_1_lista.cpp
g++ -O2 -o vector tarea3_1_vector.cpp
./lista && ./vector   # misma salida numérica
```

**Benchmarking sugerido:**
```bash
hyperfine --warmup 3 './lista' './vector'
perf stat -e cache-misses,cache-references,instructions,cycles ./lista
perf stat -e cache-misses,cache-references,instructions,cycles ./vector
```
Métricas clave: *cache-misses* (↓ drástico), *IPC* (↑), *cycles* (↓). Justificar con localidad espacial (vector contiguo) y temporal (un solo pase).

> std::list provoca "pointer chasing": cada nodo reside en una dirección arbitraria del heap y cada ++it es un salto impredecible -> cache miss.
> — `repo:datos/temarios/AC/Practicas/Code_Lab4.zip!tarea3_1_lista.cpp` (cita sin comprobar)
