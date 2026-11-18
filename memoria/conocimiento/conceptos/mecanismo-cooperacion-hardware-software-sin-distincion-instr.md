---
tipo: "concepto"
titulo: "Mecanismo cooperación hardware/software sin distinción instrucciones especulativas"
temas: ["ac", "arquitectura", "hardware-software", "prediccion-saltos"]
claves: ["cooperación HW/SW", "rutina excepción", "valor indefinido", "no termina programa"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2014.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[arquitectura]] · [[hardware-software]] · [[prediccion-saltos]]

Este mecanismo trata igual las excepciones en instrucciones normales y especulativas. Cuando cualquier instrucción (incluyendo LW* especulativas) lanza excepción, la rutina de servicio: (1) devuelve un valor "indefinido" en el registro destino, (2) NO termina el programa, (3) continúa la ejecución. Esto permite que el programa siga ejecutándose aunque las cargas especulativas fallen, pero propaga valores indefinidos a instrucciones dependientes.

> Mecanismo de cooperación hardware/software sin distinción entre instrucciones normales e instrucciones especulativas. Es decir, la rutina de servicio de la excepción siempre devuelve un valor indefinido y no termina el programa.
> — `repo:datos/temarios/AC/examenes/Enero2014.pdf`

Relacionado: [[tres-mecanismos-de-especulacion-evaluados-en-examen-ac-enero]]
