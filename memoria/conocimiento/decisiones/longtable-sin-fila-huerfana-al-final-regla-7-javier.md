---
tipo: "decision"
titulo: "Longtable sin fila huérfana al final: usar \\\\* en las últimas 2-3 filas antes de \\bottomrule (regla 7 Javier)"
temas: ["latex", "longtable", "maquetacion", "reglas-javier", "tablas"]
claves: ["\\\\*", "\\bottomrule", "fila huérfana", "longtable", "regla 7"]
proyectos: ["memoria-procesos"]
fuentes: ["memoria/reglas-tfg.md", "memoria/reglas-tfg.md (regla 7)"]
confianza: "verificado"
fecha: "2026-11-19"
actualizado: "2026-11-21"
---

Temas: [[latex]] · [[longtable]] · [[maquetacion]] · [[reglas-javier]] · [[tablas]]

Temas: [[latex]] · [[longtable]] · [[maquetacion]] · [[reglas-javier]]

**Regla principal**  
En cada `longtable`, la penúltima y última fila de datos (incluyendo la fila de totales si existe) —en general, las **últimas 2-3 filas** antes de `\bottomrule`— deben terminar con `\\*` en lugar de `\\` para evitar que la última fila quede huérfana en la página siguiente. El constructor debe revisar **TODAS** las longtables del documento (capítulos y anexos) y añadir `\\*` en esas filas. Verificar en el PDF compilado que no hay filas solas al inicio de página.

> Las tablas largas van en longtable y su última fila (por ejemplo, el Total) no se queda sola en otra página: usa \\* en las últimas filas.  
> — `memoria/reglas-tfg.md`

**Archivos a revisar / aplicar**  
- `chapters/04-descripcion.tex` (tablas RF, RJ, RNF, módulos, API)  
- `chapters/04b-juego.tex` (sistemas, logros, fases)  
- `chapters/05-evaluacion.tex` (pruebas, workflows, métricas)  
- `chapters/a1-desarrollo.tex` (backlogs, trazabilidad, problemas, evolución)  
- `chapters/a4-trazabilidad.tex` (tabla completa)  
*(Equivalente a: todas las longtables de la memoria —capítulos 4, 4b, 5, anexos A1, A4—)*

---

### Ejemplo base (3 columnas)
```latex
\begin{longtable}{@{}L{3cm} L{5cm} L{4cm}@{}}
\caption{Tabla larga.}\label{tab:ejemplo}\\
\toprule
\textbf{Col1} & \textbf{Col2} & \textbf{Col3} \\ \midrule \endfirsthead
\toprule
\textbf{Col1} & \textbf{Col2} & \textbf{Col3} \\ \midrule \endhead
Fila 1 & Dato & Dato \\
Fila 2 & Dato & Dato \\*
Fila 3 & Dato & Dato \\*
\bottomrule
\end{longtable}
```

### Ejemplo con 2 columnas (versión compacta)
```latex
\begin{longtable}{@{}L{3cm} L{10cm}@{}}
\caption{Tabla larga.}\label{tab:ejemplo}\\
\toprule
\textbf{Col1} & \textbf{Col2} \\ \midrule \endfirsthead
\toprule
\textbf{Col1} & \textbf{Col2} \\ \midrule \endhead
Dato 1 & Descripción 1 \\
Dato 2 & Descripción 2 \\*
Dato 3 & Descripción 3 \\*
\bottomrule
\end{longtable}
```

### Esquema genérico (penúltima y última fila con \\*)
```latex
\begin{longtable}{...}
\caption{...}\label{...}\\
\toprule
... \\
\midrule
... \\*   % penúltima fila
... \\*   % última fila
\bottomrule
\end{longtable}
```

---

## Ampliaciones (memoria-procesos)

### 2026-11-19
- Añadir `\\*` antes de `\bottomrule` (o antes de la última fila de datos) para evitar que la última fila quede sola en la siguiente página.  
- Usar `\\*` en las **2-3 últimas filas** antes de `\bottomrule`.  
- Aplicar a **TODAS** las longtables de la memoria (capítulos 4, 4b, 5, anexos A1, A4).

### 2026-11-20
- En cada longtable, las últimas 2-3 filas deben terminar con `\\*` en lugar de `\\`.  
- Ejemplo concreto: fila P18 `\\*`, fila P19 `\\*`, luego `\bottomrule`.  
- Esto evita que LaTeX parta la tabla dejando la última fila sola en la siguiente página.

---

## Enlaces relacionados
- [[longtable-sin-fila-huerfana-al-final-regla-7-javier]]
- [[longtable-sin-fila-huerfana-al-final]]
- [[longtable-sin-fila-huerfana-al-final-regla-7-javier]]
- [[tablas-largas-en-longtable-con-ultima-fila-acompanada]]
- [[como-anadir-en-longtables-para-evitar-filas-huerfanas]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]

> Las tablas largas van en longtable y su última fila (por ejemplo, el Total) no se queda sola en otra página: usa \\* en las últimas filas.
> — `memoria/reglas-tfg.md`

Fusionada con: Longtables deben terminar con \\* antes de \bottomrule (regla 7 Javier)

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
