---
tipo: "concepto"
titulo: "Convención de nomenclatura en tablas de Tomasulo del temario"
temas: ["ac", "notacion", "tomasulo"]
claves: ["Qi", "Vj", "Vk", "Qj", "Qk", "M(34+x2)", "M(45+x3)", "M*f4", "M()-M()"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[notacion]] · [[tomasulo]]

Notación usada en las diapositivas para los campos de las estaciones de reserva y registro de estado:
- **Qi** (en fila de registros): estación de reserva que escribirá el registro (ej. "Mult 1", "Mult 2", "M*f4/M").
- **Vj, Vk**: valor real del operando ya disponible. Ejemplos: "M(45+x3)" = valor de memoria en dirección 45+x3; "R(f4)" = valor del registro f4; "M*f4" = resultado de multiplicación por f4.
- **Qj, Qk**: etiqueta de la estación de reserva que proveerá el operando (ej. "Mult 1").
- **Op**: operación en la estación (Mult, Div, Suma).
- Expresiones compuestas como "(M-M)+M()" o "M()-M()" aparecen en la fila Qi de registros intermedios (f8, f10) indicando cadenas de dependencias aún no resueltas simbólicamente.
- Los buffers de carga se nombran "Carga 1/2/3", los de almacenamiento "Almac 1/2/3", las unidades "Suma 1/2/3", "Mult 1/2".

> Qi Mult 1 M(45+x3) (M-M)+M() M()-M() Mult 2
> — `repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf`

Relacionado: [[algoritmo-tomasulo-origen-y-objetivo-cpi1]] · [[buffers-de-carga-y-almacenamiento-en-tomasulo]]
