---
proyecto: plantilla-sus
estado: en-construccion
---

# Plantilla SUS en LaTeX — Especificación

## Objetivo

Plantilla LaTeX para el anexo de evaluación de usabilidad con SUS (System Usability Scale)
de un TFG/TFM, más las gráficas para la defensa. Se usará primero en una práctica de
Calidad de Software y después en el TFG de Javier.

**Principio clave: todo automático.** El usuario solo rellena `datos/respuestas.csv`.
Puntuaciones, estadísticas, nota, adjetivo, aceptabilidad, tablas y gráficas se calculan
y generan solos al compilar. Cambiar un dato actualiza todo el documento.

## Requisitos técnicos

- Compilador: **LuaLaTeX** (permite hacer los cálculos en Lua dentro del documento).
- Idioma: español (`babel` con `spanish`), coma decimal en los números.
- Gráficas con TikZ/pgfplots, sin imágenes externas.
- Debe compilar sin errores ni warnings importantes en TeX Live estándar.
- Doble uso:
  - `anexo-sus.tex` compila solo como documento independiente.
  - `contenido-sus.tex` contiene solo el contenido, para hacer `\input{}` desde la plantilla del TFG.
- Código limpio y comentado en español: el usuario tiene que poder entenderlo y retocarlo.

### Trampas técnicas comprobadas (evítalas)

