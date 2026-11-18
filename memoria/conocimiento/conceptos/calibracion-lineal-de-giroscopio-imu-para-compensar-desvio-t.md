---
tipo: "concepto"
titulo: "Calibración lineal de giroscopio IMU para compensar desvío térmico"
temas: ["ac", "procesamiento-senal", "sistemas-embebidos"]
claves: ["IMU", "calibración lineal", "gain", "offset", "firmware tiempo real"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2026.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[procesamiento-senal]] · [[sistemas-embebidos]]

El firmware de vehículos autónomos debe corregir en tiempo real las lecturas de velocidad angular del giróscopo aplicando una calibración lineal: valor_corregido = valor_original * gain + offset. Esto compensa los desvíos térmicos de la IMU que afectan a la precisión de los sensores.

> La corrección consiste en aplicar a cada muestra una calibración lineal, definida por una ganancia (gain) y un desplazamiento (offset), antes de enviar los datos al sistema de toma de decisiones.
> — `repo:datos/temarios/AC/examenes/Junio2026.pdf`

Relacionado: [[bucle-risc-v-para-calibracion-imu-con-puntero-descendente]] · [[simulacion-de-ejecucion-tomasulo-con-tabla-de-ciclos-issue-e]] · [[valores-de-ejemplo-para-cpu-del-laboratorio-frecuencia-bw-pu]]
