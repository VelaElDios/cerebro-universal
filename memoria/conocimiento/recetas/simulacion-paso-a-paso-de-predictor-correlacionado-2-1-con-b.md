---
tipo: "receta"
titulo: "Simulación paso a paso de predictor correlacionado (2,1) con BHR y 4 BHTs de 2-bits"
temas: ["ac", "prediccion-saltos"]
claves: ["BHR", "BHT", "predictor correlacionado", "(2", "1)", "actualización", "índice"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4_Prob.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[prediccion-saltos]]

Procedimiento para simular el predictor correlacionado (2,1) del Ejercicio 12 (y aplicable al Ejercicio 10). 1) Leer BHR actual (2 bits). 2) Usar BHR como índice para seleccionar una de las 4 BHTs (cada BHT es un predictor de 2-bits). 3) Leer predicción de esa BHT (MSB: 1=Tomado, 0=No tomado). 4) Comparar con comportamiento real → Acierto/Fallo. 5) Actualizar esa BHT según su autómata de 2-bits (00→01→11→10→00...). 6) Actualizar BHR: shift left e insertar resultado real (T=1, NT=0). 7) Repetir para siguiente salto. El BHR es global (compartido por B1 y B2).

> Considera el mismo vector de entrada del apartado a) y que el estado inicial del predictor es el mostrado en la tabla. Indica el resultad en la columna 6ª, 7ª y 8ª de la tabla de abajo. ... Bits de predicción (BHR y BTHs) ... Resultado predicción (T/NT)
> — `repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4_Prob.pdf` (cita sin comprobar)

Relacionado: [[bht-branch-history-table-tabla-separada-para-bits-de-predicc]]
