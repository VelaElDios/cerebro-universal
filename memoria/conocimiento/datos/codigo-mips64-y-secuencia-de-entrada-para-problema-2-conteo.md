---
tipo: "dato"
titulo: "Código MIPS64 y secuencia de entrada para Problema 2 (Conteo ceros y pares)"
temas: ["ac", "branch-prediction", "mips64", "prediccion-saltos"]
claves: ["LW", "BNEZ", "DADDUI", "ANDI", "secuencia 0 1 0 2 0 3", "R1=6", "R2 base", "R4 ceros", "R5 pares"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2025.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[branch-prediction]] · [[mips64]] · [[prediccion-saltos]]

Bucle de 6 iteraciones (R1=6). Secuencia de datos: [0, 1, 0, 2, 0, 3]. Etiquetas de saltos: B1 (salto si no cero), B2 (salto si impar), B3 (salto de bucle). R3 carga valor, R4 cuenta ceros, R5 cuenta pares (incluye cero). ANDI R3, R3, #1 extrae LSB (paridad).

> El siguiente código MIPS64 cuenta (en R4 y en R5) el número de ceros y de números pares (considerando que el 0 es par) en una secuencia almacenada en memoria a partir de la dirección R2. bucle: LW R3, 0(R2); BNEZ R3, nocero ; (B1); DADDUI R4, R4, #1; nocero: ANDI R3, R3, #1; BNEZ R3, impar ; (B2); DADDUI R5, R5, #1; impar: DADDUI R2, R2, #4; DADDUI R1, R1, #-1; BNEZ R1, bucle ; (B3)
> — `repo:datos/temarios/AC/examenes/Enero2025.pdf` (cita sin comprobar)

Relacionado: [[secuencia-de-datos-y-codigo-mips64-para-ejercicio-2-de-predi]] · [[ejercicio-2-analisis-de-prediccion-de-saltos-en-bucle-contad]] · [[etiquetado-de-saltos-b1-b2-b3-en-bucle-contador-ceros-pares]]
