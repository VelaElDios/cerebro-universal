---
tipo: "receta"
titulo: "Cómo identificar dependencia de datos entre iteraciones en bucle con carga y actualización de puntero"
temas: ["ac", "pipeline"]
claves: ["dependencia datos", "bucle", "L.D", "DADDUI", "puntero", "loop-carried"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Noviembre2014A.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]]

En el bucle: L.D F2,0(R1) lee R1; DADDUI R1,R1,#-8 escribe R1. La siguiente iteración de L.D leerá el R1 actualizado. Esto es una dependencia verdadera (RAW) loop-carried a través del registro puntero R1. Impide solapar iteraciones sin renombramiento o desenrollamiento con renombrado.

> Entre las instrucciones L.D y DADDUI... c) Existe una dependencia de datos, a través de R1, entre iteraciones
> — `repo:datos/temarios/AC/examenes/Noviembre2014A.pdf` (cita sin comprobar)

Relacionado: [[analisis-de-dependencias-en-bucle-con-add-d-y-s-d-misma-iter]] · [[antidependencia-entre-iteraciones-en-bucle-con-store-y-actua]]
