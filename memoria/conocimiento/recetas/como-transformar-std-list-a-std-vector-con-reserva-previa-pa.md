---
tipo: "receta"
titulo: "Cómo transformar std::list a std::vector con reserva previa para mejorar localidad de caché"
temas: ["ac", "cpp", "memoria", "optimizacion"]
claves: ["std::vector", "reserve", "push_back", "cache locality", "pointer chasing"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab4/tarea3_1_lista.cpp"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[cpp]] · [[memoria]] · [[optimizacion]]

Pasos para optimizar la estructura de datos:
1. Cambiar `std::list<float> lecturas;` por `std::vector<float> lecturas;`.
2. Antes del bucle de llenado, llamar a `lecturas.reserve(N);` para reservar memoria contigua de una sola vez y evitar reasignaciones.
3. El bucle de llenado `lecturas.push_back(dist(rng));` funciona igual, pero ahora escribe en memoria contigua.
4. Compilar con `g++ -O2 -o vector tarea3_1_vector.cpp`.
5. Verificar que la salida numérica coincide con la versión lista.

> std::list provoca \"pointer chasing\": cada nodo reside en una dirección arbitraria del heap y cada ++it es un salto impredecible -> cache miss.
> — `repo:datos/temarios/AC/Practicas/Code_Lab4/tarea3_1_lista.cpp` (cita sin comprobar)

Relacionado: [[calculo-de-flops-ciclo-para-avx2-con-fma]] · [[patron-de-salto-de-latencia-en-fronteras-de-cache]] · [[calentamiento-warm-up-para-poblar-tlb-y-evitar-page-faults]]
