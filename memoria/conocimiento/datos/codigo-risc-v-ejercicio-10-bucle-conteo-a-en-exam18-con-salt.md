---
tipo: "dato"
titulo: "Código RISC-V Ejercicio 10: bucle conteo 'a' en \"exam18\" con saltos B1 (bne) y B2 (bnez)"
temas: ["ac", "prediccion-saltos"]
claves: ["lb", "add", "bne", "addi", "bnez", "exam18", "x1-x6"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4_Prob.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[prediccion-saltos]]

Código completo del Ejercicio 10. Registros: x1=puntero cadena, x2=char actual, x3=copia char, x4='a' (implícito), x5=contador 'a', x6=longitud. Cadena "exam18" = 6 chars + NULL. B1 tomado cuando char != 'a'; B2 tomado cuando char != NULL (i.e., 6 veces tomado, 1 vez no tomado en la iteración del NULL).

> loop:         lb         x2, 0(x1)         # carga en x2 la letra actual de la cadena              add        x3, x2, x0        # copia x2 en x3              bne        x2, x4, not_a     # (B1) comprueba si la letra leída es la “a”              addi       x5, x5, 1         # cuenta el número de letras “a” en la cadena not_a:        addi       x6, x6, 1         # longitud de la cadena (incluido el carácter NULL)              addi       x1, x1, 1         # x1 apunta a la dir. De la siguiente letra              bnez       x3, loop          # (B2) comprueba si el carácter leído es NULL (0x00)
> — `repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4_Prob.pdf`

Relacionado: [[predictor-correlacionado-2-1-para-bucle-de-conteo-de-caracte]] · [[codigo-risc-v-ejercicio-12-bucle-vector-disperso-0-7-0-0-0-0]] · [[codigo-risc-v-ejercicio-11-bucle-fibonacci-6-elementos-con-s]]
