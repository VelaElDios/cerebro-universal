---
tipo: "concepto"
titulo: "BHT (Branch History Table): tabla separada para bits de predicción"
temas: ["ac", "arquitectura", "bht", "prediccion-saltos"]
claves: ["BHT", "Branch History Table", "bits predicción", "PowerPC 604", "R10000", "PowerPC 620", "Alpha 21164A"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[arquitectura]] · [[bht]] · [[prediccion-saltos]]

La BHT es una tabla independiente de la BTAC que guarda solo bits de predicción (historial). La BTAC guarda direcciones destino de saltos tomados. Acceso a BHT: típicamente usando bits menos significativos de la dirección del salto (sin tags, menor coste, pero hay compartición de entradas que degrada rendimiento) o asociativa por conjuntos (mayor coste, para mismo hardware peor comportamiento). Ventaja: puede predecir saltos que no están en la BTAC (BHT suele tener más entradas). Inconveniente: duplica hardware (dos tablas asociativas). Ejemplos: PowerPC 604 (512 entradas × 2 bits), R10000 (512×2), PowerPC 620 (2K×2), Alpha 21164A (2K×2).

> La BHT almacena los bits de predicción de todas las instrucciones de salto condicional. La BTAC almacena la dirección destino de los últimos saltos tomados. Usa una tabla especial, distinta de la BTAC, para guardar los bits de predicción. PowerPC 604 (1994) 512 x 2 bits R10000 (1994) 512 x 2 bits PowerPC 620 (1995) 2K x 2 bits Alpha 21164A (1996) 2K x 2 bits
> — `repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4.pdf` (cita sin comprobar)

Relacionado: [[la-bht-almacena-los-bits-de-prediccion-de-todas-las-instrucc]] · [[estructuras-hardware-para-prediccion-de-saltos-btac-bht-btb]] · [[implementacion-bht-para-predictor-de-2-bits-4k-entradas-80-9]]
