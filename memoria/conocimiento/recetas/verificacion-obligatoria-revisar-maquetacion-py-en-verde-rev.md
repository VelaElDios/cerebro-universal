---
tipo: "receta"
titulo: "Verificación obligatoria: revisar_maquetacion.py en verde + revisión página a página"
temas: ["ci", "latex", "memoria", "scripts", "tfg"]
claves: ["revisar_maquetacion.py", "revisar_figuras.py", "PDF", "TERMINADO"]
proyectos: []
fuentes: ["../../memoria/reglas-tfg.md"]
confianza: "verificado"
fecha: "2026-11-21"
actualizado: "2026-11-21"
---

Temas: [[ci]] · [[latex]] · [[memoria]] · [[scripts]] · [[tfg]]

Checklist de entrega:
1. Ejecutar `scripts/revisar_maquetacion.py` → debe salir todo en verde (comprueba reglas medibles: portada, tablas, figuras, flotantes, etc.).
2. Ejecutar `scripts/revisar_figuras.py` → mide coordenadas reales del PDF (líneas sobre letras, cajas solapadas, palabras partidas, tamaño de letra < 7,5 pt).
3. Revisión manual página a página del PDF: legibilidad de tablas, orden lógico de secciones, sentido del contenido.
4. Solo si todo pasa, marcar la memoria como TERMINADA.

> Antes de marcar TERMINADO, el PDF se revisa página a página, y `revisar_maquetacion.py` debe salir en verde. Lo que no mide el script (que las tablas se lean bien y que el orden tenga sentido) lo comprueba el revisor.
> — `../../memoria/reglas-tfg.md`
