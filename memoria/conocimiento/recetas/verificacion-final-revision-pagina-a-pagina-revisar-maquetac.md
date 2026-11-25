---
tipo: "receta"
titulo: "Verificación final: revisión página a página + revisar_maquetacion.py en verde"
temas: ["latex", "memoria", "python", "tfg"]
claves: ["revisar_maquetacion.py", "PDF", "página a página", "TERMINADO"]
proyectos: []
fuentes: ["../../memoria/reglas-tfg.md"]
confianza: "verificado"
fecha: "2026-11-23"
actualizado: "2026-11-23"
---

Temas: [[latex]] · [[memoria]] · [[python]] · [[tfg]]

- Paso obligatorio antes de marcar «TERMINADO»:
  1. Revisar el PDF página a página (visual).
  2. Ejecutar `scripts/revisar_maquetacion.py` → debe salir en verde (cero errores).
- El script mide reglas automatizables (márgenes, flotantes, anchos, etc.).
- Lo no medible (legibilidad de tablas, coherencia de orden, prosa vs capturas) lo valida el revisor humano/IA.
- Si algo falla, corregir y repetir hasta verde + revisión visual limpia.

> Antes de marcar TERMINADO, el PDF se revisa página a página, y `revisar_maquetacion.py` debe salir en verde. Lo que no mide el script (que las tablas se lean bien y que el orden tenga sentido) lo comprueba el revisor.
> — `../../memoria/reglas-tfg.md`

Relacionado: [[reglas-de-maquetacion-de-javier-resumen-accionable]] · [[verificacion-automatica-de-diagramas-con-scripts-revisar-fig]] · [[checklist-final-antes-de-marcar-terminado-pdf-pagina-a-pagin]] · [[validacion-final-del-pdf-antes-de-marcar-terminado]] · [[scripts-de-verificacion-automatica-en-el-repo]] · [[comprobar-la-maquetacion-de-un-tfg-automaticamente]]
