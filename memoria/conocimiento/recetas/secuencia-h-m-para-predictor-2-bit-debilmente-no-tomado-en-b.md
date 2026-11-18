---
tipo: "receta"
titulo: "Secuencia H/M para predictor 2-bit débilmente no tomado en bucle de 5 iteraciones (pregunta 11)"
temas: ["ac", "correlacion", "prediccion-saltos", "predictor-2-bit"]
claves: ["2-bit predictor", "weakly not taken", "BNEZ", "bucle 5 iteraciones", "HMMMM", "MHHHM", "MHHHH", "MMHHM"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2022.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[correlacion]] · [[prediccion-saltos]] · [[predictor-2-bit]]

Estados 2-bit: 00=strong NT, 01=weak NT, 10=weak T, 11=strong T. Inicial weak NT (01). Bucle 5 iteraciones: 4 tomados (T), 1 no tomado (NT final). Iter1: pred NT (01), real T → Miss, estado→10. Iter2: pred T (10), real T → Hit, estado→11. Iter3: pred T (11), real T → Hit, estado→11. Iter4: pred T (11), real T → Hit, estado→11. Iter5: pred T (11), real NT → Miss, estado→10. Secuencia: MHHHM (opción b).

> Indicate the sequence of Hits (H) and Misses (M) for branch B1 using a one level 2-bit predictor initialized to weakly not taken.
> — `repo:datos/temarios/AC/examenes/June2022.pdf`

Relacionado: [[bht-con-contadores-de-saturacion-de-2-bits-pregunta-17]]
