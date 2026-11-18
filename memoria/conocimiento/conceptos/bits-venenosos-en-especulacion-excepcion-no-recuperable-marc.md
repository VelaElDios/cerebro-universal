---
tipo: "concepto"
titulo: "Bits venenosos en especulación: excepción no recuperable marca registro destino"
temas: ["ac", "bits-venenosos", "especulacion", "excepcion", "tomasulo"]
claves: ["bits venenosos", "excepción no recuperable", "instrucción especulativa", "registro destino"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2011.pdf", "repo:datos/temarios/AC/examenes/Junio2025.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[bits-venenosos]] · [[especulacion]] · [[excepcion]] · [[tomasulo]]

En la especulación con bits venenosos (poison bits), si una instrucción especulativa causa una excepción no recuperable (p. ej., fallo de página en carga), no se atiende inmediatamente. En su lugar, se marca el registro destino con un bit venenoso. La excepción solo se lanza cuando una instrucción no especulativa intenta usar ese registro (se convierte en "no especulativa" al llegar al tope del ROB).

> En la especulación con \"bits venenosos\", ante una excepción no recuperable causada por una instrucción especulativa: a) La excepción se atiende y el programa finaliza b) El programa devuelve un valor indefinido c) Se activa el bit venenoso del registro destino de la instrucción d) Ninguna de las anteriores
> — `repo:datos/temarios/AC/examenes/Junio2011.pdf`

Relacionado: [[bits-venenosos-en-carga-especulativa-excepcion-diferida-hast]] · [[buffer-de-carga-en-tomasulo-especulativo]] · [[bits-venenosos-excepcion-no-recuperable-marca-registro-desti]] · [[comportamiento-de-bits-de-veneno-poison-bits-ante-excepcion]]

## Ampliación (2026-11-18, )
Los bits venenosos (poison bits) marcan un registro destino cuando una instrucción especulativa genera una excepción no recuperable (ej. fallo de página). La excepción no se toma inmediatamente; se propaga el bit venenoso. Si luego la instrucción se confirma (salto bien predicho), se lanza la excepción; si se descarta (mispredicción), se ignora. Opción correcta: b.
