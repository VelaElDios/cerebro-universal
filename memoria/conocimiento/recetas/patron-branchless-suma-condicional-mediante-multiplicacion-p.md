---
tipo: "receta"
titulo: "Patrón branchless: suma condicional mediante multiplicación por booleano"
temas: ["ac", "branchless", "optimizacion"]
claves: ["branchless", "conditional-arithmetic", "x86", "pipeline", "misprediction"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab4/tarea4_2_branchless.cpp"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[branchless]] · [[optimizacion]]

Sustituir `if (x >= 128) suma += x;` por aritmética sin salto:
```cpp
suma += x * (x >= 128);   // (x >= 128) vale 1 si true, 0 si false
```
Ventajas:
- Elimina la instrucción de salto condicional → cero fallos de predicción (mispredictions).
- Tiempo de ejecución independiente del orden de los datos (ordenados vs. aleatorios).
- En x86 moderno compila a `cmp` + `setge` + `imul` + `add` (o `cmov` si el compilador lo prefiere), sin burbujas de pipeline por flush.
Desventaja: siempre ejecuta la multiplicación y la suma, aunque `x < 128`; en bucles muy cortos o con predictor perfecto, el `if` puede ser más rápido.

> Pista: En C, una comparación devuelve 1 (verdadero) o 0 (falso). Multiplica 'x' directamente por el resultado de evaluar (x >= 128).
> — `repo:datos/temarios/AC/Practicas/Code_Lab4/tarea4_2_branchless.cpp` (cita sin comprobar)

Relacionado: [[aos-vs-soa-desperdicio-de-ancho-de-banda-en-cache]] · [[formula-del-techo-roofline-mononucleo]]
