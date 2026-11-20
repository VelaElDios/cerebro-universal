---
tipo: "decision"
titulo: "Fuentes faltantes bloquean verificación automática de números"
temas: ["fuentes", "numeros", "verificacion"]
claves: ["verificar.py", "fuentes faltantes", "numeros >20"]
proyectos: ["memoria-procesos"]
fuentes: ["spec del proyecto y resultado de prueba"]
confianza: "propuesto"
fecha: "2026-11-20"
actualizado: "2026-11-20"
---

Temas: [[fuentes]] · [[numeros]] · [[verificacion]]

El script verificar.py comprueba que todo número mayor que 20 en el texto aparezca en las fuentes proporcionadas. Si faltan fuentes principales (documentacion-tecnica.md, gestion/README.md, revision-entrega.md, hito4-configuracion.md), la verificación falla en cascada. No se puede aprobar la memoria sin estas fuentes. La acción inmediata debe ser conseguirlas antes de seguir corrigiendo otros aspectos.

> VERIFICACIÓN FALLIDA: 16 problema(s) - el número «32» no aparece en las fuentes (¿inventado o mal copiado?)
> — `spec del proyecto y resultado de prueba` (cita sin comprobar)

Relacionado: [[fuentes-faltantes-bloquean-verificacion-automatica]] · [[validacion-completa-de-numeros-en-memoria-tfg-con-verificar]] · [[como-manejar-fuentes-faltantes-en-verificacion-automatica-de]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