- Todo el código Lua va en `sus-calculos.lua` y se carga con `\directlua{dofile("sus-calculos.lua")}`.
  Dentro de `\directlua{...}` solo llamadas cortas a funciones ya definidas: **nunca** escribir `%`
  ni cadenas con `\` ahí dentro, porque TeX los interpreta antes que Lua y rompe la compilación.
- Para devolver texto de Lua a LaTeX usar `tex.sprint(...)`.

## Datos de entrada: `datos/respuestas.csv`

Una fila por participante:

```
id,perfil,q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,comentario
U1,Cliente,5,1,5,1,4,2,5,1,5,1,"Visualización de métricas clave sin editar fórmulas"
U2,Encargado,4,2,5,1,5,1,4,2,4,1,"Interfaz limpia y ágil"
```

- Respuestas en escala Likert de 1 a 5.
- Incluir 3-5 participantes de ejemplo con datos inventados y realistas.
- Si una respuesta falta o está fuera de 1-5, el documento debe avisar claramente en vez de calcular mal.

## Estructura del anexo (pautas del profesor, en este orden)

1. **Objetivo del anexo**: qué se evalúa y por qué.
2. **Qué es el SUS**: quién lo introdujo (John Brooke, 1986; publicado en 1996), qué mide, escala Likert de 5 puntos (con referencia a Likert, 1932).
3. **Tabla de preguntas SUS**: los 10 ítems en español, indicando cuáles son positivos (impares) y negativos (pares).
4. **Tabla de puntuaciones**: significado de cada valor de la escala (1 = totalmente en desacuerdo ... 5 = totalmente de acuerdo).
5. **Cómo se calcula**:
   - Ítems impares: respuesta − 1
   - Ítems pares: 5 − respuesta
   - Suma de las 10 contribuciones × 2,5 → puntuación de 0 a 100
   - Incluir la fórmula en notación matemática y un ejemplo resuelto con el primer participante.
6. **Cómo se transforma**:
   - Escala de notas curvada de **Sauro y Lewis (2016)** (A+ a F) en tabla.
   - Adjetivos de **Bangor, Kortum y Miller (2009)**. El artículo da la puntuación **media** de cada
     adjetivo, no rangos: El peor imaginable 12,5 · Horrible 20,3 · Pobre 35,7 · OK 50,9 · Bueno 71,4 ·
     Excelente 85,5 · El mejor imaginable 90,9. Se asigna el adjetivo cuya media está más cerca, es decir,
     con los puntos medios como límites: ≥88,2 El mejor imaginable · ≥78,45 Excelente · ≥61,15 Bueno ·
     ≥43,3 OK · ≥28,0 Pobre · ≥16,4 Horrible · resto El peor imaginable. El documento explica este
     criterio y muestra la tabla de medias.
   - Rangos de aceptabilidad de **Bangor, Kortum y Miller (2008)**: no aceptable / marginal / aceptable.
   - Mencionar que la media de referencia del SUS es 68.
   - Los valores de las tablas deben coincidir con las fuentes originales: el revisor debe comprobarlos.
7. **Introducción a los resultados**: texto plantilla con huecos para contexto (nº de participantes, tareas realizadas, método).
8. **Perfiles**: tabla generada desde el CSV con id, perfil y comentario.
9. **Tabla de resultados**: por participante, sus 10 respuestas, su puntuación SUS, nota, adjetivo y aceptabilidad. Al final: media, desviación típica, mínimo y máximo.
10. **Interpretación de resultados**: texto plantilla que incluye automáticamente la media, la nota y la aceptabilidad calculadas, con huecos para el análisis cualitativo.

Más un apartado de **referencias bibliográficas** con todas las fuentes citadas.

## Gráficas (reutilizables en el anexo y en la defensa)

Cada gráfica en su propio archivo dentro de `graficas/`, usable con `\input{}`:

- **Donut**: media SUS en grande en el centro, arco proporcional a la puntuación, nota y adjetivo debajo.
- **Barra de rango**: de 0 a 100, marcando el 68 de referencia y el rango mín-máx de los participantes.
- **Velocímetro**: semicírculo con zonas no aceptable (0-50, rojo), marginal (50-70, amarillo) y aceptable (70-100, verde), con la aguja en la media.
- **Barras por participante**: puntuación de cada uno con una línea en 68.

Colores definidos en un único sitio para cambiarlos fácilmente.

## Fase 2 (cuando la fase 1 esté terminada)

`defensa-sus.tex` en Beamer: 2-3 diapositivas de resultados usando las mismas gráficas,
en la línea de las capturas de ejemplo del profesor (resultado global, rango, conclusiones).

## Estructura de archivos

```
final/
├── anexo-sus.tex          # documento independiente
├── contenido-sus.tex      # contenido para \input en el TFG
├── sus-calculos.lua       # todos los cálculos
├── datos/respuestas.csv
├── graficas/*.tex
└── referencias.bib
```

## Exportar `resultados.json` (obligatorio, lo comprueba el test)

Al compilar, `sus-calculos.lua` debe escribir `resultados.json` en la carpeta del documento (junto a
`anexo-sus.tex`) con los valores que se imprimen en el documento. Un test automático externo
(`verificar.py`, que las IAs no pueden ver ni modificar) recalcula todo desde el CSV y lo compara:
si no cuadra, la prueba falla.

Formato exacto (números con punto decimal, sin redondear; textos idénticos a los de abajo):

```json
{
  "participantes": [
    {"id": "U1", "puntuacion": 95.0, "nota": "A+",
     "adjetivo": "El mejor imaginable", "aceptabilidad": "Aceptable"}
  ],
  "estadisticas": {"n": 5, "media": 85.0, "desviacion": 10.7529,
                   "minimo": 72.5, "maximo": 95.0}
}
```

- `participantes`: uno por cada fila válida del CSV, en el mismo orden. Las filas con respuestas
  inválidas no se incluyen (el documento avisa de ellas).
- `nota`: A+, A, A-, B+, B, B-, C+, C, C-, D o F (Sauro y Lewis, 2016).
- `adjetivo`: exactamente uno de `El peor imaginable`, `Horrible`, `Pobre`, `OK`, `Bueno`,
  `Excelente`, `El mejor imaginable`.
- `aceptabilidad`: exactamente uno de `No aceptable`, `Marginal`, `Aceptable`.
- `desviacion`: desviación típica **muestral** (dividiendo entre n − 1).
- Escribirlo desde Lua con `io.open(..., "w")`, en UTF-8. Recordatorio: nada de `%` ni `\` dentro
  de `\directlua{...}`; la función va en `sus-calculos.lua` y desde el `.tex` solo se llama.

## Criterios de "terminado"

- Compila con LuaLaTeX sin errores.
- Cambiar cualquier respuesta del CSV cambia correctamente todos los números y gráficas.
- Los cálculos coinciden con hacerlos a mano para todos los participantes de ejemplo.
- Las tablas de transformación coinciden con las fuentes citadas.
- Los 10 apartados están, en el orden indicado.
- `resultados.json` se genera al compilar y pasa `verificar.py`.
