---
tipo: "concepto"
titulo: "Predictor correlacionado (2,1) - estructura y funcionamiento"
temas: ["ac", "correlating-predictor", "prediccion-saltos"]
claves: ["BHR", "BHT", "(2", "1)", "historia global", "predictor 1 bit"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2018.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[correlating-predictor]] · [[prediccion-saltos]]

Predictor correlacionado (m,n): usa m bits de historia global (BHR) para indexar una tabla de predictores (BHT) de n bits cada uno.
- (2,1) significa: BHR de 2 bits → 4 entradas en BHT; cada entrada es un predictor de 1 bit (0=No tomado, 1=Tomado).
- Estado inicial: BHR=00, todas las entradas BHT=0 (No tomado).
- En cada salto:
  1. Se usa BHR actual como índice para leer predicción de BHT[BHR].
  2. Se compara con comportamiento real → Acierto/Fallo.
  3. Se actualiza BHT[BHR] con comportamiento real (1 bit: se sobrescribe).
  4. Se actualiza BHR: shift left + insertar comportamiento real (T=1, N=0).
- Dos saltos (B1 y B2) comparten el mismo BHR y BHT (historia global única).
- Tabla de seguimiento típica: Salto Ejecutado | Comp. Real | Predicción | BHR (estado) | BHTs | Acierto/Fallo.

> se usa un predictor correlacionado (2,1) para predecir el comportamiento de los saltos y que en memoria se ha almacenado la cadena "exam18
> — `repo:datos/temarios/AC/examenes/Enero2018.pdf`

Relacionado: [[bht-branch-history-table-tabla-separada-para-bits-de-predicc]] · [[btb-branch-target-buffer-fusion-de-btac-y-bits-de-prediccion]]
