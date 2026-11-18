---
tipo: "receta"
titulo: "Cómo simular Tomasulo especulativo con ROB de 4 entradas y latencias dadas"
temas: ["ac", "especulacion", "rob", "simulacion", "tomasulo"]
claves: ["Tomasulo especulativo", "ROB", "buffer reordenamiento", "CDB", "emisión", "ejecución", "escritura resultado", "terminación", "latencias ADD.D SUB.D MUL.D DIV.D"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2013.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[especulacion]] · [[rob]] · [[simulacion]] · [[tomasulo]]

8 instrucciones en orden: MUL.D F0,F4,F12 | SUB.D F4,F0,F10 | L.D F0,0(R1) | DIV.D F0,F8,F14 | SUB.D F12,F8,F0 | ADD.D F10,F14,F24 | L.D F0,0(R1) | MUL.D F18,F14,F24. Reglas: ROB 4 entradas (circular), emisión en orden (1 por ciclo si hay entrada ROB y reserva libre), ejecución fuera de orden, escritura en CDB (1 por ciclo, no simultánea con inicio de ejecución que espera ese dato), terminación (commit) en orden cuando instrucción en cabeza ROB y terminada. Latencias: ADD.D/SUB.D=2, MUL.D=4, DIV.D=20, L.D=1 (asumir). Rellenar tabla ciclos: Emisión, Ejecución (inicio-fin), Escritura resultado (ciclo CDB), Terminación (commit). Parte b: estado ROB (entrada, instrucción, destino, valor, terminada s/n) en ciclo donde termina 1ª L.D (3ª instrucción).

> Se tiene un procesador MIPS64 con la versión especulativa del algoritmo de Tomasulo y 4 entradas en el buffer de reordenamiento (ROB), que inicialmente se encuentra vacio. La etapa de ejecución del MIPS64 para las instrucciones ADD.D y SUB.D emplean 2 ciclos, 4 ciclos para MUL.D y 20 ciclos para DIV.D.
> — `repo:datos/temarios/AC/examenes/Enero2013.pdf`

Relacionado: [[algoritmo-tomasulo-origen-y-objetivo-cpi1]] · [[contenido-de-una-estacion-de-reserva-en-tomasulo]] · [[escritura-de-resultado-y-actualizacion-de-qi-en-registro-des]]
