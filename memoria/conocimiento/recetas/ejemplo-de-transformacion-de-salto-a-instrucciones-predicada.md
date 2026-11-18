---
tipo: "receta"
titulo: "Ejemplo de transformación de salto a instrucciones predicadas (código ensamblador)"
temas: ["ac", "compilador", "ensamblador", "instrucciones-predicadas", "prediccion-saltos"]
claves: ["CMPEQ", "CMPNE", "predicado", "ADD", "SUB", "predicado falso", "predicado verdadero", "bloques básicos"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[compilador]] · [[ensamblador]] · [[instrucciones-predicadas]] · [[prediccion-saltos]]

**Código con salto (ARM-like):**
```
If (r1==r2)
    r3=r4+r5;
else
    r6=r4-r5;
```
Ensamblador con saltos:
```
sub   x3, x1, x2
bne   x3, x0, L2
L1: add   x3, x4, x5
j     L3
L2: sub   x6, x4, x5
L3: ...
```

**Código con instrucciones predicadas (estilo IA64/EPIC):**
```
CMPEQ  R1, R2, p4     // p4 = (R1 == R2)
CMPNE  R1, R2, p5     // p5 = (R1 != R2)
<p4> ADD  R3, R4, R5  // solo si p4=1
<p5> SUB  R6, R4, R5  // solo si p5=1
```
Ventaja: elimina saltos, crea un bloque básico grande que el compilador puede planificar (reordenar, hacer software pipelining). Inconveniente: ambas instrucciones consumen ancho de banda de fetch/decode/issue y recursos funcionales aunque una se descarte.

> If (r1==r2) sub x3, x1, x2 bne x3, x0, L2 CMPEQ R1, R2, p4 CMPNE R1, R2, p5 <p4> ADD R3, R4, R5 <p5> SUB R6, R4, R5
> — `repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4.pdf` (cita sin comprobar)

Relacionado: [[instrucciones-predicadas-convertir-dependencias-de-control-e]] · [[arquitectura-epic-ia64-y-procesadores-itanium]] · [[ventajas-e-inconvenientes-de-las-instrucciones-predicadas]] · [[salto-retardado-y-instrucciones-predicadas-como-alternativas]]
