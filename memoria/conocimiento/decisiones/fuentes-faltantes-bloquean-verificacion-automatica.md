---
tipo: "decision"
titulo: "Fuentes faltantes bloquean verificación automática"
temas: ["fuentes", "memoria-procesos", "verificar.py"]
claves: ["documentacion-tecnica.md", "gestion/README.md", "revision-entrega.md", "hito4-configuracion.md"]
proyectos: ["memoria-procesos"]
fuentes: ["experiencia del revisor en este proyecto"]
confianza: "propuesto"
fecha: "2026-11-20"
actualizado: "2026-11-20"
---

Temas: [[fuentes]] · [[memoria-procesos]] · [[verificar.py]]

Los archivos faltantes son referenciados en la spec como "única verdad". Deben crearse en el repo para que la verificación automática funcione. El contenido puede extraerse de los docs existentes que sí están en @arbol.
relacionado: Placeholders "XX" para números sin verificar en memoria LaTeX, Cada cifra de un documento sale de las fuentes, también las pequeñas

> VERIFICACIÓN FALLIDA: 16 problema(s) ... y 726 números más que no están en las fuentes"
problema: El script `verificar.py` comprueba que todo número >20 del texto aparece en las fuentes. Las 4 fuentes principales listadas en el spec no existen en el repo (@arbol), por lo que el test falla masivamente.
solucion: Crear estos 4 archivos en `docs/` usando como base los archivos existentes (`requisitos.md`, `sprint-1.md`, `sprint-2.md`, `procesos.md`, `decisiones.md`, `arquitectura.md`, `juego.md`, `log.md`) que ya contienen la información. Una vez creados, `verificar.py` podrá validar las cifras.
> — `experiencia del revisor en este proyecto` (cita sin comprobar)

Relacionado: [[fuentes-faltantes-bloquean-verificacion-automatica-de-numero]] · [[validacion-completa-de-numeros-en-memoria-tfg-con-verificar]] · [[como-manejar-fuentes-faltantes-en-verificacion-automatica-de]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]

> ⚠️ Posible contradicción con [[numeros-pequenos-tambien-se-verifican-en-fuentes-no-solo-20]]: La Nota A afirma que `verificar.py` "comprueba que todo número >20 del texto aparece en las fuentes". La Nota B (primer párrafo) afirma lo contrario: que "comprueba TODOS los números del texto contra las fuentes, no solo los > 20". Aunque la ampliación posterior de la Nota B rectifica y coincide con la Nota A, la afirmación inicial de la Nota B contradice directamente a la Nota A sobre el comportamiento del script.
