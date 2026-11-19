---
tipo: "receta"
titulo: "Verificación automática de diagramas con scripts/revisar_figuras.py"
temas: ["diagramas", "latex", "memoria", "tfg", "verificacion"]
claves: ["scripts/revisar_figuras.py", "Gemini", "reglas 16-18"]
proyectos: []
fuentes: ["../../memoria/reglas-tfg.md"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[diagramas]] · [[latex]] · [[memoria]] · [[tfg]] · [[verificacion]]

Ejecutar `scripts/revisar_figuras.py` que renderiza cada página con diagrama a imagen y pasa a Gemini para validar reglas 16-18 (legibilidad, routing, cajas). Si Gemini reporta fallos, corregir el diagrama (separar cajas, flechas correctas, más ancho, menos participantes). No se debate la decisión del comprobador.

> Los diagramas se miran de verdad en el PDF: `scripts/revisar_figuras.py` convierte en imagen cada página con un diagrama dibujado y Gemini comprueba las reglas 16-18 a ojo. Si dice que algo falla, se corrige el dibujo (separar cajas, flechas de caja en caja, cajas más anchas, menos participantes); no se discute con el comprobador.
> — `../../memoria/reglas-tfg.md`

Relacionado: [[comprobar-la-maquetacion-de-un-tfg-automaticamente]] · [[checklist-final-antes-de-marcar-terminado-pdf-pagina-a-pagin]] · [[memoria-tfg-aprobada-tras-pasar-todos-los-tests-automaticos]]
