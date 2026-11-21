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

Relacionado: [[fuentes-faltantes-bloquean-verificacion-automatica]] · [[validacion-completa-de-numeros-en-memoria-tfg-con-verificar]] · [[como-manejar-fuentes-faltantes-en-verificacion-automatica-de]] · [[numeros-en-la-memoria-deben-aparecer-tal-cual-en-las-fuentes]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]

> ⚠️ Posible contradicción con [[numeros-pequenos-tambien-se-verifican-en-fuentes-no-solo-20]]: Nota A afirma que `verificar.py` comprueba solo números mayores que 20. Nota B (primer párrafo) afirma lo contrario: que comprueba TODOS los números, no solo los > 20. La ampliación de la propia Nota B rectifica y coincide con Nota A (solo > 20 automáticos), pero la afirmación inicial de B contradice a A.
