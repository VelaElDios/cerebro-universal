---
tipo: "concepto"
titulo: "Dependencias en bucle vectorial: dependencia de datos a través de F4 entre iteraciones (RAW)"
temas: ["ac"]
claves: ["dependencia entre iteraciones", "RAW", "bucle", "vector", "F4"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2017.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]]

I1 carga F4, I3 almacena F4. En la misma iteración: I1 → I3 es RAW (I1 escribe F4, I3 lo lee para almacenar). Entre iteraciones: I3 (iteración n) escribe en memoria 0(R1); I1 (iteración n+1) lee de 0(R1) tras incrementar R1. Como R1 se incrementa en 8 (DADDUI), acceden a direcciones distintas → no hay dependencia entre iteraciones a través de memoria. Pero a través de F4: I3 escribe F4 (registro), I1 siguiente iteración escribe F4 (carga) → WAW en F4 entre iteraciones. La opción a) dice dependencia de datos (RAW) a través de F4 entre iteraciones: falsa (es WAW). Opción b) dependencia de salida (WAW) en misma iteración: falsa (I1 e I3 misma iteración: I1 escribe, I3 lee → RAW). Opción c) antidependencia (WAR) entre iteraciones: falsa. Respuesta correcta: d) Ninguna es correcta.

> Entre las instrucciones I1 e I3, en el bucle siguiente: LOOP: L.D F4, 0(R1) ; I1 DIV.D F4, F4, F2 ; I2 S.D F4, 0(R1) ; I3 ... a) Hay una dependencia de datos, a través de F4, entre iteraciones b) Hay una dependencia de salida, a través de F4, en la misma iteración c) Hay una antidependencia, a través de F4, entre iteraciones d) Ninguna es correcta
> — `repo:datos/temarios/AC/examenes/Enero2017.pdf` (cita sin comprobar)

Relacionado: [[antidependencia-war-y-dependencia-de-salida-waw-definiciones]]
