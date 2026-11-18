---
tipo: "receta"
titulo: "Desenrollar bucle 2x y planificar para latencias FP dadas (Ejercicio 1)"
temas: ["ac", "desenrollamiento", "pipeline-flotante", "planificacion-estatica"]
claves: ["fmul.d 4 ciclos", "fadd.d 2 ciclos", "fdiv.d 16 ciclos", "desenrollar 2 veces", "latencia etapa EX"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3_Prob.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[desenrollamiento]] · [[pipeline-flotante]] · [[planificacion-estatica]]

El bucle original carga f2, multiplica f4=f2*f0, carga f6, suma f6=f4+f6, almacena f6, actualiza punteros x1/x2 -8, compara y salta. Desenrollar 2 veces significa replicar el cuerpo dos veces ajustando registros (p.ej. f2,f4,f6 para primera iteración; f10,f12,f14 para segunda) y desplazamientos de memoria (0, -8, -16). Planificar reordenando instrucciones para ocultar latencias: intercalar cargas, multiplicaciones, sumas y stores de ambas iteraciones de modo que cuando una instrucción necesita el resultado de otra, ya esté listo (respetando latencias: mul 4, add 2). Ignorar retardo de salto y asumir predicción correcta. El objetivo es minimizar ciclos por iteración original (CPI).

> Considera una segmentación de punto flotante en la que la duración de la etapa EX de la multiplicación en PF es 4 ciclos, la de la suma en PF es 2 ciclos, la de la división en PF es 16 ciclos y la del resto es un ciclo.
> — `repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3_Prob.pdf`

Relacionado: [[desenrollar-bucle-minimo-para-planificar-sin-detenciones-eje]] · [[desenrollado-4x-y-planificacion-minima-para-bucle-fp-con-lat]] · [[desenrollar-bucle-para-eliminar-dependencias-y-maximizar-ilp]]
