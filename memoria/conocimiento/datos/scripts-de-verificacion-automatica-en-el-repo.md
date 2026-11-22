---
tipo: "dato"
titulo: "Scripts de verificación automática en el repo"
temas: ["latex", "memoria", "python", "scripts", "tfg"]
claves: ["scripts/revisar_maquetacion.py", "scripts/revisar_figuras.py", "Gemini"]
proyectos: []
fuentes: ["../../memoria/reglas-tfg.md"]
confianza: "propuesto"
fecha: "2026-11-21"
actualizado: "2026-11-21"
---

Temas: [[latex]] · [[memoria]] · [[python]] · [[scripts]] · [[tfg]]

Dos scripts Python en el repositorio validan la maquetación:
- `scripts/revisar_maquetacion.py`: comprueba reglas medibles automáticamente (portada, tablas, figuras, flotantes, etc.). Debe salir en verde.
- `scripts/revisar_figuras.py`: analiza el PDF generado midiendo coordenadas reales de los diagramas (detecta líneas sobre texto, cajas solapadas, palabras con guión, letras < 7,5 pt). Si detecta problemas, avisa y Gemini revisa también a ojo.
Ambos scripts son parte del criterio de «TERMINADO».

> `scripts/revisar_maquetacion.py` comprueba automáticamente las que se pueden medir. [...] `scripts/revisar_figuras.py` mide cada diagrama con las coordenadas reales del PDF (líneas que pasan por encima de letras, cajas que se pisan, palabras partidas con guion, letras de menos de 7,5 pt) y, si eso pasa, Gemini lo mira además a ojo.
> — `../../memoria/reglas-tfg.md` (cita sin comprobar)

Relacionado: [[comprobar-la-maquetacion-de-un-tfg-automaticamente]] · [[verificacion-automatica-de-diagramas-con-scripts-revisar-fig]] · [[checklist-final-antes-de-marcar-terminado-pdf-pagina-a-pagin]]
