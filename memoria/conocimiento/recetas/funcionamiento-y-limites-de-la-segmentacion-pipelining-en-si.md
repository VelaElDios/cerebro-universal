---
tipo: "receta"
titulo: "Funcionamiento y límites de la segmentación (pipelining) en SISD"
temas: ["ac", "ciclo-máquina", "ilp", "latencia", "pipelining", "segmentación", "throughput"]
claves: ["segmentación", "pipeline", "IF", "ID", "EX", "MEM", "WB", "etapa más lenta", "ciclo máquina", "latencia", "productividad"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema1-Introduccion/Tema1 2026-27.pdf (trozo 3 de 5)"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[ciclo-máquina]] · [[ilp]] · [[latencia]] · [[pipelining]] · [[segmentación]] · [[throughput]]

Principios clave del pipelining:
- Divide la ejecución en etapas (ej. IF=Instruction Fetch, ID=Instruction Decode, EX=Execute, MEM=Memory Access, WB=Write Back).
- Instrucciones consecutivas ocupan etapas distintas simultáneamente → se solapan.
- **Latencia** por instrucción no baja (sigue tardando N ciclos en completar una), pero **throughput** (productividad) sube: idealmente una instrucción termina cada ciclo.
- **Frecuencia de reloj** limitada por la etapa más lenta (critical path).
- Transparente para el programador (arquitectura, no ISA).
- Peligros (hazards): estructurales, de datos, de control → requieren forwarding, stalls, predicción de saltos.

> La segmentación consiste en solapar la ejecución de instrucciones de forma que utilicen recursos distintos  el cauce de ejecución está dividido en varias etapas o segmentos  no se disminuye la latencia de una tarea, sino que se aumenta la productividad  la segmentación está limitada por la etapa más lenta que determina el ciclo máquina  la segmentación no es visible al programador
> — `repo:datos/temarios/AC/Tema1-Introduccion/Tema1 2026-27.pdf (trozo 3 de 5)`
