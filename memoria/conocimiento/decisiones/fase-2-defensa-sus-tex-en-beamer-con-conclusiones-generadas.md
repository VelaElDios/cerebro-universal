---
tipo: "decision"
titulo: "Fase 2: defensa-sus.tex en Beamer con conclusiones generadas dinámicamente"
temas: ["beamer", "conclusiones-dinamicas", "defensa", "latex", "sus", "usabilidad"]
claves: ["defensa-sus.tex", "sus.imprimir_conclusiones_defensa()", "probar_datos_raros.py"]
proyectos: ["plantilla-sus"]
fuentes: ["../plantilla-sus/spec.md"]
confianza: "verificado"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[beamer]] · [[conclusiones-dinamicas]] · [[defensa]] · [[latex]] · [[sus]] · [[usabilidad]]

Decisión de diseño: la Fase 2 crea `defensa-sus.tex` (Beamer) con 2-3 diapositivas que reutilizan las mismas 4 gráficas del anexo. Las conclusiones **no son texto fijo** sino que se generan en Lua (`sus.imprimir_conclusiones_defensa()`) según los datos reales:

- Frases distintas según: media > 68 vs media < 68, y aceptabilidad (Aceptable / Marginal / No aceptable).
- Ejemplo: con media 38,75 no debe aparecer "se compara favorablemente" ni "viabilidad confirmada".
- `probar_datos_raros.py` compila las diapositivas con datos malos y falla si aparecen frases fijas incorrectas.
- Etiquetas de gráficas sin solapamientos.

> Las conclusiones de las diapositivas **salen de los datos**, igual que el apartado 10 del anexo: frases elegidas en `sus-calculos.lua` según la media frente a 68 y la aceptabilidad (por ejemplo `sus.imprimir_conclusiones_defensa()`, que imprime los `\item`). Nada de frases fijas como 'se compara favorablemente' o 'viabilidad confirmada': con una media de 38,75 serían falsas.
> — `../plantilla-sus/spec.md`

Origen: [[proyectos/plantilla-sus/estado|plantilla-sus]]
