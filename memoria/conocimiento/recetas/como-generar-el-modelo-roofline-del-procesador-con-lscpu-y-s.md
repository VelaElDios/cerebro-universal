---
tipo: "receta"
titulo: "Cómo generar el modelo Roofline del procesador con lscpu y STREAM (Tarea 1.3)"
temas: ["ac", "lscpu", "rendimiento", "roofline", "stream"]
claves: ["techo de cómputo", "techo de RAM", "punto de inflexión", "GFLOPs/s", "GB/s", "tarea1.3_pintarRoofLin.py"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Practica3.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[lscpu]] · [[rendimiento]] · [[roofline]] · [[stream]]

1) `lscpu` → anotar "CPU max MHz" (convertir a GHz). 2) Descargar y compilar STREAM: `wget https://www.cs.virginia.edu/stream/FTP/Code/stream.c && gcc -O3 -march=native stream.c -o stream && ./stream`. Tomar valor *Best Rate MB/s* de la fila *Triad*, dividir entre 1000 → BW en GB/s. 3) Editar `tarea1.3_pintarRoofLin.py` con frecuencia (GHz) y BW (GB/s). 4) Ejecutar `python3 tarea1.3_pintarRoofLin.py` para generar gráfica. 5) Leer de la gráfica: techo de cómputo (GFLOPs/s) y punto de inflexión (intensidad aritmética donde se cruzan ambas rectas).

> 1. Cálculo del techo de cómputo mono-núcleo: Ejecuta el comando lscpu y obtén la frecuencia máxima en GHz. 2. Cálculo del techo de RAM: Medimos la velocidad de la memoria con el benchmark estándar STREAM para ello ejecuta el siguiente comando y busca al final de la salida la fila Triad, tomando el valor de la columna Best Rate MB/s y divídelo entre 1000 para obtener los GB/s reales.
> — `repo:datos/temarios/AC/Practicas/Practica3.pdf`

Relacionado: [[formula-del-techo-roofline-mononucleo]] · [[interpretacion-de-regiones-memory-bound-vs-compute-bound-en]] · [[calculo-de-flops-ciclo-para-avx2-con-fma]] · [[como-obtener-parametros-de-hardware-para-el-modelo-roofline]] · [[como-obtener-los-parametros-reales-de-tu-maquina-para-el-roo]] · [[como-generar-el-grafico-roofline-mononucleo-con-python]]
