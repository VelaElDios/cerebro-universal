---
tipo: "receta"
titulo: "Dimensionado de BTB implícita (ancho y bits totales) para 1024 entradas y bus 24 bits"
temas: ["ac", "btb", "prediccion-saltos"]
claves: ["BTB implícita", "entradas", "bus direcciones", "ancho entrada", "bits totales"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2022.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[btb]] · [[prediccion-saltos]]

BTB implícita: indexada por PC (no almacena etiqueta completa). Ancho de cada entrada = bits de dirección destino = 24 bits. Entradas = 1024. Bits totales = 1024 × 24. Opción a: "Ancho=24, Número bits totales=1024 *24 bits". Las otras opciones son incorrectas: b usa 1024 como ancho, c multiplica 24×24, d usa 2^24 entradas.

> Indica el ancho y el número de bits totales necesarios para implementar una BTB implícita de 1024 entradas sabiendo que el bus de direcciones usa 24 bits (hay más de una solución, pero sólo una opción es correcta).
> — `repo:datos/temarios/AC/examenes/Enero2022.pdf`

Relacionado: [[btb-branch-target-buffer-fusion-de-btac-y-bits-de-prediccion]] · [[bht-branch-history-table-tabla-separada-para-bits-de-predicc]] · [[ancho-y-tamano-en-bits-de-un-btb-implicito-con-1024-entradas]] · [[implementacion-de-btb-generica-ampliacion-de-btac-con-bits-d]] · [[btb-cache-de-direcciones-destino-de-saltos-con-bits-de-predi]]
