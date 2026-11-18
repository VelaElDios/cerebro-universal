---
tipo: "receta"
titulo: "Bucle MIPS64 para contar ocurrencias de un carácter en cadena ASCIIZ"
temas: ["ac", "ensamblador", "mips64"]
claves: ["LB", "BNE", "BNEZ", "DADDUI", "ASCIIZ", "contador", "longitud cadena"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2018.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[ensamblador]] · [[mips64]]

Patrón estándar para recorrer una cadena terminada en NULL (ASCIIZ) y contar ocurrencias de un carácter:
- R1: puntero al carácter actual (inicio de cadena)
- R4: carácter buscado (en ASCII, p.ej. 'a' = 0x61)
- R5: contador de ocurrencias (inicializado a 0)
- R6: contador de longitud total (incluye NULL, inicializado a 0)
- R2: carácter cargado (LB R2, 0(R1))
- R3: copia de R2 para test de fin de cadena (DADD R3, R2, R0)
- B1: BNE R2, R4, not_a  # salta si NO es el carácter buscado
- DADDUI R5, R5, #1     # incrementa contador de 'a' (solo si era 'a')
- not_a: DADDUI R6, R6, #1  # incrementa longitud siempre
- DADDUI R1, R1, #1     # avanza puntero
- B2: BNEZ R3, loop     # salta si carácter leído != NULL (0x00)

Para cadena "exam18" (7 bytes: e,x,a,m,1,8,\0):
- B1 (comprueba 'a'): T, N, N, N, N, N, N  (solo en 3ª iteración es 'a' → No tomado; resto Tomado)
- B2 (comprueba NULL):  N, N, N, N, N, N, T  (solo en 7ª iteración es NULL → Tomado; resto No tomado)

> El siguiente código del MIPS64 cuenta el número de letras "a" que hay en una cadena de caracteres ASCIIZ almacenados en memoria.
> — `repo:datos/temarios/AC/examenes/Enero2018.pdf`

Relacionado: [[codigo-mips64-de-conteo-elementos-no-nulos-en-vector-dispers]] · [[codigo-mips64-y-secuencia-de-entrada-para-problema-2-conteo]] · [[codigo-risc-v-ejercicio-10-bucle-conteo-a-en-exam18-con-salt]]
