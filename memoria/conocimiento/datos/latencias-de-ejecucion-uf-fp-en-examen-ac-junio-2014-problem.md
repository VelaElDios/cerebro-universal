---
tipo: "dato"
titulo: "Latencias de ejecución UF FP en examen AC Junio 2014 problema 3"
temas: ["ac", "pipeline", "tomasulo"]
claves: ["latencia ADD.D SUB.D 2 ciclos", "MUL.D 4 ciclos", "DIV.D 20 ciclos", "L.D S.D 2 ciclos"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2014.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]] · [[tomasulo]]

Tabla de latencias de la etapa de **Ejecución** (ciclos de reloj) para cada tipo de instrucción:
- L.D / S.D (carga/almacenamiento FP): 2 ciclos
- ADD.D / SUB.D: 2 ciclos
- MUL.D: 4 ciclos
- DIV.D: 20 ciclos
- Resto (salto, enteras, etc.): 1 ciclo
Nota: "Etapa de ejecución" significa ciclos que la instrucción ocupa la UF desde que empieza ejecución hasta que produce resultado listo para CDB. La emisión, escritura en CDB y terminación (commit) son etapas separadas de 1 ciclo cada una (salvo conflictos estructurales).

> para las instrucciones ADD.D y SUB.D se emplean 2 ciclos, 4 ciclos para MUL.D, 20 ciclos para DIV.D y el resto 1 ciclo.  La etapa de ejecución de una carga y de un almacenamiento emplea 2 ciclos de reloj
> — `repo:datos/temarios/AC/examenes/Junio2014.pdf` (cita sin comprobar)

Relacionado: [[algoritmo-tomasulo-origen-y-objetivo-cpi1]] · [[bucle-vectorial-de-referencia-para-desenrollado-y-planificac]] · [[latencias-de-ejecucion-fp-en-configuracion-examen-junio-2012]] · [[latencias-de-unidades-funcionales-en-coma-flotante-y-memoria]] · [[latencias-de-unidades-funcionales-dadas-en-el-examen-fp-y-me]]
