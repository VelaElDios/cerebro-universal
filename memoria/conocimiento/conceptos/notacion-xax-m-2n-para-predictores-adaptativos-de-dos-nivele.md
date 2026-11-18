---
tipo: "concepto"
titulo: "Notación XAx(m,2n) para predictores adaptativos de dos niveles (Yeh y Patt 1992)"
temas: ["ac", "prediccion-saltos", "yeh-patt"]
claves: ["XAx(m", "2n)", "BHR", "BHT", "historia global", "historia local"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[prediccion-saltos]] · [[yeh-patt]]

La notación XAx(m,2n) define tres dimensiones:
- X (historia): G = un BHR global compartido; P = un BHR por salto (local); S = un BHR por conjunto de saltos indexado por n bits bajos del PC.
- x (organización BHT): g = una BHT global; p = una BHT por salto; s = una BHT por conjunto seleccionada con n bits bajos del PC.
- m = bits del registro de desplazamiento BHR (ancho de historia).
- 2n = entradas de cada BHT (todas de 2 bits según Yeh y Patt).
Ejemplo Gas(4,22): un BHR global de 4 bits indexa una BHT seleccionada por los 2 bits bajos del PC.

> Notación: XAx(m,2n) X (forma de recoger historia global): G (un único BHR global), P (un BHR por cada salto) o S (un BHR por cada conjunto de saltos, indexada por los n bits menos significativos de la dirección de la instrucción de salto)
> — `repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4.pdf` (cita sin comprobar)

Relacionado: [[ejemplo-gas-4-22-predictor-dos-niveles]] · [[yeh-y-patt-recomiendan-g-g-para-enteros-y-s-s-para-coma-flot]] · [[predictor-correlacionado-o-de-dos-niveles-m-n-correlacion-es]]
