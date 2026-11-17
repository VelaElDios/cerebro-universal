---
tipo: "dato"
titulo: "Parámetros del experimento lista vs vector: N=20M, media=50.0f, semilla=123"
temas: ["ac", "benchmark", "experimento"]
claves: ["N=20000000", "media=50.0f", "mt19937", "seed=123", "uniform_real_distribution"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab4/tarea3_1_lista.cpp"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[benchmark]] · [[experimento]]

Valores fijos del código base para reproducibilidad:
- Tamaño del problema: `N = 20'000'000` elementos (20 millones de floats ≈ 80 MB).
- Generador: `std::mt19937 rng(123);` (semilla fija 123).
- Distribución: `std::uniform_real_distribution<float> dist(0.0f, 100.0f);`.
- Media de normalización: `const float media = 50.0f;`.
- Salida esperada: `std::printf("suma de cuadrados = %.3f\n", suma);`.
Estos parámetros permiten comparar exactamente las dos versiones (lista y vector) y validar corrección numérica antes de medir rendimiento.

> constexpr std::size_t N = 20'000'000;
> — `repo:datos/temarios/AC/Practicas/Code_Lab4/tarea3_1_lista.cpp`

Relacionado: [[patron-aleatorio-peor-caso-con-permutacion-fija-de-indices-s]]
