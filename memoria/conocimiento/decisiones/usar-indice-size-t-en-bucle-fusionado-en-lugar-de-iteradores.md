---
tipo: "decision"
titulo: "Usar índice size_t en bucle fusionado en lugar de iteradores"
temas: ["ac", "cpp", "estilo", "optimizacion"]
claves: ["size_t", "index loop", "iteradores", "vector", "loop fusion"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab4.zip!tarea3_1_lista.cpp"]
confianza: "verificado"
fecha: "2026-11-19"
actualizado: "2026-11-19"
---

Temas: [[ac]] · [[cpp]] · [[estilo]] · [[optimizacion]]

El enunciado sugiere explícitamente usar un bucle indexado con `std::size_t i` (`for (std::size_t i = 0; i < N; ++i)`) en lugar de iteradores (`for (auto it = v.begin(); ...)`).

**Razones:**
- Acceso directo `v[i]` es más claro para el compilador (elimina comprobaciones de iterador en modo debug, aunque en `-O2` se optimizan igual).
- Facilita vectorización automática (SIMD): el compilador ve un índice de inducción canónico y límites de bucle triviales → genera código AVX/SSE para procesar 4–8 floats por instrucción.
- Evita invalidación de iteradores si se hiciera `push_back` dentro (no es el caso aquí, pero es práctica segura).
- Coherente con `N` de tipo `std::size_t` y `v.size()`.

> Crea solo UNICO bucle que recorra el vector lecturas[i] desde (std::size_t i = 0; i < N; ++i)
> — `repo:datos/temarios/AC/Practicas/Code_Lab4.zip!tarea3_1_lista.cpp`

Relacionado: [[optimizar-std-list-a-std-vector-con-reserva-y-fusion-de-bucl]]
