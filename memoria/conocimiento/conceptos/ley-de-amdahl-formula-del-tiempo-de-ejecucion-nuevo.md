---
tipo: "concepto"
titulo: "Ley de Amdahl: fórmula del tiempo de ejecución nuevo"
temas: ["ac", "rendimiento"]
claves: ["Ley de Amdahl", "tiempo de ejecución nuevo", "fracción no mejorada", "fracción mejorada"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema1-Introduccion/Tema1 2026-27.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[rendimiento]]

La Ley de Amdahl establece que el tiempo de ejecución tras una mejora es la suma del tiempo de la parte no mejorada (que permanece igual) y el tiempo de la parte mejorada (que se reduce según el factor de aceleración). La fórmula presentada en las diapositivas es: tiempo_nuevo = tiempo_fracción_no_mejorada + tiempo_fracción_mejorada. Para aplicarla, se expresa el tiempo original como T = T_no_mej + T_mej, y el nuevo tiempo T' = T_no_mej + T_mej / speedup_mejora. El speedup global es T / T'.

> tiempo de ejecución nuevo = tiempo de ejecuciónfracción no mejorada + tiempo de ejecuciónfracción mejorada
> — `repo:datos/temarios/AC/Tema1-Introduccion/Tema1 2026-27.pdf`

Relacionado: [[definicion-de-speedup-como-razon-de-tiempos-de-ejecucion]]
