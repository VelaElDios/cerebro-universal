---
tipo: "receta"
titulo: "Transformación de AoS a SoA para kernel de suma de IDs"
temas: ["ac", "cpp", "optimizacion-memoria", "refactoring"]
claves: ["Particulas", "vector<int>", "vector<uint8_t>", "vector<float>", "reserva", "resize"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab4.zip!tarea3_2_aos.cpp"]
confianza: "propuesto"
fecha: "2026-11-19"
actualizado: "2026-11-19"
---

Temas: [[ac]] · [[cpp]] · [[optimizacion-memoria]] · [[refactoring]]

Pasos para convertir el código base (tarea3_2_aos.cpp) a SoA (tarea3_2_soa.cpp):
1. Definir struct Particulas con cuatro vectores separados: `id`, `active`, `data`, `score`.
2. En inicialización (TODO2): reservar capacidad `N` en cada vector (`reserve(N)` o `resize(N)`) y rellenar campo a campo: `particulas.id[i] = i & 0xFF; particulas.active[i] = i & 1; particulas.data[i] = i; particulas.score[i] = 0.5f * i;`.
3. En bucle de acumulación (TODO3): iterar solo sobre `particulas.id[i]` en lugar de `particulas[i].id`.
4. Compilar ambos con `g++ -O2 -o aos tarea3_2_aos.cpp` y `g++ -O2 -o soa tarea3_2_soa.cpp`.
5. Verificar que la suma final (`checksum`) coincide.

> struct Particulas { std::vector<int> id; std::vector<uint8_t> active; std::vector<int> data; std::vector<float> score; };
> — `repo:datos/temarios/AC/Practicas/Code_Lab4.zip!tarea3_2_aos.cpp` (cita sin comprobar)
