---
tipo: "decision"
titulo: "Una sola imagen por captura en toda la memoria (Regla 10 Javier) — fusión de notas"
temas: ["duplicados", "figuras", "gestion-contenido", "latex", "maquetacion", "maquetación", "memoria-procesos", "ref", "regla 10 javier", "reglas-javier", "reglas-tfg"]
claves: ["regla 10", "imágenes repetidas", "ref cruzadas", "imagen repetida", "\\ref", "una sola vez", "capturas duplicadas", "figura repetida", "ref cruzado", "DoneTonic", "produccion", "ref", "figura", "captura", "duplicado"]
proyectos: ["memoria-procesos"]
fuentes: ["memoria/reglas-tfg.md", "memoria/reglas-tfg.md (regla 10)", "memoria/reglas-tfg.md regla 10 y spec versión 4"]
confianza: "verificado"
fecha: "2026-11-16"
actualizado: "2026-11-25"
---

Temas: [[duplicados]] · [[figuras]] · [[gestion-contenido]] · [[latex]] · [[maquetacion]] · [[maquetación]] · [[memoria-procesos]] · [[ref]] · [[regla 10 javier]] · [[reglas-javier]] · [[reglas-tfg]]

# Una sola imagen por captura en toda la memoria (Regla 10 Javier)

**Temas:** `[[duplicados]]` · `[[figuras]]` · `[[latex]]` · `[[maquetacion]]` · `[[maquetación]]` · `[[memoria-procesos]]` · `[[ref]]` · `[[reglas-javier]]` · `[[reglas-tfg]]`

---

## Regla central
Cada archivo de imagen físico en `figs/capturas/` debe aparecer en `\includegraphics` **exactamente una vez** en todo el documento. En los demás capítulos, sustituir `\includegraphics{...}` por `\ref{fig:etiqueta-canónica}` (y, si procede, breve mención: «como se muestra en la Figura~\ref{fig:...}»).  
> **Regla 10 — `memoria/reglas-tfg.md`**  
> *Sin figuras repetidas: cada imagen aparece una sola vez. Si hace falta en otro sitio, se pone `\ref` a la figura que ya existe.*

**Prioridad:** decidir la ubicación canónica donde la captura tiene más sentido (cap. 4, 5, anexos) y mantenerla solo allí. Las capturas de **DoneTonic, producción, prueba técnica y Hito 4** son las de mayor riesgo de duplicación.

---

## Inventario de capturas por carpeta (mínimos spec)
| Carpeta | Capturas esperadas |
|---------|-------------------|
| `app/` | 4 |
| `hito4/` | 4 |
| `juego/` | 8 |
| `donetonic/` | 5 |
| `produccion/` | 2 |
| `prueba-tecnica/` | 1 |

*Cada archivo físico en `figs/capturas/` debe usarse una sola vez en el documento.*

---

## Ubicación canónica por captura (lista consolidada)

| Captura (archivo / descripción) | Label canónico | Ubicación canónica (Nota A) | Ubicación canónica (Nota B, versión 4) | Estado |
|--------------------------------|----------------|----------------------------|----------------------------------------|--------|
| Tablero Sprint 1 (`01-tablero-sprint`) | `fig:donetonic-tablero` | **03-propuesta.tex** (cap. 3) | **cap. 3** | ✅ Coinciden |
| Gráficas Sprint 1 (`02-graficas-sprint`) | `fig:donetonic-graficas-s1` | **a1-desarrollo.tex** (anexo A1) | **cap. 3** | ⚠️ **DISCREPANCIA** |
| Backlog (`03-backlog`) | `fig:donetonic-backlog` | **a1-desarrollo.tex** (anexo A1) | **cap. 3** | ⚠️ **DISCREPANCIA** |
| Tablero Sprint 2 (`04-tablero-sprint2`) | `fig:donetonic-s2-tablero` | **a1-desarrollo.tex** (anexo A1) | **anexo A1** | ✅ Coinciden |
| Gráficas Sprint 2 (`06-graficas-sprint2`) | `fig:donetonic-s2-graficas` | **a1-desarrollo.tex** (anexo A1) | **anexo A1** | ✅ Coinciden |
| Detalle Sprint 2 (nuevo en Nota B) | `fig:donetonic-s2-detalle` | — | **anexo A1** | Solo en Nota B |
| Correo confirmación (`01-correo-confirmacion`) | `fig:correo-confirmacion` | **05-evaluacion.tex** (cap. 5) | **cap. 5** | ✅ Coinciden |
| Actions verde (`02-actions-verde`) | `fig:actions-verde` | **05-evaluacion.tex** (cap. 5) | **cap. 5** | ✅ Coinciden |
| Google publicada (`03-google-publicada`) | `fig:google-publicada` | **05-evaluacion.tex** (cap. 5) | **cap. 5** | ✅ Coinciden |
| Prueba técnica permitido (`01-dominio-permitido`) | `fig:prueba-tecnica-permitido` | **05-evaluacion.tex** (cap. 5) | **cap. 5** (label `fig:prueba-tecnica`) | ⚠️ **Label distinto** |
| Verificación producción (nuevo en Nota B) | `fig:produccion-verificacion` | — | **cap. 5** | Solo en Nota B |

