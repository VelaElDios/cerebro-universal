---
tipo: "decision"
titulo: "Uso de TODO1 y TODO2 como puntos de personalización obligatorios para el alumno"
temas: ["ac", "metodologia", "practica", "roofline"]
claves: ["TODO1", "TODO2", "FRECUENCIA_GHZ", "BW_DRAM", "intensidades", "rendimientos"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab3.zip!tarea2_1_pintarRoofLin_conPunto.py"]
confianza: "propuesto"
fecha: "2026-11-19"
actualizado: "2026-11-19"
---

Temas: [[ac]] · [[metodologia]] · [[practica]] · [[roofline]]

El script está diseñado como plantilla educativa con dos bloques de edición obligatoria:
- TODO1: hardware del alumno → frecuencia CPU (lscpu) y BW DRAM (benchmark STREAM).
- TODO2: resultados experimentales del alumno → intensidades y rendimientos medidos para los tres patrones (temporal, secuencial, aleatorio) según el Anexo B de la práctica.
Esto fuerza al alumno a caracterizar su máquina y medir sus kernels antes de visualizar el Roofline.

> # TODO1 ... FRECUENCIA_GHZ = 4.9     # Tu frecuencia en GHz (de lscpu) BW_DRAM = 26.68          # Tus GB/s de la RAM (de STREAM) # TODO2 ... intensidades = [0.3661, 0.3006, 0.00885]   # Valores X recalculados [Temporal, Secuencial, Aleatorio] rendimientos = [1.1940, 1.2000, 0.0825]    # Valores Y recalculados [Temporal, Secuencial, Aleatorio]
> — `repo:datos/temarios/AC/Practicas/Code_Lab3.zip!tarea2_1_pintarRoofLin_conPunto.py` (cita sin comprobar)

Relacionado: [[valores-de-ejemplo-de-intensidad-y-rendimiento-para-tres-pat]]
