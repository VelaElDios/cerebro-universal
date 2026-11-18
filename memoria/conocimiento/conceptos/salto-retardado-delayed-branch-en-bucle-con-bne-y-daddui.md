---
tipo: "concepto"
titulo: "Salto retardado (delayed branch) en bucle con BNE y DADDUI"
temas: ["ac", "pipeline", "prediccion-saltos"]
claves: ["delayed branch", "delay slot", "BNE", "DADDUI", "branch latency"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2021.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]] · [[prediccion-saltos]]

El enunciado asume **delayed branch** (salto retardado): la instrucción inmediatamente posterior al salto (el *delay slot*) se ejecuta **siempre**, independientemente de si el salto se toma o no.
En el bucle:
```
DADDUI R2, R2, -8
BNE    R2, R3, Bucle
```
La instrucción en el *delay slot* del BNE sería la siguiente en memoria. Al desenrollar 8×, el compilador/planificador puede **mover instrucciones útiles al delay slot** de cada BNE (p.ej. la L.D de la siguiente iteración o una ADD.D independiente) para ocultar la latencia del salto.
En Processor A (superscalar), el BNE cuenta como instrucción **entera** (ocupa 1 de los 2 slots enteros/ciclo). En Processor B (VLIW), el BNE es una operación más sin restricción de tipo.
La latencia efectiva del salto es 0 ciclos para la instrucción en delay slot; el fetch de la siguiente instrucción (objetivo del salto) comienza en el ciclo siguiente al BNE.

> We assume forwarding and delayed branch.
> — `repo:datos/temarios/AC/examenes/January2021.pdf`

Relacionado: [[definicion-de-latencia-de-salto-y-huecos-de-retardo]] · [[alternativas-de-deteccion-de-instruccion-de-salto-en-pipelin]]
