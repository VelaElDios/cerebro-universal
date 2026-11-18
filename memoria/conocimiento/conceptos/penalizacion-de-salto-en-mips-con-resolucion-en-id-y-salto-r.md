---
tipo: "concepto"
titulo: "Penalización de salto en MIPS con resolución en ID y salto retardado: cero ciclos"
temas: ["ac", "mips", "pipeline", "prediccion-saltos"]
claves: ["salto", "penalización", "MIPS", "etapa ID", "salto retardado", "delayed branch"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2013.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[mips]] · [[pipeline]] · [[prediccion-saltos]]

En un pipeline MIPS clásico donde la decisión de salto se toma en la etapa ID y se utiliza salto retardado (delayed branch), la instrucción inmediatamente posterior al salto (slot de retardo) se ejecuta siempre. Si el compilador llena ese slot con una instrucción útil, no hay penalización por salto, ya que la fetch de la siguiente instrucción correcta continúa sin burbujas.

> En una implementación segmentada de MIPS en la que los saltos se resuelven completamente en la etapa ID, suponiendo que no se emplea ninguna técnica de predicción, las instrucciones de salto: a. No tienen penalización
> — `repo:datos/temarios/AC/examenes/Junio2013.pdf`

Relacionado: [[accion-del-procesador-ante-fallo-de-prediccion-de-salto]] · [[alternativas-de-deteccion-de-instruccion-de-salto-en-pipelin]] · [[penalizacion-de-salto-en-mips-resuelto-en-id-sin-prediccion]] · [[prediccion-fija-siempre-no-tomado-con-calculo-destino-en-id]] · [[penalizacion-de-salto-condicional-en-pipeline-de-5-etapas-re]]
