---
titulo: "Verificación de números en memoria LaTeX contra fuentes únicas"
temas: ["latex", "python", "verificacion"]
claves: ["número mayor que 20", "fuentes", "verificar.py"]
estado: "propuesta"
veces: 1
fecha: "2026-10-13"
proyectos: ["memoria-procesos"]
---

Temas: [[latex]] · [[python]] · [[verificacion]]

## Problema
El test automático `verificar.py` falla si cualquier número >20 en el texto no aparece literalmente en los archivos de fuentes (`fuentes/*.md`). Esto obliga a que cada cifra (fechas, conteos, métricas, versiones, tamaños, porcentajes) tenga su origen trazable en la documentación del proyecto.

## Solución
Antes de escribir cualquier cifra, buscarla en las fuentes. Si no está, no se escribe. Usar `\cite` o `\ref` para datos tabulados. Mantener una hoja de correspondencia número→fuente durante la redacción.

## Ejemplo
"80 pruebas" → guia.md §7 "Total 80 pruebas automatizadas"; "12/10/2026" → guia.md §7 "Último commit ... 12/10/2026"; "0,27 CU-h" → guia.md §7 tabla Neon.

Origen: [[proyectos/memoria-procesos/bitacora|memoria-procesos]]
