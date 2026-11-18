---
tipo: "dato"
titulo: "Número de tablas BHT en predictor correlacionado (m, n)"
temas: ["ac", "bht", "prediccion-saltos", "predictor-correlacionado"]
claves: ["predictor correlacionado", "tablas BHT", "historia global", "m bits", "BHT", "tablas predicción"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2026.pdf", "repo:datos/temarios/AC/examenes/Junio2018.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[bht]] · [[prediccion-saltos]] · [[predictor-correlacionado]]

Temas: [[ac]] · [[bht]] · [[prediccion-saltos]] · [[predictor-correlacionado]]

**Definición y fórmulas según fuentes**

*   **Nota A (Junio 2026):** Un predictor correlacionado **(m, n)** usa **m bits de historia global** para indexar **2^m tablas BHT** (Branch History Tables), cada una con contadores de saturación de **n bits**.
    *   Ejemplo **(3, 2)**: 2^3 = **8 tablas BHT**.
    *   Pregunta origen: `repo:datos/temarios/AC/examenes/Junio2026.pdf` → Opción correcta: "8 tablas".

*   **Nota B (Junio 2018):** Un predictor correlacionado **(m, n)** usa **m bits de historia global** y **n bits de historia local** (el orden puede variar según notación). El número de BHTs (tablas de predicción) es **2^n**, donde **n** es el número de bits de historia que indexan la tabla de patrones (historia local).
    *   Ejemplo **(3, 2)** aplicando 2^n: 2^2 = **4 BHTs** (esta opción no aparece en el examen).
    *   Interpretación académica del contexto (Junio 2018): Se asume que el primer parámetro (m=3) son bits de historia global que determinan el número de BHTs = **2^3 = 8**.
    *   Pregunta origen: `repo:datos/temarios/AC/examenes/Junio2018.pdf` → Opción esperada: **d) 8**.

**Resumen de parámetros**
*   **m**: Generalmente bits de historia global (GHR).
*   **n**: Generalmente bits de historia local / contadores de saturación / índice a tabla de patrones.
*   **Número de tablas BHT**: Discrepancia en si es **2^m** (Nota A, y conclusión práctica Nota B) o **2^n** (definición teórica inicial Nota B).

**Enlaces relacionados**
[[bht-con-contadores-de-saturacion-de-2-bits-pregunta-17]] · [[bht-en-predictor-dinamico-de-3-bits-contadores-de-saturacion]] · [[bht-branch-history-table-tabla-separada-para-bits-de-predicc]]

> ¿Cuántas tablas BHTs diferentes existen en un predictor correlacionado (3, 2)? a. 3 tablas. b. 4 tablas. c. 8 tablas. d. 9 tablas.
> — `repo:datos/temarios/AC/examenes/Junio2026.pdf`
> ¿Cuántas BHTs hay en un predictor correlacionado (3, 2)? a) 2 b) 3 c) 6 d) 8
> — `repo:datos/temarios/AC/examenes/Junio2018.pdf`


> ⚠️ Posible contradicción al fusionar: Las dos notas definen distinto qué parámetro (m o n) determina el número de tablas BHT. Nota A dice que son **2^m** (m = historia global). Nota B dice teóricamente que son **2^n** (n = historia local/índice patrón), pero admite que en el examen de Junio 2018 la respuesta esperada es 8 (2^3), contradiciendo su propia fórmula teórica inicial (que daría 4). No hay consenso en la notación (m,n) entre las fuentes.

Fusionada con: Predictor correlacionado (m,n) tiene 2^n BHTs

Relacionado: [[predictor-correlacionante-m-n-tiene-2-n-bhts]] · [[predictor-correlacionado-m-n-numero-de-bhts-2-m]] · [[calculo-de-bits-en-predictor-correlacionado-de-dos-niveles-p]]
