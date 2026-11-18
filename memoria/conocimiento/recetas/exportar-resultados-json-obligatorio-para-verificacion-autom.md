---
tipo: "receta"
titulo: "Exportar resultados.json obligatorio para verificación automática"
temas: ["json", "latex", "lua", "sus", "test", "usabilidad", "verificacion"]
claves: ["resultados.json", "verificar.py", "probar_datos_raros.py", "%.6f", "desviacion muestral"]
proyectos: ["plantilla-sus"]
fuentes: ["../plantilla-sus/spec.md"]
confianza: "verificado"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[json]] · [[latex]] · [[lua]] · [[sus]] · [[test]] · [[usabilidad]] · [[verificacion]]

El archivo `sus-calculos.lua` debe escribir `resultados.json` al compilar (usando `io.open(..., "w")` en UTF-8). Formato exacto requerido:

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

Reglas estrictas:
- `participantes`: uno por fila válida del CSV, mismo orden. Filas inválidas se excluyen (el documento avisa).
- `nota`: exactamente A+, A, A-, B+, B, B-, C+, C, C-, D o F (Sauro y Lewis, 2016).
- `adjetivo`: exactamente uno de los 7 valores de Bangor et al. (2009).
- `aceptabilidad`: exactamente "No aceptable", "Marginal" o "Aceptable".
- `desviacion`: **desviación típica muestral** (dividir entre n-1, no n).
- **Números con punto decimal y SIN redondear**: usar `%.6f` para media, desviación, mínimo, máximo y puntuaciones (nunca `%.1f`).
- Textos idénticos a los definidos (mayúsculas, acentos, espacios).

El test `verificar.py` recalcula desde el CSV y compara; `probar_datos_raros.py` prueba con `pruebas/respuestas-raras.csv` (decimales, notas bajas, caracteres especiales, fila inválida).

> Al compilar, `sus-calculos.lua` debe escribir `resultados.json` en la carpeta del documento (junto a `anexo-sus.tex`) con los valores que se imprimen en el documento. Un test automático externo (`verificar.py`, que las IAs no pueden ver ni modificar) recalcula todo desde el CSV y lo compara: si no cuadra, la prueba falla.
> — `../plantilla-sus/spec.md`

Relacionado: [[arquitectura-de-calculos-en-lualatex-para-plantilla-sus]] · [[criterios-de-terminado-de-la-plantilla-sus-checklist-de-acep]] · [[trampas-tecnicas-comprobadas-en-lualatex-evitar-errores-de-c]]

Origen: [[proyectos/plantilla-sus/estado|plantilla-sus]]
