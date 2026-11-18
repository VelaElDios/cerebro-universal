---
tipo: "dato"
titulo: "Estado inicial de registros y memoria para Problema 3 (Enero 2015)"
temas: ["ac", "examen", "prediccion-saltos"]
claves: ["R1=10 R2=5 R3=0 R4=20 R5=10 R6=5 R7=0 R8=20 R9=10", "memoria 0-1023=0", "dir 0 ilegal"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2015.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[examen]] · [[prediccion-saltos]]

Valores concretos del enunciado para simular el Problema 3:
- **Registros iniciales:**
  - R1 = 10
  - R2 = 5
  - R3 = 0
  - R4 = 20
  - R5 = 10
  - R6 = 5
  - R7 = 0
  - R8 = 20
  - R9 = 10
- **Memoria:** Direcciones 0 a 1023 inicializadas a 0.
- **Restricción clave:** Cualquier acceso (lectura o escritura) a la dirección **0** lanza **excepción por acceso ilegal**. Esto afecta a `LW* R1,0(R1)` si R1=0, `LW* R3,0(R3)` si R3=0, y `SW R8,0(R2)` si R2=0 (R2=5, no es 0).
- En la ejecución secuencial (caso a), R3=0 inicialmente → segunda LW* accede a dir 0 → excepción inmediata.
- En poison bits (caso b), la segunda LW* marca R3 como "sucio"; la excepción real ocurre en el SW al intentar usar el valor sucio.

> sabiendo que el estado inicial es: R1=10 R2=5 R3=0 R4=20 R5=10 R6=5 R7=0 R8=20 R9=10. Y que el acceso a la dirección de memoria 0 está prohibido (cualquier intento de leer o escribir en dicha posición lanzará una excepción por acceso ilegal). Además, el contenido de las 1024 primeras direcciones de memoria se han inicializado a 0.
> — `repo:datos/temarios/AC/examenes/Enero2015.pdf` (cita sin comprobar)

Relacionado: [[como-resolver-el-problema-3-de-especulacion-con-poison-bits]] · [[especulacion-estatica-con-poison-bits-en-mips64-lw]]
