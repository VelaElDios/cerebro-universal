---
tipo: "concepto"
titulo: "Pointer chasing en std::list vs acceso contiguo en std::vector"
temas: ["ac", "cache", "memoria", "punteros", "estructuras-datos"]
claves: ["pointer chasing", "std::list", "std::vector", "heap allocation", "cache miss", "spatial locality"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab4/tarea3_1_lista.cpp", "repo:datos/temarios/AC/Practicas/Practica4.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[cache]] · [[memoria]] · [[punteros]]

`std::list` almacena cada elemento en un nodo separado asignado individualmente en el heap (`new` por `push_back`). Los nodos no tienen orden físico; el iterador `++it` sigue un puntero `next` a una dirección arbitraria. Esto causa:
- **Pointer chasing**: la CPU no puede predecir la siguiente dirección → fallos de caché (cache misses) en cada salto.
- **Sin localidad espacial**: líneas de caché traen solo un nodo (≈ 16-24 bytes), desperdiciando ancho de banda.
- **Overhead de asignación**: 20M llamadas a `new`/`delete` añaden latencia y fragmentación.

`std::vector` con `.reserve(N)` asigna un único bloque contiguo. El acceso `lecturas[i]` o iteradores son aritmética de punteros simple → prefetcher hardware funciona, se aprovecha toda la línea de caché (64 bytes = 16 floats), y no hay asignaciones por elemento.

> std::list provoca \"pointer chasing\": cada nodo reside en una dirección arbitraria del heap y cada ++it es un salto impredecible -> cache miss.
> — `repo:datos/temarios/AC/Practicas/Code_Lab4/tarea3_1_lista.cpp` (cita sin comprobar)

Relacionado: [[patron-de-salto-de-latencia-en-fronteras-de-cache]] · [[calentamiento-warm-up-para-poblar-tlb-y-evitar-page-faults]]

## Ampliación (2026-11-17, )
std::list dispersa nodos en heap; cada nodo = dato + puntero siguiente. Recorrerla salta de cache line en cache line → 1 cache-miss por elemento. std::vector almacena elementos contiguos; una cache line (64 B) trae varios elementos → accesos siguientes son cache hits. Solución cache-friendly: `std::vector<T> v; v.reserve(N);` para evitar reallocations y garantizar contigüidad desde el inicio. Ambos códigos deben producir idéntico resultado numérico.
