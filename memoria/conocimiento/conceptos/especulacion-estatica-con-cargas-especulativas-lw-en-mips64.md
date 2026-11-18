---
tipo: "concepto"
titulo: "Especulación estática con cargas especulativas LW* en MIPS64"
temas: ["ac", "arquitectura", "prediccion-saltos"]
claves: ["LW*", "carga especulativa", "especulación estática", "MIPS64", "examen Enero 2014"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2014.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[arquitectura]] · [[prediccion-saltos]]

El examen utiliza la notación LW* para indicar cargas especulativas que se ejecutan antes de saber si la instrucción debería ejecutarse realmente (están en la ruta especulativa de un salto). El código tiene dos cargas especulativas a dirección 0(R2) donde R2=0, por lo que acceden a dirección de memoria 0 que está prohibida y lanza excepción por acceso ilegal. Esto permite evaluar cómo manejan los diferentes mecanismos de especulación las excepciones en instrucciones especulativas.

> LW*   R1, 0(R2)                ; Carga especulativa
> — `repo:datos/temarios/AC/examenes/Enero2014.pdf`

Relacionado: [[especulacion-estatica-con-poison-bits-en-mips64-lw]] · [[analisis-de-codigo-con-especulacion-estatica-para-examen-ac]] · [[procesador-sin-soporte-para-especulacion-comportamiento-ante]]
