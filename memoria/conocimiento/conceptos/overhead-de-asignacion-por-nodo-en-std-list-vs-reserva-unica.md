---
tipo: "concepto"
titulo: "Overhead de asignación por nodo en std::list vs reserva única en std::vector"
temas: ["ac", "allocator", "cpp", "memoria"]
claves: ["new", "push_back", "reserve", "allocation overhead", "heap fragmentation"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab4.zip!tarea3_1_lista.cpp"]
confianza: "verificado"
fecha: "2026-11-19"
actualizado: "2026-11-19"
---

Temas: [[ac]] · [[allocator]] · [[cpp]] · [[memoria]]

**std::list**: cada `push_back` invoca `allocator_traits::allocate` → típicamente `::operator new(sizeof(Node))` → llamada al allocador del heap (malloc/arena). 20M llamadas a `new`:
- Overhead de allocador (metadata, locking en multihilo, búsqueda de bloque libre).
- Fragmentación de heap.
- Tiempo de construcción de cada nodo (inicializar punteros `next`, `prev`).

**std::vector + reserve(N)**: una sola asignación de `N * sizeof(float)` bytes (80 MB contiguos). `push_back` luego solo escribe en memoria ya reservada y incrementa `size_` → O(1) amortizado sin llamadas al allocador.

**Impacto medible**: en la fase de llenado, `vector+reserve` es órdenes de magnitud más rápido que `list`. Incluso sin `reserve`, `vector` hace reasignaciones logarítmicas (2×, 4×, 8×…), muy pocas comparadas con 20M `new` individuales.

> Cada push_back en una lista implica una reserva dinámica (llamada a new).
> — `repo:datos/temarios/AC/Practicas/Code_Lab4.zip!tarea3_1_lista.cpp`

Relacionado: [[optimizar-std-list-a-std-vector-con-reserva-y-fusion-de-bucl]] · [[pointer-chasing-en-std-list-vs-acceso-contiguo-en-std-vector]]
