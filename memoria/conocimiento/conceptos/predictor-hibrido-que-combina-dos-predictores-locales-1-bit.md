---
tipo: "concepto"
titulo: "Predictor híbrido que combina dos predictores locales (1 bit y 3 bits) con selector de 2 bits y reglas de actualización específicas"
temas: ["ac", "actualizacion-selector", "prediccion-saltos", "predictor-hibrido", "predictor-local", "selector-contador"]
claves: ["Predictor 1 (1 bit por salto)", "Predictor 2 (3 bits por salto)", "Contadores selector 2 bits por salto", "regla actualización: Acierto/Acierto->no cambia", "Acierto/Fallo->inc", "Fallo/Acerto->dec", "Fallo/Fallo->no cambia", "MSB selector 1->P1", "0->P2"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4_Prob.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[actualizacion-selector]] · [[prediccion-saltos]] · [[predictor-hibrido]] · [[predictor-local]] · [[selector-contador]]

Mismo bucle RISC-V que ejercicio 7 (secuencia 0,1,0,2,0,3,0,4,0,5). Estado inicial: Contadores B1=00, B2=00 (MSB=0 -> usa Predictor 2). Predictor 1: B1=0 (NT), B2=0 (NT). Predictor 2: B1=000 (NT fuerte), B2=000 (NT fuerte). Simular 10 iteraciones (10 ejecuciones de B1 y B2 cada una). En cada salto: 1) Leer selector MSB -> elegir P1 o P2. 2) Predecir con elegido. 3) Comparar con real (tabla ejercicio 7). 4) Actualizar P1 y P2 con real. 5) Actualizar selector según tabla de 4 casos. Rellenar tabla de seguimiento.

> Detalla el comportamiento de un predictor híbrido que combina dos predictores locales (llamados “Predictor 1” y “Predictor 2”). El Predictor 1 asocia un predictor de 1 bit a cada instrucción de salto (B1 y B2), mientras que el Predictor 2 asocia un predictor de 3 bits a cada salto. Para seleccionar el predictor a emplear hay una tabla (llamada “Contadores”) que almacena un contador saturado de 2 bits para cada salto. Si el bit más significativo del contador es 1 se emplea el Predictor 1, mientras que si es 0 se emplea el Predictor 2. Tras cada predicción, además de actualizar ambos predictores, el contador correspondiente debe ser actualizado según la tabla siguiente...
> — `repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4_Prob.pdf` (cita sin comprobar)

Relacionado: [[bht-branch-history-table-tabla-separada-para-bits-de-predicc]] · [[alternativas-de-deteccion-de-instruccion-de-salto-en-pipelin]]
