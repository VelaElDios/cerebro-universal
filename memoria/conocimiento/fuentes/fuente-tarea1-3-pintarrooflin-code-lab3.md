---
tipo: "fuente"
titulo: "tarea1 3 pintarRoofLin (Code_Lab3)"
temas: ["ac"]
claves: []
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab3/tarea1_3_pintarRoofLin.py"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]]

Documento aprendido: `repo:datos/temarios/AC/Practicas/Code_Lab3/tarea1_3_pintarRoofLin.py`.

## Resumen
Script de Python para generar el modelo Roofline mononúcleo de una máquina concreta. Define la frecuencia de CPU (4.9 GHz) y el ancho de banda DRAM (26.143 GB/s), calcula el tope de cómputo teórico (32 FLOPs/ciclo con AVX2+FMA) y dibuja en escala log-log la curva techo: rampa limitada por memoria (BW × intensidad aritmética) y horizontal limitada por cómputo (GFLOPS máximos).

## Lo que se sacó de él (8)
- [[calculo-de-flops-ciclo-para-avx2-con-fma]]
- [[como-generar-el-grafico-roofline-mononucleo-con-python]]
- [[como-guardar-el-grafico-roofline-como-archivo-png-en-lugar-d]]
- [[como-obtener-los-parametros-reales-de-tu-maquina-para-el-roo]]
- [[eleccion-de-eje-x-logaritmico-logspace-2-a-3-para-cubrir-4-o]]
- [[formula-del-techo-roofline-mononucleo]]
- [[interpretacion-de-regiones-memory-bound-vs-compute-bound-en]]
- [[parametros-de-ejemplo-del-script-cpu-4-9-ghz-ddr4-26-143-gb]]
