---
tipo: "fuente"
titulo: "tarea4 2 branchless (Code_Lab4)"
temas: ["ac"]
claves: []
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab4/tarea4_2_branchless.cpp"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]]

Documento aprendido: `repo:datos/temarios/AC/Practicas/Code_Lab4/tarea4_2_branchless.cpp`.

## Resumen
Este trozo implementa un experimento de arquitectura de computadores que compara el rendimiento de código con salto condicional (`if (x >= 128)`) frente a una versión branchless usando aritmética condicional. El código genera datos aleatorios (semilla 42), los ordena, y mide cuatro configuraciones: con salto en datos desordenados/ordenados y sin salto en ambos. Los atributos `__attribute__((optimize(...)))` fuerzan al compilador a mantener el salto real para que el predictor de ramas sea probado. La verificación exige que los cuatro checksums coincidan.

## Lo que se sacó de él (7)
- [[como-forzar-un-salto-condicional-real-en-gcc-para-medir-pred]]
- [[cuando-no-usar-branchless-trade-off-latencia-vs-previsibilid]]
- [[parametros-fijos-del-experimento-de-branchless-tamanio-repet]]
- [[patron-branchless-suma-condicional-mediante-multiplicacion-p]]
- [[penalizacion-de-fallo-de-prediccion-de-salto-en-pipeline-sup]]
- [[por-que-el-orden-de-los-datos-afecta-al-codigo-con-salto-per]]
- [[verificacion-de-correccion-mediante-checksum-identico-en-las]]
