---
tipo: "receta"
titulo: "Legibilidad de diagramas: sin cruces, sin palabras partidas, flechas caja-a-caja"
temas: ["diagramas", "latex", "memoria", "tfg", "tikz"]
claves: ["node distance", "text width", "|-", "-|", "7.5 pt", "revisar_figuras.py"]
proyectos: []
fuentes: ["../../memoria/reglas-tfg.md"]
confianza: "verificado"
fecha: "2026-11-21"
actualizado: "2026-11-21"
---

Temas: [[diagramas]] · [[latex]] · [[memoria]] · [[tfg]] · [[tikz]]

Reglas de dibujo para diagramas (TikZ, Mermaid, etc.):
- Flechas siempre de caja adyacente a caja adyacente (A→B, B→C). Nada de saltar cajas (A→C por encima de B).
- Si hay que rodear, usar codos ortogonales: `|-` (vertical luego horizontal) o `-|` (horizontal luego vertical).
- Separar cajas con `node distance` suficiente.
- Dentro de cajas: no partir palabras ni rutas (ej. «sr-c/services»). Soluciones: aumentar `text width`, salto de línea manual `\\`, o abreviar.
- Tamaño mínimo de letra en el PDF: 7,5 pt (comprobado por `scripts/revisar_figuras.py`).
- Si el script detecta problemas (líneas sobre letras, cajas solapadas, palabras con guión, letras < 7,5 pt), hay que replantear el diagrama (separar, ensanchar, reducir participantes), NO encoger con `adjustbox`/`resizebox`/`scale`.

> **Ninguna línea ni flecha atraviesa una caja o un texto, y ninguna caja pisa a otra.** Las flechas van de una caja a la siguiente (A → B, B → C), nunca de A a C pasando por encima de B; si hay que rodear, con codos (`|-`, `-|`) y separando bien las cajas (`node distance` suficiente).
> — `../../memoria/reglas-tfg.md`
