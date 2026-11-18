---
tipo: "concepto"
titulo: "Acción del procesador ante fallo de predicción de salto"
temas: ["ac", "especulacion", "fallo-prediccion", "prediccion-saltos"]
claves: ["branch misprediction", "speculative instructions", "flush", "pipeline restart"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2025.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[especulacion]] · [[fallo-prediccion]] · [[prediccion-saltos]]

Cuando falla la predicción: se descartan las instrucciones especulativas ejecutadas por el camino erróneo (flush pipeline), se reinicia la captura en la dirección correcta. No se reinicia todo el procesador, no se ejecutan ambas direcciones, no se para el reloj. Respuesta: b. Speculative instructions are discarded.

> What happens when branch prediction fails?
> — `repo:datos/temarios/AC/examenes/June2025.pdf`

Relacionado: [[bits-venenosos-en-carga-especulativa-excepcion-diferida-hast]]
