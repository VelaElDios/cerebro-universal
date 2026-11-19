---
tipo: "dato"
titulo: "Parámetros fijos de la práctica ILP: N=100M elementos, vector de 1.0f, múltiplo de 4"
temas: ["ac", "datos", "parametros", "verificacion"]
claves: ["N=100000000", "100 millones", "vector double", "1.0f", "multiple of 4"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab4.zip!tarea4_1_ilp.cpp"]
confianza: "verificado"
fecha: "2026-11-19"
actualizado: "2026-11-19"
---

Temas: [[ac]] · [[datos]] · [[parametros]] · [[verificacion]]

Valores constantes del experimento para reproducibilidad:
- N = 100'000'000 (100 millones) elementos.
- Vector `v` de tipo `double` inicializado con `1.0f` (todos los elementos valen 1.0).
- N es múltiplo de 4 → el desenrollado de 4 vías no requiere epílogo de limpieza (cleanup loop).
- Resultado esperado: `sumA == 100'000'000.0` (exactamente N, ya que cada elemento suma 1.0).
- Tipo `double` para acumuladores (precisión suficiente para suma exacta de 1e8 unos).

> const int N = 100'000'000; // 100 millones de elementos (múltiplo de 4)
> — `repo:datos/temarios/AC/Practicas/Code_Lab4.zip!tarea4_1_ilp.cpp`

Relacionado: [[optimizacion-ilp-mediante-desenrollado-de-4-vias-con-acumula]]
