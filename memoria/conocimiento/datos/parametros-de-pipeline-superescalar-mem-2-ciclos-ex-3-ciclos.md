---
tipo: "dato"
titulo: "Parámetros de pipeline superescalar: MEM 2 ciclos, EX 3 ciclos, adelantamiento, ventana grande"
temas: ["ac", "pipeline"]
claves: ["MEM 2 ciclos", "EX 3 ciclos", "forwarding", "ventana instrucciones grande", "superescalar uniforme grado 2"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2015.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]]

Configuración fija para el Problema 4: - Grado de emisión: 2 instrucciones/ciclo (uniforme, cualquier tipo). - Etapa EX (aritmética entera DADD/DSUB): 3 ciclos (pipelined, puede iniciar nueva cada ciclo). - Etapa MEM (carga LW): 2 ciclos (pipelined, puede iniciar nueva cada ciclo). - Adelantamiento (forwarding): resultados disponibles al final de EX/MEM para instrucciones dependientes en ciclos siguientes. - Ventana de instrucciones: ilimitada (todas las 7 instrucciones disponibles desde ciclo 1). - Etapas IF, ID, IS, WB: 1 ciclo cada una (implícito). - Sin saltos en el código.

> El procesador invierte 2 ciclos para la etapa MEM en las cargas y 3 ciclos para completar la etapa EX de las operaciones aritméticas e implementa adelantamiento. Además, asume una ventana de instrucciones lo suficientemente grande como para poder considerar todas las instrucciones del código al mismo tiempo.
> — `repo:datos/temarios/AC/examenes/Junio2015.pdf`

Relacionado: [[bucle-de-calculo-y-i-a-x-i-2-en-ensamblador-mips64]] · [[analisis-de-dependencias-en-bucle-con-add-d-y-s-d-misma-iter]] · [[alternativas-de-deteccion-de-instruccion-de-salto-en-pipelin]] · [[latencias-de-etapas-memoria-y-ejecucion-en-superescalar-exam]] · [[latencias-y-grado-de-superescalaridad-del-problema-3-ac-juni]] · [[configuracion-de-pipeline-mips64-para-problema-de-examen-lat]]
