---
tipo: "decision"
titulo: "Deshacer el paso entero si rompe la compilación"
temas: ["cerebro", "orquestador"]
claves: ["rompe", "restaurar", "foto", "paso deshecho"]
proyectos: []
fuentes: ["scripts/proyecto.py"]
confianza: "verificado"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[cerebro]] · [[orquestador]]

Antes de aplicar la respuesta del constructor se guarda una foto del borrador (`nucleo.foto`). Si después de los intentos la prueba falla «de verdad» (cumple `reintentar_si` o se cuelga) y antes no fallaba, se restaura la foto (`nucleo.restaurar`) y se apunta «paso deshecho» en la bitácora. Con las correcciones del revisor se hace lo mismo.

> mejor no avanzar que retroceder
> — `scripts/proyecto.py`

Relacionado: [[tocar-trozos-con-cambiar-en-vez-de-reescribir-archivos-enter]]
