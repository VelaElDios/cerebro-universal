---
tipo: "dato"
titulo: "Parámetros fijos del benchmark: semilla, accesos, formato salida"
temas: ["ac", "benchmark", "parametros", "reproducibilidad"]
claves: ["seed 42", "mt19937_64", "50M accesos", "printf", "%12zu %14.2f"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab3/tarea1_2_mem_latency.cpp"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[benchmark]] · [[parametros]] · [[reproducibilidad]]

**Semilla RNG:** 42 (fija, reproducible). **Generador:** `std::mt19937_64` (Mersenne Twister 64-bit). **Accesos por medición:** 50'000'000 (50 millones). **Formato salida:** dos columnas alineadas: tamaño en KiB (entero, 12 chars) y latencia en ns (float con 2 decimales, 14 chars). Cabecera: "Tamaño(KiB)  Latencia(ns)". Esto permite parseo fácil y gráficas directas con gnuplot, Python, Excel, etc.

> std::mt19937_64 rng(42);
constexpr std::size_t kAccesses = 50'000'000;
std::printf("%12s %14s\n", "Tamaño(KiB)", "Latencia(ns)");
std::printf("%12zu %14.2f\n", bytes / 1024, ns);
> — `repo:datos/temarios/AC/Practicas/Code_Lab3/tarea1_2_mem_latency.cpp` (cita sin comprobar)

Relacionado: [[como-compilar-y-ejecutar-el-benchmark-de-latencia-de-memoria]] · [[rango-de-working-set-4-kib-a-256-mib-en-potencias-de-2]] · [[parametros-fijos-del-experimento-de-branchless-tamanio-repet]] · [[uso-de-semilla-fija-42-en-mt19937-para-reproducibilidad-del]]
