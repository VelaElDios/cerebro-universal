---
tipo: "concepto"
titulo: "Procesador sin soporte para especulación - comportamiento ante excepciones especulativas"
temas: ["ac", "arquitectura", "prediccion-saltos"]
claves: ["sin especulación", "excepción especulativa", "termina programa", "MIPS64"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2014.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[arquitectura]] · [[prediccion-saltos]]

En un procesador sin ayuda para especulación, las instrucciones especulativas (LW*) se ejecutan como instrucciones normales. Si lanzan excepción (acceso a dir 0), la excepción se trata normalmente y termina el programa. No hay mecanismo para descartar resultados de ruta especulativa incorrecta. La primera LW* R1,0(R2) está en la ruta del salto no tomado (BEQZ R3 salta), pero se ejecuta igual y su excepción termina el programa antes de llegar al salto.

> a) Un procesador sin ayuda para la especulación.
> — `repo:datos/temarios/AC/examenes/Enero2014.pdf`

Relacionado: [[tres-mecanismos-de-especulacion-evaluados-en-examen-ac-enero]] · [[especulacion-estatica-con-cargas-especulativas-lw-en-mips64]] · [[analisis-de-codigo-con-especulacion-estatica-para-examen-ac]] · [[especulacion-con-poison-bits-propagacion-y-excepcion-diferid]]
