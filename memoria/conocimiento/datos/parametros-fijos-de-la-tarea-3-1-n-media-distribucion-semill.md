---
tipo: "dato"
titulo: "Parámetros fijos de la Tarea 3.1 (N, media, distribución, semilla)"
temas: ["ac", "datos", "parametros"]
claves: ["N=20000000", "media=50.0f", "uniform_real_distribution", "mt19937", "seed=123"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab4.zip!tarea3_1_lista.cpp"]
confianza: "verificado"
fecha: "2026-11-19"
actualizado: "2026-11-19"
---

Temas: [[ac]] · [[datos]] · [[parametros]]

Valores constantes definidos en el código base:
- `N = 20'000'000` (20 millones de elementos)
- Tipo de dato: `float` (4 bytes) → vector ocupa ~80 MB, lista mucho más por overhead de nodos (punteros next/prev + allocator metadata ≈ 24–32 bytes/nodo → 500–600 MB totales).
- Generador: `std::mt19937 rng(123)` (semilla fija 123 → resultados reproducibles).
- Distribución: `std::uniform_real_distribution<float> dist(0.0f, 100.0f)`.
- Media para normalización: `const float media = 50.0f` (centro de la distribución).
- Salida: `suma de cuadrados = %.3f` (double acumulado para evitar overflow/precisión).

> constexpr std::size_t N = 20'000'000;
> — `repo:datos/temarios/AC/Practicas/Code_Lab4.zip!tarea3_1_lista.cpp`

Relacionado: [[optimizar-std-list-a-std-vector-con-reserva-y-fusion-de-bucl]]
