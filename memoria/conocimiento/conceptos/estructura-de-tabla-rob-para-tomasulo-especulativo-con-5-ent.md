---
tipo: "concepto"
titulo: "Estructura de tabla ROB para Tomasulo especulativo con 5 entradas"
temas: ["ac", "pipeline", "tomasulo"]
claves: ["ROB", "Reorder Buffer", "entradas", "campos: Instrucción Estado Destino Valor"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2017.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]] · [[tomasulo]]

El ROB tiene 5 entradas (0-4). Cada entrada muestra: número de entrada, bit de ocupada (S/N), instrucción, estado (ej. Emisión, Ejecución, Escritura, Commit), destino (registro o dirección de memoria), valor (resultado calculado o dirección efectiva). Al ciclo 8 se debe volcar el estado completo. El ROB gestiona la terminación en orden (commit) para soportar especulación y recuperación ante fallos.

> Muestra el contenido del ROB al final del ciclo de reloj número 8. Nº de ¿Ocupada? Instrucción Estado Destino Valor
> — `repo:datos/temarios/AC/examenes/Junio2017.pdf`

Relacionado: [[buffer-de-reordenamiento-rob-en-tomasulo-con-especulacion-ca]] · [[simulacion-de-algoritmo-tomasulo-basico-y-especulativo-con-r]] · [[estructura-del-reorder-buffer-rob-en-tomasulo-con-especulaci]] · [[estructura-de-tabla-rob-de-4-entradas-para-volcado-en-ciclo]]
