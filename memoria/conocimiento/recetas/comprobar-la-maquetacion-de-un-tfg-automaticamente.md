---
tipo: "receta"
titulo: "Comprobar la maquetación de un TFG automáticamente"
temas: ["latex", "tfg", "verificacion"]
claves: ["revisar_maquetacion.py", "pdftotext", "poppler-utils"]
proyectos: []
fuentes: ["scripts/revisar_maquetacion.py"]
confianza: "verificado"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[latex]] · [[tfg]] · [[verificacion]]

`scripts/revisar_maquetacion.py` se ejecuta desde `borrador/` después de compilar (`python3 ../../../scripts/revisar_maquetacion.py Memoria.pdf`). Falla si encuentra cualquiera de estas cosas:

- otra portada que no sea la oficial;
- falta algo de la plantilla;
- el color `tema` no es negro;
- columnas `m{}`;
- una imagen repetida;
- `->` en un caption;
- en el PDF, leído página a página con `pdftotext`: páginas en blanco, páginas con una sola imagen o casi vacías.

Necesita el paquete `poppler-utils`.

> Comprueba las reglas de maquetación de un TFG
> — `scripts/revisar_maquetacion.py`

Relacionado: [[como-se-pone-la-portada-oficial-del-tfg-esiiab-uclm]] · [[memoria-tfg-aprobada-tras-pasar-todos-los-tests-automaticos]] · [[la-memoria-tfg-se-entrega-en-pdf-con-marcadores-preferibleme]] · [[checklist-final-antes-de-marcar-terminado-pdf-pagina-a-pagin]] · [[verificacion-automatica-de-diagramas-con-scripts-revisar-fig]] · [[scripts-de-verificacion-automatica-en-el-repo]] · [[verificacion-final-revision-pagina-a-pagina-revisar-maquetac]]
