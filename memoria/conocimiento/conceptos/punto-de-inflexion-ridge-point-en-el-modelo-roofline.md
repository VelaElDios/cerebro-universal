---
tipo: "concepto"
titulo: "Punto de inflexión (ridge point) en el modelo Roofline"
temas: ["ac", "rendimiento", "roofline"]
claves: ["ridge point", "punto de inflexión", "intensidad aritmética", "techo de cómputo", "ancho de banda memoria"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Practica3.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[rendimiento]] · [[roofline]]

El ridge point (punto de inflexión) marca la intensidad aritmética donde el límite de ancho de banda de memoria (pendiente) se encuentra con el techo de cómputo máximo (meseta horizontal). A la izquierda del ridge point el kernel es memory-bound; a la derecha, compute-bound. Se calcula como:
  Ridge Point (FLOPs/Byte) = Techo de Cómputo Máximo (GFLOPs/s) / Ancho de Banda de Memoria Máximo (GB/s)

> El punto de inflexión es el valor de Intensidad Aritmética (𝐼𝐼𝑘𝑘𝑘𝑘𝑘𝑘𝑘𝑘 ) en el Eje X donde la pendiente del ancho de banda de la memoria se cruza con la meseta horizontal del techo de la CPU.
> — `repo:datos/temarios/AC/Practicas/Practica3.pdf`

Relacionado: [[formula-del-techo-roofline-mononucleo]] · [[interpretacion-de-regiones-memory-bound-vs-compute-bound-en]]
