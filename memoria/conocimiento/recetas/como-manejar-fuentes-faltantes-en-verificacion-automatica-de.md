---
tipo: "receta"
titulo: "Cómo manejar fuentes faltantes en verificación automática de números"
temas: ["fuentes", "memoria-procesos", "verificacion", "verificar.py"]
claves: ["verificar.py", "fuentes faltantes", "números no verificados", "placeholders"]
proyectos: ["memoria-procesos"]
fuentes: ["memoria/reglas-tfg.md y experiencia del proyecto"]
confianza: "propuesto"
fecha: "2026-11-19"
actualizado: "2026-11-19"
---

Temas: [[fuentes]] · [[memoria-procesos]] · [[verificacion]] · [[verificar.py]]

Cuando `verificar.py` falla porque faltan fuentes principales:
1. NO inventar ni redondear números. Usar placeholders visibles ("XX") en el texto LaTeX.
2. Añadir comentario en el código LaTeX: `% PENDIENTE: verificar en documentacion-tecnica.md §X.Y`
3. En la bitácora/TAREAS, marcar como CRÍTICO obtener las fuentes faltantes.
4. El constructor debe solicitar las fuentes al usuario ANTES de continuar con otras correcciones.
5. Una vez disponibles las fuentes, reemplazar TODOS los placeholders por valores exactos (contar uno a uno si hace falta: P1–P14 y P18 = 16 PBIs en burndown, no 19).
6. Volver a ejecutar `verificar.py` hasta que pase sin errores.

> Regla de oro: cada dato (cifras, fechas, nombres, versiones, URLs, números de PR, nombres de módulos) sale de las fuentes, copiado tal cual. Si algo no está en las fuentes, no se escribe.
> — `memoria/reglas-tfg.md y experiencia del proyecto` (cita sin comprobar)

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
