---
tipo: "receta"
titulo: "Cómo resolver el Problema 3 de especulación con poison bits (Enero 2015)"
temas: ["ac", "examen", "prediccion-saltos"]
claves: ["LW*", "poison bit", "BEQZ", "DADDI", "DADD", "SW", "registro sucio", "registro indefinido", "excepción acceso ilegal dirección 0"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2015.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[examen]] · [[prediccion-saltos]]

**Código:**
```
LW*   R1, 0(R1)        ; Carga especulativa
BEQZ  R3, salto1
DADDI R1, R1, #8
salto1: LW*   R3, 0(R3)        ; Carga especulativa
BEQZ  R6, salto2
DADDI R5, R3, #-1
salto2: DADD  R8, R1, R5
SW    R8, 0(R2)
DADDI R9, R0, #1
```

**Estado inicial:** R1=10, R2=5, R3=0, R4=20, R5=10, R6=5, R7=0, R8=20, R9=10. Memoria[0..1023]=0, pero acceso a dir 0 → excepción.

**Caso a) Sin ayuda para especulación (ejecución secuencial normal):**
- LW* R1,0(R1): R1=10 → dir 10. Mem[10]=0 → R1=0. (No hay excepción, dir 10 ≠ 0)
- BEQZ R3, salto1: R3=0 → salta a salto1.
- DADDI R1,R1,#8: **NO se ejecuta** (salto tomado).
- LW* R3,0(R3): R3=0 → dir 0 → **EXCEPCIÓN por acceso ilegal**. Programa **NO termina**.
- Resto no se ejecuta.
- Registros al fallar: R1=0, R2=5, R3=0 (antes de la carga), R4=20, R5=10, R6=5, R7=0, R8=20, R9=10.

**Caso b) Con poison bits:**
- LW* R1,0(R1): dir 10 → Mem[10]=0 → R1=0 (poison=0).
- BEQZ R3, salto1: R3=0 → salta a salto1 (la especulación de la primera carga era correcta, no hay poison).
- DADDI R1,R1,#8: **NO se ejecuta** (salto tomado).
- LW* R3,0(R3): dir 0 → **acceso ilegal**. Como es LW*, **no lanza excepción ya**; pone **poison bit=1 en R3** (R3 = "sucio").
- BEQZ R6, salto2: R6=5 ≠ 0 → **NO salta** (cae a siguiente).
- DADDI R5,R3,#-1: usa R3 (sucio) → R5 = "sucio" (propaga poison).
- DADD R8,R1,R5: usa R5 (sucio) → R8 = "sucio".
- SW R8,0(R2): R2=5 → dir 5. **SW no es especulativa**; intenta escribir valor sucio → **EXCEPCIÓN por poison bit** (o por acceso ilegal si la dir fuera 0, pero es 5). Programa **NO termina**.
- DADDI R9,R0,#1: no se ejecuta.
- Registros al fallar: R1=0, R2=5, R3=sucio, R4=20, R5=sucio, R6=5, R7=0, R8=sucio, R9=10 (inalterado).
**Nota:** Usar etiquetas "indefinido" (valor nunca escrito) y "sucio" (poison bit a 1) según enunciado.

> Indica para cada caso las instrucciones que lanzan alguna excepción, y si terminan o no el programa, así como el valor de los registros al finalizar el programa sabiendo que el estado inicial es: R1=10 R2=5 R3=0 R4=20 R5=10 R6=5 R7=0 R8=20 R9=10. Y que el acceso a la dirección de memoria 0 está prohibido (cualquier intento de leer o escribir en dicha posición lanzará una excepción por acceso ilegal).
> — `repo:datos/temarios/AC/examenes/Enero2015.pdf` (cita sin comprobar)

Relacionado: [[especulacion-estatica-con-poison-bits-en-mips64-lw]] · [[especulacion-con-poison-bits-propagacion-y-excepcion-diferid]] · [[estado-inicial-de-registros-y-memoria-para-problema-3-enero]] · [[planificacion-estatica-con-poison-bits-en-mips64-reglas-de-e]]
