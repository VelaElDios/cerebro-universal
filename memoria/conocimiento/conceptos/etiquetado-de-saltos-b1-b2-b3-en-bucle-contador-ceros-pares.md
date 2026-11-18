---
tipo: "concepto"
titulo: "Etiquetado de saltos B1, B2, B3 en bucle contador ceros/pares"
temas: ["ac", "mips64", "prediccion-saltos"]
claves: ["B1 BNEZ R3 nozero", "B2 BNEZ R3 odd", "B3 BNEZ R1 loop"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January 2025.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[mips64]] · [[prediccion-saltos]]

Los tres saltos condicionales del bucle se etiquetan en el enunciado como B1, B2, B3 para la tabla de predicción: B1 es el salto tras la carga (BNEZ R3, nozero) que salta si R3!=0 (es decir, si no es cero); B2 es el salto tras ANDI (BNEZ R3, odd) que salta si el bit menos significativo es 1 (impar); B3 es el salto de fin de bucle (BNEZ R1, loop) que salta si R1!=0. El orden de ejecución en cada iteración es B1, B2, B3.

> BNEZ   R3, nozero             ; (B1) ... BNEZ   R3, odd                ; (B2) ... BNEZ   R1, loop               ; (B3)
> — `repo:datos/temarios/AC/examenes/January 2025.pdf` (cita sin comprobar)

Relacionado: [[ejercicio-2-analisis-de-prediccion-de-saltos-en-bucle-contad]] · [[secuencia-de-datos-y-codigo-mips64-para-ejercicio-2-de-predi]] · [[patron-de-saltos-en-bucle-mips64-secuencia-0-1-0-2-examen-en]]
