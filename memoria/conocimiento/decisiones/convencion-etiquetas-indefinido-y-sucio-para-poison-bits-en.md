---
tipo: "decision"
titulo: "Convención etiquetas \"indefinido\" y \"sucio\" para poison bits en examen AC"
temas: ["ac", "arquitectura", "examenes", "poison-bits"]
claves: ["poison bit", "indefinido", "sucio", "convención examen", "registros"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2014.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[arquitectura]] · [[examenes]] · [[poison-bits]]

En el apartado (c) con poison bits, el examen establece convención explícita para la solución: "indefinido" = valor de registro indefinido (no se pudo calcular por excepción en instrucción especulativa), "sucio" = registro tiene poison bit a 1 (valor contaminado por dependencia de instrucción especulativa que falló). Esto permite distinguir entre registro que nunca se escribió (indefinido) vs registro que recibió valor de instrucción con poison bit (sucio).

> Utiliza las etiquetas "indefinido" y "sucio" para indicar cuando el valor de un registro es indefinido o tiene el poison bit a 1, respectivamente.
> — `repo:datos/temarios/AC/examenes/Enero2014.pdf`

Relacionado: [[tres-mecanismos-de-especulacion-evaluados-en-examen-ac-enero]] · [[especulacion-con-poison-bits-propagacion-y-excepcion-diferid]] · [[funcionamiento-detallado-de-bits-de-veneno-poison-bits-en-es]]
