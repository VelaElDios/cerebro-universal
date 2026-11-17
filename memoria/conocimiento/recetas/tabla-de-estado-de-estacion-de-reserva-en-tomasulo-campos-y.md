---
tipo: "receta"
titulo: "Tabla de estado de estación de reserva en Tomasulo: campos y lectura"
temas: ["ac", "estacion-reserva", "simulacion", "tomasulo"]
claves: ["Ocupada Op Vj Vk Qj Qk", "nombre estación", "suma1 suma2 suma3"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3_Prob.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[estacion-reserva]] · [[simulacion]] · [[tomasulo]]

Estructura de fila que piden rellenar (Ej. 16c):
| Nombre | Ocupada (S/N) | Op | Vj | Vk | Qj | Qk |
|--------|---------------|----|----|----|----|----|
| Suma1  |               |    |    |    |    |    |
| Suma2  |               |    |    |    |    |    |
| Suma3  |               |    |    |    |    |    |

Significado en el ciclo de **emisión** de `ADD.D F6, F4, F6`:
- **Ocupada**: S (sí, porque acaba de emitirse en una de las 3).
- **Op**: ADD.D (o ADD).
- **Vj / Vk**: Valor del operando *si ya está disponible* en registros (Qj=Qk=0). Si no, 0 o vacío.
- **Qj / Qk**: Etiqueta de la estación de reserva (o buffer de carga) que *producirá* el operando. Ej: si F4 viene de un MUL.D en Mult1 → Qj=Mult1. Si F6 viene de un ADD.D previo en Suma2 → Qk=Suma2. Si el registro no tiene Qi (ya valor listo) → 0.
- **Nombre**: Suma1, Suma2 o Suma3 (la que se asigna libre en ese ciclo).
Clave: En el ciclo de emisión *aún no se han leído operandos* (eso pasa en siguiente ciclo si Q=0). Por tanto Vj/Vk suelen estar vacíos y Qj/Qk reflejan el *Register Result Status* (Qi) en ese instante.

> Muestra el contenido de la estación de reserva del sumador/restador en el ciclo en el que se emite la instrucción ADD.D F6, F4, F6 en el apartado b
> — `repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3_Prob.pdf`

Relacionado: [[algoritmo-de-tomasulo-reglas-de-simulacion-para-ejercicios-d]] · [[contenido-de-una-estacion-de-reserva-en-tomasulo]]
