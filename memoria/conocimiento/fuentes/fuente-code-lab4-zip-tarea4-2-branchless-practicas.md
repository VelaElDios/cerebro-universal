---
tipo: "fuente"
titulo: "Code Lab4.zip!tarea4 2 branchless (Practicas)"
temas: ["ac"]
claves: []
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab4.zip!tarea4_2_branchless.cpp"]
confianza: "verificado"
fecha: "2026-11-19"
actualizado: "2026-11-19"
---

Temas: [[ac]]

Documento aprendido: `repo:datos/temarios/AC/Practicas/Code_Lab4.zip!tarea4_2_branchless.cpp`.

## Resumen
Este trozo es un laboratorio de Arquitectura de Computadores (Tarea 4.2) que evalúa el impacto de la predicción de saltos en el rendimiento. Compara dos versiones de suma condicional: una con salto (`if (x >= 128)`) y otra branchless usando aritmética condicional. El código incluye atributos GCC para forzar un salto real y evitar optimizaciones vectoriales, y un benchmark que mide tiempos en datos ordenados vs desordenados demostrando la penalización de fallos de predicción (~10-20 ciclos).

## Lo que se sacó de él (6)
- [[atributos-gcc-para-forzar-salto-real-y-desactivar-optimizaci]]
- [[configuracion-del-benchmark-32768-elementos-1000-repeticione]]
- [[efecto-del-orden-de-datos-en-prediccion-de-saltos-condiciona]]
- [[implementacion-branchless-de-suma-condicional-con-multiplica]]
- [[penalizacion-de-fallo-de-prediccion-de-salto-en-pipeline]]
- [[trade-offs-de-programacion-branchless-vs-condicional]]
