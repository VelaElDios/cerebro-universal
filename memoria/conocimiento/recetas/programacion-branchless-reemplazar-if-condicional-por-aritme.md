---
tipo: "receta"
titulo: "Programación branchless: reemplazar if condicional por aritmética con máscara 0/1"
temas: ["ac", "branchless", "optimizacion", "simd"]
claves: ["branchless programming", "branchless", "mascara", "multiplicacion", "vectorizacion SIMD", "tarea4_2_branchless.cpp", "sumar_sin_salto"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Practica4.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[branchless]] · [[optimizacion]] · [[simd]]

Transformar:
```cpp
// Con salto (branchy)
if (data[i] >= 128) sum += data[i];
```
en versión branchless:
```cpp
// Sin salto: la comparación produce 0 (false) o 1 (true)
sum += data[i] * (data[i] >= 128);
// o con máscara bit a bit (para enteros)
sum += data[i] & -(data[i] >= 128);
```
Ventajas: 1) Elimina fallos de predictor → rendimiento constante independientemente del orden de datos. 2) Permite auto-vectorización SIMD del compilador (no hay control flow que lo impida). 3) Latencia predecible. Compilar con `-O1` o superior para que el compilador genere instrucciones CMOV o aritmética sin saltos.

> Como la condición `(data[i] >= 128)` devuelve `0` o `1`, podemos utilizar ese resultado directamente en una operación aritmética (multiplicando o enmascarando) en lugar de saltar.
> — `repo:datos/temarios/AC/Practicas/Practica4.pdf`

Relacionado: [[predictor-de-saltos-por-que-datos-ordenados-vs-desordenados]] · [[calculo-de-flops-ciclo-para-avx2-con-fma]]
