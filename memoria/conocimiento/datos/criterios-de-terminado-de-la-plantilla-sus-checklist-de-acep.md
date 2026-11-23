---
tipo: "dato"
titulo: "Criterios de \"terminado\" de la plantilla SUS (checklist de aceptación)"
temas: ["calidad", "criterios", "latex", "sus", "terminado", "usabilidad", "verificacion"]
claves: ["compila sin errores", "CSV cambia todo", "calculos a mano", "tablas fuentes", "10 apartados", "resultados.json", "verificar.py", "probar_datos_raros.py", "revisar_tex.py", "FloatBarrier"]
proyectos: ["plantilla-sus"]
fuentes: ["../plantilla-sus/spec.md"]
confianza: "propuesto"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[calidad]] · [[criterios]] · [[latex]] · [[sus]] · [[terminado]] · [[usabilidad]] · [[verificacion]]

Checklist completo de criterios de aceptación (todos obligatorios):

1. **Compilación limpia**: LuaLaTeX sin errores ni warnings importantes en TeX Live estándar.
2. **Reactividad total**: Cambiar cualquier valor en `respuestas.csv` actualiza automáticamente todos los números, tablas y gráficas al recompilar.
3. **Verificación manual**: Cálculos coinciden con hacerlos a mano para todos los participantes de ejemplo.
4. **Fidelidad a fuentes**: Tablas de transformación (Sauro-Lewis 2016, Bangor et al. 2009/2008) coinciden exactamente con las publicaciones originales.
5. **Estructura completa**: Los 10 apartados del anexo están presentes y en el orden especificado.
6. **JSON exportado y verificado**: `resultados.json` se genera al compilar y pasa `verificar.py` (test externo invisible).
7. **Robustez con datos raros**: Pasa `probar_datos_raros.py` con `pruebas/respuestas-raras.csv` (decimales, notas bajas, caracteres especiales, fila inválida).
8. **PDF limpio**: Sin texto de comentarios ni código visible (`revisar_tex.py`); sin figuras dentro de la bibliografía (usar `\usepackage{placeins}` + `\FloatBarrier` antes de `\printbibliography`); etiquetas de gráficas sin solaparse.
9. **Fase 2 completada**: `defensa-sus.tex` existe y compila correctamente.

> Criterios de 'terminado': · Compila con LuaLaTeX sin errores. · Cambiar cualquier respuesta del CSV cambia correctamente todos los números y gráficas. · Los cálculos coinciden con hacerlos a mano para todos los participantes de ejemplo. · Las tablas de transformación coinciden con las fuentes citadas. · Los 10 apartados están, en el orden indicado. · `resultados.json` se genera al compilar y pasa `verificar.py`. · Pasa `probar_datos_raros.py`: compila y cuadra también con `pruebas/respuestas-raras.csv` (media con decimales, notas bajas, caracteres especiales, una fila inválida). · En el PDF no aparece texto de comentarios ni código (`revisar_tex.py` lo comprueba en parte), ni figuras dentro de la bibliografía, y las etiquetas de las gráficas no se pisan. · La Fase 2 está hecha: `defensa-sus.tex` compila (la prueba lo compila si existe).
> — `../plantilla-sus/spec.md` (cita sin comprobar)

Relacionado: [[exportar-resultados-json-obligatorio-para-verificacion-autom]] · [[fase-2-defensa-sus-tex-en-beamer-con-conclusiones-generadas]] · [[arquitectura-de-calculos-en-lualatex-para-plantilla-sus]] · [[cuatro-graficas-sus-reutilizables-donut-barra-rango-velocime]] · [[numeros-en-diagramas-de-secuencia-deben-coincidir-con-la-esp]] · [[estructura-de-archivos-obligatoria-para-la-plantilla-sus]] · [[validacion-final-del-pdf-antes-de-marcar-terminado]]

Origen: [[proyectos/plantilla-sus/estado|plantilla-sus]]