> **Nota:** El anexo Material (`a2-material.tex`) solo lista las figuras con `\ref`, no las incluye.

---

## Distribución canónica resumida (versión 4 / Nota B)
- **Capturas DoneTonic Sprint 1** (tablero S1, gráficas S1, backlog) → solo en **cap:propuesta** (Capítulo 3)  
  Figuras: `\ref{fig:donetonic-tablero}`, `\ref{fig:donetonic-graficas-s1}`, `\ref{fig:donetonic-backlog}`.
- **Capturas DoneTonic Sprint 2** (tablero S2, gráficas S2, detalle PBI, tareas) → solo en **anx:desarrollo** (Anexo A)  
  Figuras: `\ref{fig:donetonic-s2-tablero}`, `\ref{fig:donetonic-s2-graficas}`, `\ref{fig:donetonic-s2-detalle}`.
- **Capturas producción** (correo, actions, google) → solo en **cap:evaluacion** (Capítulo 5)  
  Figuras: `\ref{fig:correo-confirmacion}`, `\ref{fig:actions-verde}`, `\ref{fig:google-publicada}`.  
  En Capítulo 4 (Descripción) se citan con `\ref{fig:actions-verde}`, etc.
- **Capturas app/ y hito4/** → solo en **cap:descripcion** (Capítulo 4, sección «La aplicación»).
- **Capturas juego/** → solo en **cap:juego** (Capítulo 4b, sección «Cómo se juega»).
- **Capturas fase7/** → solo en **cap:juego** (Capítulo 4b) si se usan, **o en anexo** si son comparativas antes/después.
- **Capturas prueba-tecnica/** → solo en **cap:evaluacion** (Capítulo 5)  
  Figura: `\ref{fig:prueba-tecnica}`.

---

## Ampliaciones cronológicas

### 2026-11-16 (memoria-procesos) — Desde Nota A
1. **Regla 10 de Javier:** ninguna imagen se repite en el PDF. Se elige capítulo canónico donde la imagen tiene más sentido (donde se explica por primera vez). En los demás capítulos se sustituye la inclusión por `\ref{fig:...}` y, si es necesario, breve mención. Evita duplicados y mantiene el PDF ligero.
2. **Solución práctica:** elegir capítulo canónico por captura y usar `\ref{fig:etiqueta-canónica}` en el resto. En este proyecto:  
   - Tablero Sprint 1 → Cap. 3 (`03-propuesta.tex`, `fig:donetonic-tablero`)  
   - Tablero Sprint 2 → Anexo Desarrollo (`a1-desarrollo.tex`, `fig:donetonic-s2-tablero`)  
   - Backlog → Anexo Desarrollo (`fig:donetonic-backlog`)  
   - Gráficas Sprint 1 → Anexo Desarrollo (`fig:donetonic-graficas-s1`)  
   - Gráficas Sprint 2 → Anexo Desarrollo (`fig:donetonic-s2-graficas`)  
   - El anexo Material (`a2-material.tex`) solo lista con `\ref`.
3. **Decisión de Javier:** capturas de producción, prueba técnica y DoneTonic salen en varios capítulos. Cada una va una sola vez donde más sentido tiene; en el resto se cita con `\ref`.  
   - `app/` y `hito4/` → Cap. 4 (Descripción)  
   - `juego/` → Cap. 4b (Juego)  
   - `donetonic/` → Anexo A1 (Desarrollo) y Cap. 3 (Propuesta)  
   - `produccion/` y `prueba-tecnica/` → Cap. 5 (Evaluación)

### 2026-11-20 (memoria-procesos) — Desde Nota B
- Lista de capturas y ubicación canónica (ver tabla consolidada arriba).
- Inventario de capturas por carpeta (ver tabla arriba).
- Relacionado: *Prosa de TFG sin cadenas «La figura X muestra…» (Regla 13 Javier)*, *Capturas agrupadas en subfigure*.

---

## Verificación automática (Nota B)
- `verificar.py` comprueba mínimos por carpeta.
- `revisar_maquetacion.py` **no** detecta duplicados — el revisor debe confirmar visualmente en el PDF.

---

## Procedimiento de verificación manual
```bash
# Buscar todas las inclusiones de imágenes en capítulos
grep -r "includegraphics" chapters/
```
- Cada archivo de imagen debe aparecer **una sola vez** en la salida.
- Reemplazar el resto por `\ref{fig:etiqueta-original}`.

---

## Ejemplos de cita cruzada (Nota B)
- En `04-descripcion.tex`: «El despliegue en Google Cloud Run se validó… (Figura~\ref{fig:correo-confirmacion}, Capítulo~\ref{cap:evaluacion})».
- En texto: «el tablero del Sprint 1 (Figura~\ref{fig:donetonic-tablero})» en lugar de volver a incluir la imagen.

---

## Enlaces relacionados
- `[[cada-imagen-aparece-una-sola-vez-en-el-capitulo-canonico]]`
- `[[una-imagen-en-un-solo-sitio-y-en-el-resto-una-referencia]]`
- `[[sin-figuras-repetidas-usar-ref-a-la-figura-existente]]`
- `[[cada-imagen-aparece-una-sola-vez-en-el-capitulo-canonico]]`
- `[[como-centralizar-capturas-duplicadas-entre-capitulos-en-late]]`
- `[[inventario-de-capturas-donetonic-requeridas-y-disponibles]]`

**Origen:** `[[proyectos/memoria-procesos/estado|memoria-procesos]]`

> 10. **Sin figuras repetidas:** cada imagen aparece una sola vez. Si hace falta en otro sitio, se pone `\ref` a la figura que ya existe.
> — `memoria/reglas-tfg.md`

Fusionada con: *Imágenes repetidas — una sola aparición + \ref en el resto*  
Relacionado: `[[sin-figuras-repetidas-usar-ref-a-la-figura-existente]]`
<<<CONTRADICCION>>
1. **Gráficas Sprint 1 (`fig:donetonic-graficas-s1`)**: Nota A → Anexo A1; Nota B (v4) → Cap. 3.  
2. **Backlog (`fig:donetonic-backlog`)**: Nota A → Anexo A1; Nota B (v4) → Cap. 3.  
3. **Prueba técnica**: Nota A usa label `fig:prueba-tecnica-permitido`; Nota B usa `fig:prueba-tecnica` (ambos en Cap. 5).  
4. **Capturas exclusivas de Nota B**: `fig:donetonic-s2-detalle` (Anexo A1) y `fig:produccion-verificacion` (Cap. 5) no aparecen en Nota A.  
5. **Advertencia interna de Nota A invertida**: la nota A incluye un aviso que dice «Nota A sitúa Backlog en Cap. 3 y Nota B en Anexo A1», pero la tabla principal de Nota A sitúa Backlog en Anexo A1; el aviso está invertido respecto al contenido real de la nota.

> 10. **Sin figuras repetidas:** cada imagen aparece una sola vez. Si hace falta en otro sitio, se pone `\ref` a la figura que ya existe.
> — `memoria/reglas-tfg.md`
> Sin figuras repetidas: cada imagen aparece una sola vez. Si hace falta en otro sitio, se pone \ref a la figura que ya existe.
> — `memoria/reglas-tfg.md`
> **Sin figuras repetidas: cada imagen aparece una sola vez. Si hace falta en otro sitio, se pone \ref a la figura que ya existe.**  
> — `memoria/reglas-tfg.md` (regla 10 y spec versión 4)
> Sin figuras repetidas: cada imagen aparece una sola vez. Si hace falta en otro sitio, se pone \ref a la figura que ya existe.
> — `memoria/reglas-tfg.md regla 10 y spec versión 4`

Fusionada con: Imágenes repetidas: una sola aparición y \ref en el resto

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
