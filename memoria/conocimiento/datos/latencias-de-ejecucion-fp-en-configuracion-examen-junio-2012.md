---
tipo: "dato"
titulo: "Latencias de ejecución FP en configuración examen Junio 2012"
temas: ["ac", "pipeline", "tomasulo"]
claves: ["latencia FP", "ADD.D 2 ciclos", "MUL.D 6 ciclos", "DIV.D 12 ciclos", "load/store 2 ciclos"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2012.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]] · [[tomasulo]]

Tabla de latencias de ejecución (ciclos en etapa EX) para el ejercicio:
- L.D / S.D (buffer carga/almacenamiento): 2 ciclos
- ADD.D / SUB.D (sumador/restador): 2 ciclos
- MUL.D (multiplicador): 6 ciclos
- DIV.D (divisor): 12 ciclos
Nota: "cantidad" en la tabla del enunciado se refiere al número de unidades funcionales, no a ciclos. Los ciclos son la columna "Ciclos".

> Sumador/Restador 2 cantidad 2 ciclos / Multiplicador 2 cantidad 6 ciclos / Divisor 1 cantidad 12 ciclos / La etapa de ejecución de ambas operaciones requiere 2 ciclos
> — `repo:datos/temarios/AC/examenes/Junio2012.pdf` (cita sin comprobar)

Relacionado: [[analisis-de-dependencias-en-bucle-con-add-d-y-s-d-misma-iter]] · [[bucle-vectorial-de-referencia-para-desenrollado-y-planificac]] · [[latencias-de-ejecucion-uf-fp-en-examen-ac-junio-2014-problem]] · [[latencias-de-unidades-funcionales-dadas-en-el-examen-fp-y-me]] · [[parametros-de-temporizacion-del-examen-ac-june-2022-exercise]]
