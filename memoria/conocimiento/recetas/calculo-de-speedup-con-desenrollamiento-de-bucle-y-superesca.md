---
tipo: "receta"
titulo: "Cálculo de speedup con desenrollamiento de bucle y superescalar"
temas: ["ac", "desenrollamiento", "speedup", "superscalar"]
claves: ["speedup", "desenrollamiento bucle", "superescalar", "ciclos por iteración"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2025.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[desenrollamiento]] · [[speedup]] · [[superscalar]]

Original: 30 iteraciones × 10 ciclos/iter = 300 ciclos. Desenrollado 3×: 10 iteraciones del bucle grande × 15 ciclos = 150 ciclos. Speedup = 300/150 = 2. Opción correcta: c. 2.

> Se ejecuta un código MIPS64 que itera un código 30 veces y emplea 300 ciclos de reloj al ejecutarse en un procesador escalar. Desenrollamos el bucle 3 veces y lo planificamos para un superescalar de grado 4. Cada iteración del bucle modificado requiere 15 ciclos en el superescalar. Hemos obtenido un speedup de:
> — `repo:datos/temarios/AC/examenes/Junio2025.pdf`

Relacionado: [[algoritmo-tomasulo-origen-y-objetivo-cpi1]] · [[analisis-de-dependencias-en-bucle-con-add-d-y-s-d-misma-iter]]
