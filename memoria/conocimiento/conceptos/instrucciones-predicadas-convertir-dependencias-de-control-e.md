---
tipo: "concepto"
titulo: "Instrucciones predicadas: convertir dependencias de control en dependencias de datos"
temas: ["ac", "epic", "ia64", "instrucciones-predicadas", "prediccion-saltos"]
claves: ["instrucciones predicadas", "registros predicados", "predicado", "dependencia control", "dependencia datos", "IA64", "EPIC", "compilador"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[epic]] · [[ia64]] · [[instrucciones-predicadas]] · [[prediccion-saltos]]

Mecanismo para eliminar saltos condicionales:
- **Registros predicados**: registros de 1 bit que almacenan el resultado de una comparación (p.ej., `p4 = (r1 == r2)`).
- **Instrucciones predicadas**: llevan un registro predicado como operando adicional (`<p4> ADD R3, R4, R5`).
- **Semántica** (dos variantes):
  1. *Ejecución condicional real*: la instrucción solo se ejecuta si el predicado es verdadero.
  2. *Ejecución con escritura condicional (IA64/EPIC)*: la instrucción se ejecuta siempre, pero solo escribe en el banco de registros si el predicado es verdadero; si es falso, el resultado se descarta.
- **Flujo**: las instrucciones predicadas pasan por fetch, decode, issue normalmente; la predicción de saltos deja de ser necesaria para ese flujo de control.
- **Requisito ISA**: el conjunto de instrucciones debe soportar predicados y registros predicados.

> Objetivo: eliminar saltos, convirtiendo dependencias de control en dependencias de datos Requisitos: instrucciones predicadas o condicionales y registros predicados Cada registro predicado de un bit puede ser escrito después de comprobar una condición Las instrucciones predicadas usan un registro predicado como entrada adicional Las instrucciones predicadas se buscan, decodifican y emiten normalmente Dependiendo de la arquitectura del procesador: • una instrucción predicada se ejecuta sólo si el predicado es cierto • se puede ejecutar pero no se escribe en el banco de registros si el predicado es falso (arquitectura IA64)
> — `repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4.pdf` (cita sin comprobar)

Relacionado: [[arquitectura-epic-ia64-y-procesadores-itanium]] · [[instrucciones-predicadas-eliminan-saltos-y-prediccion-pregun]] · [[salto-retardado-y-instrucciones-predicadas-como-alternativas]] · [[ventajas-e-inconvenientes-de-las-instrucciones-predicadas]]
