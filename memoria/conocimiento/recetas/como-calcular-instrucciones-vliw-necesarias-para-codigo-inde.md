---
tipo: "receta"
titulo: "Cómo calcular instrucciones VLIW necesarias para código independiente"
temas: ["ac", "empaquetado", "planificacion-estatica", "vliw"]
claves: ["VLIW", "instrucción larga", "operaciones por ciclo", "eficiencia máxima", "NOP"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2025.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[empaquetado]] · [[planificacion-estatica]] · [[vliw]]

40 operaciones independientes, ancho VLIW = 6 ops/ciclo. Con eficiencia máxima (sin huecos innecesarios), se necesitan ceil(40/6) = 7 palabras VLIW (instrucciones largas). La última contendrá 4 ops útiles + 2 NOP. Opción correcta: b. «El código a ejecutar por el VLIW estará formado por 7 instrucciones largas.»

> Nos han facilitado un código formado con 40 instrucciones independientes que se quiere planificar para su ejecución en un procesador VLIW. Sabiendo que el procesador VLIW es capaz de emitir 6 operaciones por ciclo y que obtiene una eficiencia máxima indica cuál es la respuesta correcta:
> — `repo:datos/temarios/AC/examenes/Junio2025.pdf`

Relacionado: [[planificacion-estatica-el-compilador-reordena-para-reducir-d]] · [[analisis-de-dependencias-en-bucle-con-add-d-y-s-d-misma-iter]] · [[calculo-de-numero-minimo-de-instrucciones-largas-en-vliw-dad]] · [[caracteristicas-clave-de-procesadores-vliw]] · [[calculo-de-operaciones-por-ciclo-ipc-en-planificacion-vliw-d]]
