---
tipo: "dato"
titulo: "Parámetros temporales de pipeline para VLIW Problema 3b"
temas: ["ac", "ex", "fp", "latencia", "mem", "pipeline", "vliw"]
claves: ["2 ciclos etapa MEM carga/almacenamiento", "2 ciclos etapa EX operaciones aritméticas FP", "1 ciclo resto etapas"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2016.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[ex]] · [[fp]] · [[latencia]] · [[mem]] · [[pipeline]] · [[vliw]]

Tiempos de pipeline para la planificación VLIW: etapa MEM (acceso a memoria) de L.D y S.D toma 2 ciclos; etapa EX (ejecución) de ADD.D, MUL.D, DIV.D toma 2 ciclos; todas las demás etapas (IF, ID, WB, etc.) toman 1 ciclo. El salto BNEZ tiene slot de retardo (delayed branch).

> Considera los siguientes parámetros temporales: 2 ciclos para la etapa MEM en las cargas y almacenamientos, 2 ciclos para completar la etapa EX de las operaciones aritméticas FP y 1 ciclo para el resto de las etapas.
> — `repo:datos/temarios/AC/examenes/Enero2016.pdf`

Relacionado: [[caracteristicas-del-procesador-vliw-del-examen-enero-2016-pr]] · [[codigo-del-bucle-y-valores-iniciales-de-registros-para-vliw]] · [[parametros-de-temporizacion-vliw-examen-enero-2016]] · [[parametros-de-temporizacion-del-ejercicio-vliw-examen-enero]] · [[parametros-de-temporizacion-del-examen-ac-june-2022-exercise]]
