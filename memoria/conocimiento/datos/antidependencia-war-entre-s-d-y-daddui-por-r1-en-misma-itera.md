---
tipo: "dato"
titulo: "Antidependencia WAR entre S.D y DADDUI por R1 en misma iteración (bucle MIPS64)"
temas: ["ac", "pipeline"]
claves: ["WAR", "antidependencia", "bucle", "R1", "S.D", "DADDUI"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2016.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]]

En el bucle dado, S.D F4,0(R1) lee R1 (base) y DADDUI R1,R1,#-8 escribe R1. Esto crea una antidependencia (WAR) a través de R1 en la misma iteración: la store necesita el valor antiguo de R1 antes de que se actualice. La opción correcta no está explícita; la c) "dependencia de datos" se refiere a WAR en terminología del examen.

> Entre las instrucciones S.D y DADDUI... a) No existe ningún tipo de dependencia b) Existe una dependencia de salida, a través de R1, en la misma iteración c) Existe una dependencia de datos, a través de R1, en la misma iteración d) Existe una dependencia de datos, a través de R1, entre iteraciones
> — `repo:datos/temarios/AC/examenes/Junio2016.pdf`

Relacionado: [[antidependencia-war-en-bucle-entre-carga-y-actualizacion-de]] · [[antidependencia-entre-iteraciones-en-bucle-con-store-y-actua]] · [[dependencia-entre-iteraciones-en-bucle-con-s-d-y-daddui-sobr]]
