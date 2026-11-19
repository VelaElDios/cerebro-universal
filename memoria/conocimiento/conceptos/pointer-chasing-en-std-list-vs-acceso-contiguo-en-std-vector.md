---
tipo: "concepto"
titulo: "Pointer chasing en std::list vs acceso contiguo en std::vector"
temas: ["ac", "cache", "memoria", "punteros", "estructuras-datos", "cpp"]
claves: ["pointer chasing", "std::list", "std::vector", "heap allocation", "cache miss", "spatial locality"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab4/tarea3_1_lista.cpp", "repo:datos/temarios/AC/Practicas/Practica4.pdf", "repo:datos/temarios/AC/Practicas/Code_Lab4.zip!tarea3_1_lista.cpp"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-19"
---

Temas: [[ac]] · [[cache]] · [[memoria]] · [[punteros]]

`std::list` almacena cada elemento en un nodo separado asignado individualmente en el heap (`new` por `push_back`). Los nodos no tienen orden físico; el iterador `++it` sigue un puntero `next` a una dirección arbitraria. Esto causa:
- **Pointer chasing**: la CPU no puede predecir la siguiente dirección → fallos de caché (cache misses) en cada salto.
- **Sin localidad espacial**: líneas de caché traen solo un nodo (≈ 16-24 bytes), desperdiciando ancho de banda.
- **Overhead de asignación**: 20M llamadas a `new`/`delete` añaden latencia y fragmentación.

`std::vector` con `.reserve(N)` asigna un único bloque contiguo. El acceso `lecturas[i]` o iteradores son aritmética de punteros simple → prefetcher hardware funciona, se aprovecha toda la línea de caché (64 bytes = 16 floats), y no hay asignaciones por elemento.

> // - std::list provoca "pointer chasing": cada nodo reside en una dirección // arbitraria del heap y cada ++it es un salto impredecible -> cache miss.
> — `repo:datos/temarios/AC/Practicas/Code_Lab4/tarea3_1_lista.cpp`

Relacionado: [[patron-de-salto-de-latencia-en-fronteras-de-cache]] · [[calentamiento-warm-up-para-poblar-tlb-y-evitar-page-faults]] · [[como-transformar-std-list-a-std-vector-con-reserva-previa-pa]] · [[tecnica-pointer-chasing-para-medir-latencia-real-de-memoria]] · [[tamano-del-vector-y-bloque-en-bytes-y-lineas-de-cache]]

## Ampliación (2026-11-17, )
std::list dispersa nodos en heap; cada nodo = dato + puntero siguiente. Recorrerla salta de cache line en cache line → 1 cache-miss por elemento. std::vector almacena elementos contiguos; una cache line (64 B) trae varios elementos → accesos siguientes son cache hits. Solución cache-friendly: `std::vector<T> v; v.reserve(N);` para evitar reallocations y garantizar contigüidad desde el inicio. Ambos códigos deben producir idéntico resultado numérico.

## Ampliación (2026-11-19, )
**Pointer chasing**: en `std::list` cada nodo se asigna individualmente en el heap (`new` por `push_back`). Los nodos quedan dispersos en direcciones virtuales aleatorias. Al iterar (`++it`), el procesador debe seguir el puntero `next` de cada nodo → acceso a memoria impredecible → el prefetcher hardware no puede anticipar → *cache miss* casi garantizado por nodo.

**std::vector contiguo**: un único bloque de memoria contigua. Iterar con índice `v[i]` o iterador es acceso secuencial predecible → el prefetcher trae líneas de caché adelantadas → *spatial locality* óptima. Una sola asignación (`reserve` + `push_back` o `resize`) evita overhead de allocador y fragmentación.

**Impacto típico**: en recorridos lineales sobre millones de elementos, `std::vector` puede ser 5–20× más rápido que `std::list` solo por patrón de acceso a memoria, antes de considerar fusión de bucles.
