---
tipo: "receta"
titulo: "Verificación automática de diagramas con scripts/revisar_figuras.py"
temas: ["diagramas", "latex", "memoria", "tfg", "verificacion", "python"]
claves: ["scripts/revisar_figuras.py", "Gemini", "reglas 16-18"]
proyectos: []
fuentes: ["../../memoria/reglas-tfg.md"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-23"
---

Temas: [[diagramas]] · [[latex]] · [[memoria]] · [[tfg]] · [[verificacion]]

Ejecutar `scripts/revisar_figuras.py` que renderiza cada página con diagrama a imagen y pasa a Gemini para validar reglas 16-18 (legibilidad, routing, cajas). Si Gemini reporta fallos, corregir el diagrama (separar cajas, flechas correctas, más ancho, menos participantes). No se debate la decisión del comprobador.

> Los diagramas se miran de verdad en el PDF: `scripts/revisar_figuras.py` convierte en imagen cada página con un diagrama dibujado y Gemini comprueba las reglas 16-18 a ojo. Si dice que algo falla, se corrige el dibujo (separar cajas, flechas de caja en caja, cajas más anchas, menos participantes); no se discute con el comprobador.
> — `../../memoria/reglas-tfg.md`

Relacionado: [[comprobar-la-maquetacion-de-un-tfg-automaticamente]] · [[checklist-final-antes-de-marcar-terminado-pdf-pagina-a-pagin]] · [[memoria-tfg-aprobada-tras-pasar-todos-los-tests-automaticos]] · [[scripts-de-verificacion-automatica-en-el-repo]] · [[verificacion-final-revision-pagina-a-pagina-revisar-maquetac]]

## Ampliación (2026-11-23, )
- Ejecutar `scripts/revisar_figuras.py` sobre el PDF generado.
- El script detecta con coordenadas reales:
  1. Líneas/flechas que pasan por encima de letras.
  2. Cajas que se pisan.
  3. Palabras partidas con guion dentro de cajas.
  4. Letras < 7,5 pt.
- Si el script avisa, Gemini revisa a ojo (si hay cupo/modelo disponible).
- NO corregir encogiendo el dibujo (`adjustbox`, `resizebox`, `scale`): eso achica las letras.
- Corregir replanteando: separar cajas, flechas caja-a-caja, cajas más anchas, menos participantes.
- Si Gemini no está disponible, la medición del script basta; no es excusa para no terminar.
