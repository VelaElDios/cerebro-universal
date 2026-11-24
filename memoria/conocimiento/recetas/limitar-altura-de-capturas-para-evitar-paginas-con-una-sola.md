---
tipo: "receta"
titulo: "Evitar páginas con una sola imagen (Regla 8): capturas y diagramas en LaTeX"
temas: ["adjustbox", "capturas", "figuras", "latex", "maquetacion", "maquetación", "reglas-tfg"]
claves: ["regla 8", "página sola imagen", "height", "subfigure", "adjustbox", "max totalheight", "0.42\\textheight"]
proyectos: ["memoria-procesos"]
fuentes: ["memoria/reglas-tfg.md"]
confianza: "propuesto"
fecha: "2026-11-19"
actualizado: "2026-11-22"
---

Temas: [[adjustbox]] · [[capturas]] · [[figuras]] · [[latex]] · [[maquetacion]] · [[maquetación]] · [[reglas-tfg]]

Temas: [[latex]] · [[maquetacion]] · [[reglas-tfg]] · [[figuras]]

**Regla 8**: Ninguna página del PDF debe tener una sola imagen ocupando toda la página. Las figuras deben compartir página con texto u otras figuras.

---

## 1. Parámetros de flotantes relajados (preámbulo / `include/extra.tex`)
Ya configurados en el proyecto:
```latex
\renewcommand{\topfraction}{0.85}
\renewcommand{\bottomfraction}{0.6}
\renewcommand{\textfraction}{0.12}
\renewcommand{\floatpagefraction}{0.8}
\setcounter{topnumber}{3}
\setcounter{totalnumber}{4}
```

---

## 2. Capturas (archivos PNG: gráficas DoneTonic, CI/CD, móviles, etc.)

### 2.1 Opción principal: `adjustbox` con `max totalheight`
Para capturas altas que ocupan casi una página entera, envolver en `adjustbox` **en lugar de** solo `height=...,keepaspectratio` en `\includegraphics`. Esto garantiza que la figura comparta página con texto.

```latex
\begin{figure}[htbp]
\centering
\adjustbox{max totalheight=0.42\textheight,width=0.85\textwidth}{%
  \includegraphics{figs/capturas/...}%
}
\caption{...}\label{...}
\end{figure}
```

### 2.2 Valores concretos por tipo de captura
| Tipo | `\includegraphics` / `adjustbox` |
|------|----------------------------------|
| **Verticales (móvil)** | `width=0.35\textwidth, height=0.42\textheight, keepaspectratio` |
| **Horizontales** | `width=0.9\textwidth, height=0.42\textheight, keepaspectratio` |
| **En `subfigure` (dos por fila)** | `width=\linewidth, height=0.35\textheight, keepaspectratio` |
| **Fallback si queda sola en página** | Envolver en `\adjustbox{max totalheight=0.42\textheight,width=...}{\includegraphics{...}}` |

> **Nota**: El borrador original usaba `height=0.72\textheight`; hay que bajarlo a `0.42\textheight` como máximo.

### 2.3 Capturas identificadas que necesitan `adjustbox`
- `figs/capturas/donetonic/06-graficas-sprint2.png` (en `a1-desarrollo.tex`, Figura~\ref{fig:donetonic-s2-graficas})
- `figs/capturas/produccion/02-actions-verde.png` (en `05-evaluacion.tex`, Figura~\ref{fig:actions-verde})

---

## 3. Diagramas TikZ / pgfplots / pgf-umlsd grandes
Envolver en entorno `adjustbox`:
```latex
\begin{adjustbox}{max width=\linewidth, max totalheight=0.6\textheight}
  ... código TikZ/pgfplots ...
\end{adjustbox}
```
- Dentro, usar `\resizebox{\textwidth}{!}{...}` **solo si es necesario**.
- **Si las letras quedan < 8 pt tras escalar**: rediseñar el diagrama (menos participantes, más espacio, dividir en dos).

---

## 4. Agrupar capturas relacionadas en `subfigure`
- Poner dos capturas por fila (`subfigure` + `subcaption`).
- Altura por subfigura: `height=0.35\textheight, keepaspectratio`.
- Así el grupo ocupa menos alto y facilita que LaTeX lo mezcle con texto.

---

## 5. Texto explicativo y ubicación `[htbp]`
- **Siempre** usar `[htbp]` en el entorno `figure`.
- Añadir texto explicativo **antes y/o después** de la figura para que la página no quede solo con la imagen.
- Si una sección queda muy corta, **fusionarla con la anterior** o **convertirla en lista**.

---

## 6. Resumen de límites de altura
| Elemento | Límite de altura |
|----------|------------------|
| Capturas (PNG) | `0.42\textheight` (con `max totalheight` en `adjustbox`) |
| Diagramas TikZ/pgfplots grandes | `0.6\textheight` (con `max totalheight` en `adjustbox`) |

---

> **Cita de `memoria/reglas-tfg.md`**  
> - capturas como mucho a `height=0.42\textheight`;  
> - diagramas grandes con `max totalheight`;  
> - figuras `[htbp]` con los parámetros de flotantes relajados, para que compartan página con el texto u otra figura.

---

## Referencias cruzadas
- [[limitar-altura-de-capturas-para-evitar-paginas-con-una-sola]]
- [[figuras-que-comparten-pagina-con-el-texto-parametros-de-flot]]
- [[figuras-ninguna-pagina-con-una-sola-imagen-limites-de-altura]]
- [[limitar-altura-de-capturas-para-evitar-paginas-con-una-sola]]
- [[como-evitar-paginas-con-una-sola-imagen-regla-8-de-javier]]
- [[arreglar-pagina-con-una-sola-imagen-regla-8-agrupando-en-sub]]

Relacionado: [[figuras-sin-paginas-solas-ni-casi-vacias-limites-de-altura-y]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]

> Regla 8: Ninguna página con una sola imagen: capturas como mucho a `height=0.42\textheight`; diagramas grandes con `max totalheight`; figuras `[htbp]` con parámetros de flotantes relajados.
> — `memoria/reglas-tfg.md` (cita sin comprobar)
> - capturas como mucho a `height=0.42\textheight`; - diagramas grandes con `max totalheight`; - figuras `[htbp]` con los parámetros de flotantes relajados, para que compartan página con el texto u otra figura.
> — `memoria/reglas-tfg.md`


> ⚠️ Posible contradicción al fusionar: - Nota A propone `height=0.42\textheight,keepaspectratio` directamente en `\includegraphics`; Nota B recomienda `adjustbox{max totalheight=0.42\textheight,width=...}` como método principal para capturas altas.
- Nota A usa `max width=\textwidth` para diagramas TikZ; Nota B usa `max width=\linewidth`.
- Nota A menciona que el borrador actual tiene `height=0.72\textheight`; Nota B no lo menciona.
- Nota A sugiere fusionar secciones cortas o convertirlas en lista (Ampliación 2, punto 6); Nota B no lo contempla.
- Las ampliaciones de Nota A son de 2026-11-16; las de Nota B son de 2026-11-19 (versión más reciente y verificada).

Fusionada con: Corregir páginas con una sola imagen (Regla 8)

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
