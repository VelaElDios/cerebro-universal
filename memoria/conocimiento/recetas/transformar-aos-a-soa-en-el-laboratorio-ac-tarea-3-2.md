---
tipo: "receta"
titulo: "Transformar AoS a SoA en el laboratorio AC (tarea 3.2)"
temas: ["ac", "cpp", "refactoring", "soa"]
claves: ["TODO1", "TODO2", "TODO3", "Particulas", "vector<Particula>"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab4/tarea3_2_aos.cpp"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[cpp]] · [[refactoring]] · [[soa]]

Pasos guiados por los TODOs del enunciado:
1. **TODO1** – Definir `struct Particulas { std::vector<int> id; std::vector<uint8_t> active; std::vector<int> data; std::vector<float> score; };`.
2. **TODO2** – Instanciar `Particulas p; p.id.resize(N); p.active.resize(N); …` y rellenar cada vector en bucle único (`p.id[i] = i & 0xFF; …`).
3. **TODO3** – Cambiar el bucle de acumulación a `for (int it=0; it<ITER; ++it) for (size_t i=0; i<N; ++i) suma += p.id[i];`.
4. Compilar ambas versiones: `g++ -O2 -o aos tarea3_2_aos.cpp` y `g++ -O2 -o soa tarea3_2_soa.cpp`.
5. Verificar que `suma` coincide y medir con `hyperfine ./aos ./soa` y `perf stat -e cache-references,cache-misses,instructions,cycles ./aos ./soa`.

> // a) Transforma el "vector de estructuras" en una "estructura de // vectores" (SoA): // struct Particulas { // vector<int> id;
> — `repo:datos/temarios/AC/Practicas/Code_Lab4/tarea3_2_aos.cpp`

Relacionado: [[aos-vs-soa-desperdicio-de-ancho-de-banda-en-cache]] · [[transformacion-aos-a-soa-para-optimizacion-de-cache-esquema]] · [[porcentaje-de-aprovechamiento-de-linea-de-cache-en-aos-acced]] · [[tarea-3-2-aos-vs-soa-marcada-como-opcional-en-anexo-c]]
