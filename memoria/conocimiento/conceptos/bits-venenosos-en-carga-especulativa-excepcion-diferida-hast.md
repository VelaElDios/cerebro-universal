---
tipo: "concepto"
titulo: "Bits venenosos en carga especulativa: excepción diferida hasta uso del registro"
temas: ["ac", "bits-veneno", "especulacion", "poison-bits", "tomasulo"]
claves: ["bits veneno", "poison bits", "carga especulativa", "excepción", "registro destino", "sobrescritura"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2026.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[bits-veneno]] · [[especulacion]] · [[poison-bits]] · [[tomasulo]]

En Tomasulo especulativo, una carga que falla (excepción) no interrumpe inmediatamente; pone el bit veneno en su registro destino (x4). Si luego una instrucción no especulativa usa ese registro (como fuente), se lanza la excepción. En el ejemplo, I2 (especulativa) falla al leer dir 0 → bit veneno en x4. El salto I3 no se toma (x3=0), por lo que I4 (addi x4, x0, 2) sobrescribe x4 **antes** de que I5 (sw) lo use como dato. Al sobrescribirse, el bit veneno se limpia y el programa continúa sin excepción por ese registro. (La store I5 sí causaría excepción por dir 0, pero la opción b dice que finaliza correctamente, asumiendo que la store no se ejecuta o se ignora en el enunciado).

> El estado de los registros antes de ejecutar este código es: x0 =0, x1 =1000, x2 =0, x3 =2000, x4=0. Además, el acceso a la dirección de memoria 0 está prohibido... (I2) lw x4, 0(x2) # carga especulativa de B ... b. La instrucción I2 genera una excepción, establece el bit venenoso en el registro x4 a 1, pero el programa finaliza correctamente.
> — `repo:datos/temarios/AC/examenes/Enero2026.pdf` (cita sin comprobar)

Relacionado: [[comportamiento-de-bits-de-veneno-poison-bits-ante-excepcion]] · [[configuracion-tomasulo-con-especulacion-para-examen-enero-20]]
