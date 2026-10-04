# Bitácora del proyecto

Registro de lo que hace cada IA, paso a paso.

## 2026-10-04 05:27 · Constructor (gemini · gemini-flash-latest)

He creado la base de datos de ejemplo (`datos/respuestas.csv`), el motor de cálculo y lógica en Lua (`sus-calculos.lua`) con validación de entradas, cálculo de puntuaciones SUS, estadísticas (media, desviación típica, mínimo y máximo) y asignación de escalas normativas (Sauro y Lewis 2016, Bangor et al. 2008 y 2009), junto con el archivo de bibliografía completo (`referencias.bib`) con las citas canónicas requeridas por la especificación.

**Archivos:** `datos/respuestas.csv`, `sus-calculos.lua`, `referencias.bib`

**Siguiente:** Crear los archivos de las 4 gráficas TikZ modulares (`graficas/donut.tex`, `graficas/rango.tex`, `graficas/velocimetro.tex`, `graficas/barras.tex`) y el archivo de contenido principal (`contenido-sus.tex`) con los 10 apartados estructurados de la spec.

## 2026-10-04 05:28 · Revisor (openrouter · nvidia/nemotron-3.5-lightning:free)

**Veredicto:** cambios · **Prueba:** ❌ falla la prueba

**Qué está bien:**
El motor de cálculo en Lua (`sus-calculos.lua`) está correctamente implementado y libre de errores graves. Los cálculos SUS (ítems impares/pares, multiplicación por 2.5) son exactos. Las escalas normativas (Sauro & Lewis 2016 para notas A+/F, Bangor et al. 2009 para adjetivos, Bangor et al. 2008 para aceptabilidad) coinciden con los rangos canónicos de las fuentes citadas. La validación del CSV funciona correctamente y avisa de errores de formato. El formato de coma decimal está correcto para el idioma español.

**Qué está mal / Pendiente:**
El proyecto actual se queda en la base de datos y la lógica, pero le faltan los componentes esenciales para que sea una plantilla compilable según la spec:
1.  **Falta `anexo-sus.tex`**: El documento independiente que integra todo.
2.  **Falta `contenido-sus.tex`**: El contenido particionado para `\input{}` en el TFG.
3.  **Faltan las gráficas en `graficas/*.tex`**: Las 4 gráficas (Donut, Rango, Velocímetro, Barras) necesarias para el apartado 9 y la Fase 2.
Sin estos archivos, no es posible compilar con LuaLaTeX ni cumplir el criterio de "Los 10 apartados están".

**Correcciones realizadas:**
Ninguna. El código Lua entregado por el constructor es funcional y correcto para los datos de ejemplo (verificado manualmente el participante U1: puntuación 90, nota A+, adjetivo "El mejor imaginable", aceptabilidad Aceptable).

<<<ARCHIVO ruta/relativa.ext>>
(No hay archivos .tex que corregir en este paso, el código Lua está aprobado como está).

**Correcciones del revisor:** ninguna

**Tareas para el constructor:**
- Crear el archivo `anexo-sus.tex` con la estructura completa de los 10 apartados especificados, integrando las llamadas a las funciones de `sus-calculos.lua` y el CSV.
- Crear el archivo `contenido-sus.tex` con el contenido particionado para `\input{}` desde la plantilla del TFG.
- Crear los 4 archivos de gráficas TikZ en la carpeta `graficas/`: `donut.tex`, `rango.tex`, `velocimetro.tex`, `barras.tex`. Estas deben ser modulares y usar las coordenadas/estadísticas exportadas por el motor Lua.
- Integrar la carga del CSV y la impresión de errores/estadísticas en los nuevos archivos .tex.
