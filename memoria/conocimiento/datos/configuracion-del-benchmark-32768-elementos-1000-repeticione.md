---
tipo: "dato"
titulo: "Configuración del benchmark: 32768 elementos, 1000 repeticiones, valores 0-255"
temas: ["ac", "rendimiento"]
claves: ["TAMANIO", "REPETICIONES", "mt19937", "uniform_int_distribution"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab4.zip!tarea4_2_branchless.cpp"]
confianza: "verificado"
fecha: "2026-11-19"
actualizado: "2026-11-19"
---

Temas: [[ac]] · [[rendimiento]]

Parámetros fijos del experimento para reproducibilidad:
- `TAMANIO = 32768` elementos (32K enteros)
- `REPETICIONES = 1000` iteraciones del bucle externo
- Datos generados con `std::mt19937 rng(42)` (semilla fija) y `std::uniform_int_distribution<int> dist(0, 255)`
- Se crea una copia ordenada con `std::sort` para comparar mismo conjunto de datos en distinto orden
- Checksum de verificación: las 4 ejecuciones deben dar idéntico resultado (s1==s2==s3==s4)

> constexpr int TAMANIO = 32768; constexpr int REPETICIONES = 1000;
> — `repo:datos/temarios/AC/Practicas/Code_Lab4.zip!tarea4_2_branchless.cpp`

Relacionado: [[penalizacion-de-fallo-de-prediccion-de-salto-en-pipeline]]
