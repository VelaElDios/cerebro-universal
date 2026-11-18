---
tipo: "receta"
titulo: "Planificación estática con poison bits en MIPS64: reglas de excepción y propagación"
temas: ["ac", "pipeline", "tomasulo"]
claves: ["poison bits", "sucio", "prohibido", "planificación estática", "especulación", "L.D*", "ADD.D*", "BNEZ"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2025.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]] · [[tomasulo]]

Reglas del ejercicio: direcciones 0 y 1 son "prohibidas" para lectura; memoria inicializada a 1 (Mem(dir)=1). Instrucciones marcadas con * son especulativas. Si una carga especulativa (L.D*) accede a dirección prohibida, no lanza excepción inmediata, sino que marca el registro destino como "sucio" (poison bit). Las instrucciones posteriores que usen un registro sucio propagan la suciedad a su registro destino. Solo cuando una instrucción no especulativa (o el commit) intenta usar un registro sucio se lanza la excepción. La tabla debe mostrar tras cada instrucción: valores de registros (R1-R3, F0, F2, F4, F6), memoria (Mem(R1), Mem(R2), Mem(R3)), si hay excepción y si termina el programa. Dos casos iniciales: (a) R1=0, R2=0, R3=8, memorias prohibidas; (b) R1=5, R2=0, R3=7, Mem(R1)=1, Mem(R2) prohibida.

> El procesador usa la técnica de planificación estática con poison bits. Usa “sucio” para registros con poison y “prohibido” para direcciones no válidas.
> — `repo:datos/temarios/AC/examenes/Junio2025.pdf`

Relacionado: [[bits-venenosos-en-carga-especulativa-excepcion-diferida-hast]] · [[bits-venenosos-en-especulacion-excepcion-no-recuperable-marc]]
