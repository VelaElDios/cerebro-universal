---
tipo: "concepto"
titulo: "Saltos retardados (delayed branches) en planificación estática"
temas: ["ac", "control-hardware", "delayed-branch", "planificacion-estatica", "salto-retardado"]
claves: ["saltos retardados", "delayed branch", "retardo un ciclo", "ranura retardo", "compilador"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[control-hardware]] · [[delayed-branch]] · [[planificacion-estatica]] · [[salto-retardado]]

**Saltos retardados (delayed branches)**: Técnica de planificación estática donde la arquitectura define que la instrucción inmediatamente posterior a un salto (la "ranura de retardo" o *delay slot*) se ejecuta **siempre**, independientemente de si el salto se toma o no.
- En el procesador de referencia: "Los saltos tienen un retardo de un ciclo".
- El compilador debe rellenar esa ranura con una instrucción útil (de la iteración anterior, del código antes del salto, o NOP si no hay nada).
- En el ejemplo de desenrollamiento 4x aparece la anotación "Salto retardado" tras el `bne`, indicando que la instrucción siguiente (en el código original, la primera del bucle) se ejecuta antes de que el salto surta efecto.
- Simplifica el control hardware (no hace falta predicción ni flush de pipeline en saltos tomados) pero exige trabajo del compilador y complica la depuración/excepciones.

> 3.1.4 Saltos retardados • Los saltos tienen un retardo de un ciclo
> — `repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf` (cita sin comprobar)
