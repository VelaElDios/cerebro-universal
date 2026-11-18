---
tipo: "dato"
titulo: "Parámetros fijos del experimento: 20 millones de lecturas, N múltiplo de 4, Ubuntu Linux, GCC/Clang"
temas: ["ac", "experimentacion", "parametros"]
claves: ["20 millones", "N múltiplo de 4", "Ubuntu", "GCC", "Clang", "perf", "hyperfine", "Campus Virtual Code-Lab3 and Lab4"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Practica4.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[experimentacion]] · [[parametros]]

Constantes del laboratorio para reproducibilidad:
- Dataset: 20 millones de elementos (lecturas de sensor).
- N múltiplo de 4 (requisito para desenrollado 4× en tarea 4.1).
- Entorno: Ubuntu Linux (arranque dual en PCs del lab), GCC o Clang.
- Herramientas: `perf` (linux-tools-common), `hyperfine` (Rust benchmarking).
- Fuentes: ZIP "Code-Lab3 and Lab4" en Campus Virtual, cada fichero con cabecera explicativa y marcadores `TODO`.
- Compilación base: `g++ -O1` para tareas ILP/branchless.

> El código base provisto en tarea3_1_lista.cpp realiza el procesamiento de 20 millones de lecturas de un sensor utilizando una lista doblemente enlazada (std::list).
> — `repo:datos/temarios/AC/Practicas/Practica4.pdf`

Relacionado: [[calentamiento-warm-up-para-poblar-tlb-y-evitar-page-faults]] · [[patron-temporal-localidad-temporal-maxima-reutilizando-un-bl]] · [[parametros-del-experimento-lista-vs-vector-n-20m-media-50-0f]] · [[parametros-fijos-del-experimento-aos-soa-tarea-3-2]] · [[parametros-fijos-del-experimento-ilp-n-100m-tipo-double-valo]]
