---
tipo: "concepto"
titulo: "Punto de inflexión (knee) del modelo Roofline: I_KNEE = GFLOPS_MAX / BW_DRAM"
temas: ["ac", "cuello de botella", "rendimiento", "roofline"]
claves: ["I_KNEE", "knee point", "GFLOPS_MAX", "BW_DRAM", "memory-bound", "compute-bound"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab3/tarea2_1_pintarRoofLin_conPunto.py"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[cuello de botella]] · [[rendimiento]] · [[roofline]]

Definición y significado del punto de inflexión (knee) en el modelo Roofline:
- Fórmula: `I_KNEE = GFLOPS_MAX / BW_DRAM` (unidades: FLOPs/Byte).
- Es la intensidad aritmética a la que el techo de memoria (rampa) intersecta el techo de cómputo (horizontal).
- A la izquierda (intensidad < I_KNEE): el rendimiento está limitado por el ancho de banda de memoria → **memory-bound**.
- A la derecha (intensidad > I_KNEE): el rendimiento está limitado por la capacidad de cómputo de la CPU → **compute-bound**.
- En el ejemplo: GFLOPS_MAX = 156.8, BW_DRAM = 26.68 → I_KNEE ≈ 5.88 FLOPs/Byte.
- Los tres puntos medidos (0.37, 0.30, 0.009) caen todos en la zona memory-bound (muy a la izquierda del knee).

> I_KNEE = GFLOPS_MAX / BW_DRAM                # Punto de inflexión (FLOPs/Byte)
> — `repo:datos/temarios/AC/Practicas/Code_Lab3/tarea2_1_pintarRoofLin_conPunto.py`

Relacionado: [[punto-de-inflexion-knee-del-modelo-roofline-mononucleo]] · [[punto-de-inflexion-ridge-point-en-el-modelo-roofline]] · [[interpretacion-de-regiones-memory-bound-vs-compute-bound-en]]
