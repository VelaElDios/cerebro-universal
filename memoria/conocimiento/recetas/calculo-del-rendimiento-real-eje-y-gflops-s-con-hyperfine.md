---
tipo: "receta"
titulo: "Cálculo del rendimiento real (eje Y: GFLOPs/s) con hyperfine"
temas: ["ac", "hyperfine", "rendimiento", "roofline"]
claves: ["GFLOPs/s", "Total_FLOPs", "tiempo ejecución", "hyperfine", "10^9"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Practica3.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[hyperfine]] · [[rendimiento]] · [[roofline]]

Rendimiento real en GFLOPs/s (eje Y del Roofline):
  Y = Total_FLOPs / (t_segundos * 1e9)
Pasos:
1. Medir tiempo de ejecución con `hyperfine` (mediana de varias corridas).
2. Calcular Total_FLOPs según la receta anterior.
3. Dividir y escalar a GFLOPs/s (10^9).
Ejemplo: si N=10^7, REPETICIONES=4 → Total_FLOPs=1.6e8; t=0.05 s → Y=3.2 GFLOPs/s.

> El rendimiento se obtiene dividiendo el número total de operaciones de punto flotante (FLOPs) ejecutadas por el algoritmo entre su tiempo de ejecución en segundos. Y = Total_FLOPs / (Tiempo ejecución en segundos (hyperfine) * 10^9)
> — `repo:datos/temarios/AC/Practicas/Practica3.pdf` (cita sin comprobar)

Relacionado: [[mapeo-de-patrones-de-acceso-en-grafico-roofline-gflops-s-y-f]] · [[definicion-de-mflops-millones-de-operaciones-de-punto-flotan]] · [[formula-del-techo-roofline-mononucleo]]
