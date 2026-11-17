---
tipo: "fuente"
titulo: "tarea3 1 lista (Code_Lab4)"
temas: ["ac"]
claves: []
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab4/tarea3_1_lista.cpp"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]]

Documento aprendido: `repo:datos/temarios/AC/Practicas/Code_Lab4/tarea3_1_lista.cpp`.

## Resumen
Este trozo es el código base ineficiente de la Tarea 3.1 de Arquitectura de Computadores (Prácticas 3 y 4). Usa `std::list` para almacenar 20 millones de lecturas de sensor, las normaliza en un primer bucle y acumula la suma de cuadrados en un segundo bucle. El comentario explica los problemas: *pointer chasing* por nodos dispersos en heap, una asignación dinámica por `push_back`, y pérdida de localidad temporal al recorrer dos veces los datos. Incluye instrucciones para crear una versión optimizada con `std::vector`, `.reserve(N)` y fusión de bucles, y cómo compilar y medir con `hyperfine` y

## Lo que se sacó de él (6)
- [[como-compilar-y-medir-lista-vs-vector-con-g-o2-hyperfine-y-p]]
- [[como-fusionar-dos-bucles-en-uno-solo-para-aprovechar-localid]]
- [[como-transformar-std-list-a-std-vector-con-reserva-previa-pa]]
- [[parametros-del-experimento-lista-vs-vector-n-20m-media-50-0f]]
- [[pointer-chasing-en-std-list-vs-acceso-contiguo-en-std-vector]]
- [[por-que-fusionar-bucles-de-normalizacion-y-suma-de-cuadrados]]
