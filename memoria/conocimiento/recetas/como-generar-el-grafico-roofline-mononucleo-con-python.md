---
tipo: "receta"
titulo: "Cómo generar el gráfico Roofline mononúcleo con Python"
temas: ["ac", "arquitectura-computadores", "matplotlib", "python", "roofline"]
claves: ["tarea1_3_pintarRoofLin.py", "FRECUENCIA_GHZ", "BW_DRAM", "FLOPSperCYCLE", "GFLOPS_MAX", "np.logspace", "plt.loglog"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab3/tarea1_3_pintarRoofLin.py"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[arquitectura-computadores]] · [[matplotlib]] · [[python]] · [[roofline]]

Pasos para reproducir el gráfico Roofline:
1. Editar los dos parámetros de la máquina: FRECUENCIA_GHZ (GHz, de `lscpu`) y BW_DRAM (GB/s, de benchmark STREAM).
2. El script usa FLOPSperCYCLE = 32 para AVX2+FMA (8 floats × 2 ops FMA × 2 unidades FMA por núcleo).
3. Calcula GFLOPS_MAX = FRECUENCIA_GHZ × FLOPSperCYCLE.
4. Genera eje X con `np.logspace(-2, 3, 1000)` (intensidad aritmética 0.01–1000 FLOPs/Byte).
5. Dibuja la curva techo con `plt.loglog(x, np.minimum(BW_DRAM * x, GFLOPS_MAX))` y la horizontal del tope de cómputo con `plt.axhline`.
6. Ejecutar: `python3 tarea1_3_pintarRoofLin.py`. Opcional: descomentar `plt.savefig` para guardar imagen.

> Genera una gráfica del modelo Roofline mononúcleo de tu máquina.
> — `repo:datos/temarios/AC/Practicas/Code_Lab3/tarea1_3_pintarRoofLin.py`

Relacionado: [[como-trazar-el-modelo-roofline-con-matplotlib-en-escala-log]] · [[parametros-de-ejemplo-del-script-cpu-4-9-ghz-ddr4-26-143-gb]] · [[como-guardar-el-grafico-roofline-como-archivo-png-en-lugar-d]]
