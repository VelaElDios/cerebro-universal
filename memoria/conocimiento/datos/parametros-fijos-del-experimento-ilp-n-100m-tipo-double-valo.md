---
tipo: "dato"
titulo: "Parámetros fijos del experimento ILP: N=100M, tipo double, valor 1.0f"
temas: ["ac", "experimento", "parametros"]
claves: ["N=100000000", "double", "1.0f", "multiple of 4"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab4/tarea4_1_ilp.cpp"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[experimento]] · [[parametros]]

**Parámetros fijos del experimento** (definidos en el código base):
- **N = 100'000'000** elementos (100 millones, múltiplo de 4 para que el unrolling factor 4 encaje exacto)
- **Tipo de datos**: `double` (64 bits, 8 bytes cada uno)
- **Valor inicial**: `1.0f` (se promociona a double 1.0)
- **Tamaño total vector**: 100M × 8 bytes = **800 MB** (excede L3 caché típica → memory bound parcial)
- **Resultado esperado**: suma = 100'000'000.0 (exactamente N)

**Implicaciones**:
- Vector no cabe en caché → accesos a memoria principal dominan
- Patrón de acceso **secuencial** → prefetcher hardware funciona bien
- Ancho de banda memoria puede ser cuello de botella antes que ILP
- Repetición única (no hay bucle externo de repeticiones) → medición incluye cold start

> const int N = 100'000'000; // 100 millones de elementos (múltiplo de 4) std::vector<double> v(N, 1.0f);
> — `repo:datos/temarios/AC/Practicas/Code_Lab4/tarea4_1_ilp.cpp`

Relacionado: [[patron-secuencial-localidad-espacial-y-prefetcher-hardware]]
