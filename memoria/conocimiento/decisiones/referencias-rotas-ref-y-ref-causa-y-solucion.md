---
tipo: "decision"
titulo: "Referencias rotas `\\ref{.}` y `\\ref{)}` — causa y solución"
temas: ["depuracion", "latex", "referencias"]
claves: ["referencia sin resolver", "Reference `.", "Reference `)", "line 794"]
proyectos: ["memoria-procesos"]
fuentes: ["salida de verificar.py y revisar_maquetacion.py"]
confianza: "propuesto"
fecha: "2026-11-23"
actualizado: "2026-11-23"
---

Temas: [[depuracion]] · [[latex]] · [[referencias]]

**Problema**: Durante edición de 04-descripcion.tex se introdujeron referencias mal formadas `\ref{.}` o `\ref{)}` (probablemente por borrado accidental de label dentro de llaves).
**Detección**: `verificar.py` reporta "Referencia sin resolver: ." y "Referencia sin resolver: )" en línea 794 (página 31 PDF).
**Solución**: Buscar en 04-descripcion.tex (y otros capítulos) patrones `\ref{.}` `\ref{)}` `\ref{ }` y corregir a label válido (ej. `\ref{fig:capas}`) o eliminar si es texto suelto. Usar `grep -n "ref{.}" chapters/04-descripcion.tex` y similar.
**Prevención**: Al editar cerca de `\ref{}`, no borrar el contenido de las llaves; usar editor con matching de llaves.

> ERROR: Memoria.log: referencia sin resolver: . / ERROR: Memoria.log: referencia sin resolver: )
> — `salida de verificar.py y revisar_maquetacion.py` (cita sin comprobar)

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
