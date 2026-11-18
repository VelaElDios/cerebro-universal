---
tipo: "receta"
titulo: "Análisis de predicción de saltos en bucle con dos saltos condicionales (B1: BEQZ, B2: BEQ)"
temas: ["ac", "pipeline", "prediccion-saltos"]
claves: ["BEQZ", "BEQ", "predictor 1 bit", "predictor 3 bits", "predictor correlacionado (2", "1)", "BHT"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2015.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]] · [[prediccion-saltos]]

El bucle recorre un array en memoria (direcciones 0x1000, 0x1004, ...). B1 (BEQZ R4, next) se toma cuando el valor cargado es 0; B2 (BEQ R1, R2, fin) se toma cuando el puntero R1 alcanza el límite R2. Para resolver: 1) Determinar la secuencia real de tomados/no tomados para B1 y B2 iteración a iteración usando los valores de memoria dados (0x1000=1, 0x1004=0, 0x1008=2, 0x100C=0, 0x1010=0, 0x1014=3, 0x1018=0, 0x101C=0, 0x1020=0, 0x1024=4). 2) Simular predictor de 1 bit inicializado a "tomado" (estado T) para cada salto: actualizar tras cada ejecución, contar aciertos. 3) Simular predictor de 3 bits (contador saturación 3 bits) inicializado a 011 (débilmente tomado) para cada salto. 4) Para predictor correlacionado (2,1): usar historia global de 2 saltos previos (ambos no tomados) para indexar una BHT de 4 entradas, cada una con predictor de 1 bit inicializado a "no tomado fuerte" (00). Actualizar historia y BHT tras cada salto.

> a) ¿Cuál será el sentido real de los saltos B1 y B2 durante el recorrido de la secuencia?
> — `repo:datos/temarios/AC/examenes/Junio2015.pdf`

Relacionado: [[alternativas-de-deteccion-de-instruccion-de-salto-en-pipelin]] · [[bht-con-contadores-de-saturacion-de-2-bits-pregunta-17]] · [[bht-en-predictor-dinamico-de-3-bits-contadores-de-saturacion]]
