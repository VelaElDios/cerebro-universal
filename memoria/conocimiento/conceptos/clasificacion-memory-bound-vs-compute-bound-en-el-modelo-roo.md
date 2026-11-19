---
tipo: "concepto"
titulo: "Clasificación memory-bound vs compute-bound en el modelo Roofline"
temas: ["ac", "rendimiento", "roofline"]
claves: ["memory-bound", "compute-bound", "I_KNEE", "intensidad aritmética"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab3.zip!tarea2_1_pintarRoofLin_conPunto.py"]
confianza: "propuesto"
fecha: "2026-11-19"
actualizado: "2026-11-19"
---

Temas: [[ac]] · [[rendimiento]] · [[roofline]]

Un patrón de acceso es memory-bound si su intensidad aritmética (FLOPs/Byte) está a la izquierda de la rodilla (x ≤ I_KNEE): el rendimiento real se acerca a BW_DRAM × intensidad. Es compute-bound si está a la derecha (x > I_KNEE): el rendimiento se acerca al techo de cómputo GFLOPS_MAX. El script colorea la zona memory-bound en "mistyrose" y la compute-bound en "honeydew".

> # 1. Zona Memory-Bound (Azul claro/rojo suave): donde x <= I_KNEE ... # 2. Zona Compute-Bound (Verde claro): donde x > I_KNEE
> — `repo:datos/temarios/AC/Practicas/Code_Lab3.zip!tarea2_1_pintarRoofLin_conPunto.py` (cita sin comprobar)

Relacionado: [[como-calcular-el-techo-de-computo-gflops-max-y-el-punto-de-i]]
