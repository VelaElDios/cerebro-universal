---
tipo: "receta"
titulo: "Análisis de dependencias entre S.D y DADDUI en bucle vectorial"
temas: ["ac", "bucles", "dependencias", "pipeline"]
claves: ["S.D", "DADDUI", "dependencia datos", "R1", "entre iteraciones", "misma iteración"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Noviembre2013.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[bucles]] · [[dependencias]] · [[pipeline]]

S.D F4, 0(R1) usa R1 como base para almacenar. DADDUI R1, R1, #-8 actualiza R1. En la MISMA iteración: S.D lee R1 (valor viejo), DADDUI escribe R1 (valor nuevo) → dependencia de datos RAW (lectura después de escritura) en misma iteración. Entre iteraciones: DADDUI de iteración n escribe R1 que S.D de iteración n+1 leerá → dependencia de datos RAW entre iteraciones. La respuesta correcta es b) misma iteración (la pregunta pregunta específicamente "entre S.D y DADDUI" en el orden del código).

> Entre las instrucciones S.D y DADDUI... a) No existe ningún tipo de dependencia b) Existe una dependencia de datos, a través de R1, en la misma iteración c) Existe una dependencia de datos, a través de R1, entre iteraciones d) Existe una dependencia de salida, a través de R1, en la misma iteración
> — `repo:datos/temarios/AC/examenes/Noviembre2013.pdf`

Relacionado: [[analisis-de-dependencias-en-bucle-con-add-d-y-s-d-misma-iter]] · [[antidependencia-entre-iteraciones-en-bucle-con-store-y-actua]]
