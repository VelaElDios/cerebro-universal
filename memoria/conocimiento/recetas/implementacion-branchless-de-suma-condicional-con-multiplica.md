---
tipo: "receta"
titulo: "Implementación branchless de suma condicional con multiplicación"
temas: ["ac", "pipeline", "rendimiento"]
claves: ["branchless", "conditional arithmetic", "multiplication trick", "x >= 128"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab4.zip!tarea4_2_branchless.cpp"]
confianza: "propuesto"
fecha: "2026-11-19"
actualizado: "2026-11-19"
---

Temas: [[ac]] · [[pipeline]] · [[rendimiento]]

Para eliminar un salto condicional `if (x >= 128) suma += x;` se usa aritmética condicional:
```cpp
suma += x * (x >= 128);
```
En C/C++, la expresión `(x >= 128)` evalúa a `1` (true) o `0` (false). Multiplicando `x` por este resultado se suma `x` cuando la condición es verdadera y `0` cuando es falsa, sin ninguna instrucción de salto. Esto hace que el tiempo de ejecución sea independiente del orden de los datos y evita fallos de predicción.

> Pista: En C, una comparación devuelve 1 (verdadero) o 0 (falso). Multiplica 'x' directamente por el resultado de evaluar (x >= 128).
> — `repo:datos/temarios/AC/Practicas/Code_Lab4.zip!tarea4_2_branchless.cpp` (cita sin comprobar)

Relacionado: [[penalizacion-de-fallo-de-prediccion-de-salto-en-pipeline]]
