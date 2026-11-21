---
tipo: "decision"
titulo: "Números en la memoria deben aparecer tal cual en las fuentes"
temas: ["fuentes", "latex", "verificacion"]
claves: ["verificar.py", "números", "fuentes"]
proyectos: ["memoria-procesos"]
fuentes: ["memoria/reglas-tfg.md"]
confianza: "propuesto"
fecha: "2026-11-20"
actualizado: "2026-11-20"
---

Temas: [[fuentes]] · [[latex]] · [[verificacion]]

Antes de escribir cualquier cifra (también las pequeñas, y las que salen de sumar), buscarla en las fuentes y copiarla tal cual. Si hay que contar elementos de una lista (P1–P14 y P18), contarlos uno a uno y comprobarlo con la tabla de la fuente. Lo que no está en las fuentes no se escribe. Si el script `verificar.py` falla, comprobar que las fuentes estén accesibles y que el formato del número en el texto coincida exactamente (sin espacios extra, sin comas decimales en números enteros).

> El test comprueba que todo número mayor que 20 del texto aparece en las fuentes; los pequeños los comprueba el revisor.
> — `memoria/reglas-tfg.md` (cita sin comprobar)

Relacionado: [[cada-cifra-del-documento-sale-de-las-fuentes-tambien-las-peq]] · [[como-manejar-fuentes-faltantes-en-verificacion-automatica-de]] · [[fuentes-faltantes-bloquean-verificacion-automatica-de-numero]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]

> ⚠️ Posible contradicción con [[numeros-pequenos-tambien-se-verifican-en-fuentes-no-solo-20]]: Nota A afirma que el test automático solo comprueba números > 20 y los pequeños los revisa el revisor. Nota B (primer párrafo) afirma lo contrario: que `verificar.py` comprueba TODOS los números, no solo los > 20. (La ampliación posterior de la propia Nota B rectifica y coincide con Nota A).
