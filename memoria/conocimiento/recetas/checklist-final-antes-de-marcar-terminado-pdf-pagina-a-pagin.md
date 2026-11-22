---
tipo: "receta"
titulo: "Checklist final de verificación antes de marcar TERMINADO (PDF página a página + scripts en verde)"
temas: ["ci", "latex", "memoria", "revisar_maquetacion.py", "scripts", "tfg", "verificacion"]
claves: ["revisar_maquetacion.py", "verde", "PDF página a página", "revisor", "revisar_figuras.py", "PDF", "TERMINADO"]
proyectos: []
fuentes: ["../../memoria/reglas-tfg.md"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-22"
---

Temas: [[ci]] · [[latex]] · [[memoria]] · [[revisar_maquetacion.py]] · [[scripts]] · [[tfg]] · [[verificacion]]

Temas: [[ci]] · [[latex]] · [[memoria]] · [[revisar_maquetacion.py]] · [[revisar_figuras.py]] · [[scripts]] · [[tfg]] · [[verificacion]]

Proceso obligatorio antes de TERMINADO:
1. Ejecutar `scripts/revisar_maquetacion.py` → debe salir todo en verde (comprueba reglas medibles: portada, tablas, figuras, flotantes, etc.).
2. Ejecutar `scripts/revisar_figuras.py` → mide coordenadas reales del PDF (líneas sobre letras, cajas solapadas, palabras partidas, tamaño de letra < 7,5 pt).
3. Revisión manual página a página del PDF: legibilidad de tablas, orden lógico de secciones, sentido del contenido, coherencia narrativa.
4. Solo si todo pasa (scripts en verde + revisión humana), marcar la memoria como TERMINADA.

> Antes de marcar TERMINADO, el PDF se revisa página a página, y `revisar_maquetacion.py` debe salir en verde. Lo que no mide el script (que las tablas se lean bien y que el orden tenga sentido) lo comprueba el revisor.
> — `../../memoria/reglas-tfg.md`

Relacionado: [[memoria-tfg-aprobada-tras-pasar-todos-los-tests-automaticos]] · [[comprobar-la-maquetacion-de-un-tfg-automaticamente]] · [[verificacion-automatica-de-diagramas-con-scripts-revisar-fig]] · [[scripts-de-verificacion-automatica-en-el-repo]]
<<<CONTRADICCION>>
no

> Antes de marcar TERMINADO, el PDF se revisa página a página, y `revisar_maquetacion.py` debe salir en verde. Lo que no mide el script (que las tablas se lean bien y que el orden tenga sentido) lo comprueba el revisor.
> — `../../memoria/reglas-tfg.md`

Fusionada con: Verificación obligatoria: revisar_maquetacion.py en verde + revisión página a página
