---
tipo: "receta"
titulo: "Simulación Tomasulo especulativa con ROB de 4 entradas (examen Enero 2017)"
temas: ["ac", "especulacion", "rob", "tomasulo"]
claves: ["Tomasulo especulativo", "ROB", "reorder buffer", "commit", "terminación", "MIPS64"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2017.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[especulacion]] · [[rob]] · [[tomasulo]]

Variante del problema anterior usando Tomasulo con especulación y ROB (Reorder Buffer) de 4 entradas.
- Mismas latencias y restricciones de bus/recurso que la versión básica.
- El ROB gestiona la terminación (commit) en orden de programa; una instrucción termina (Terminación) cuando llega a cabeza de ROB y su resultado está listo.
- Tabla ROB al final del ciclo 9: 4 entradas (0-3) con campos: ¿Ocupada? (S/N), Instrucción, Estado, Destino, Valor.
- Código idéntico (6 instrucciones). Hay que rellenar tabla de Emisión, Ejecución, Escritura resultado, Terminación y el estado del ROB en ciclo 9.

> Resuelve el mismo ejercicio, pero empleando la versión especulativa del método de Tomasulo y un ROB de 4 entradas inicialmente vacío.
> — `repo:datos/temarios/AC/examenes/Enero2017.pdf`

Relacionado: [[configuracion-tomasulo-con-especulacion-para-examen-enero-20]] · [[especulacion-con-poison-bits-propagacion-y-excepcion-diferid]] · [[buffers-de-carga-y-almacenamiento-en-tomasulo]]
