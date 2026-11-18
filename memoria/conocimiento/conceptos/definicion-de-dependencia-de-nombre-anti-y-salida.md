---
tipo: "concepto"
titulo: "Definición de dependencia de nombre (anti y salida)"
temas: ["ac", "dependencias", "pipeline"]
claves: ["dependencia nombre", "WAW", "WAR", "antidependencia", "dependencia salida"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2025.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[dependencias]] · [[pipeline]]

La dependencia de nombre (name dependence) ocurre cuando dos instrucciones usan el mismo nombre de registro/posición sin flujo real de datos. Incluye: dependencia de salida (WAW, ambas escriben mismo destino) y antidependencia (WAR, j escribe lo que i lee). La opción correcta es c: ambas son ciertas.

> Dadas dos instrucciones i y j (j lógicamente después de i), existe una dependencia de nombre si: a. Las dos instrucciones i y j escriben sobre el mismo registro o posición de memoria. b. La instrucción j escribe sobre un registro o una posición de memoria que lee la instrucción i. c. Las respuestas a y b son ciertas. d. Todas las anteriores son falsas.
> — `repo:datos/temarios/AC/examenes/Junio2025.pdf`

Relacionado: [[antidependencia-entre-iteraciones-en-bucle-con-store-y-actua]] · [[antidependencia-war-en-bucle-entre-carga-y-actualizacion-de]] · [[definicion-de-dependencia-de-nombre-name-dependency-entre-in]] · [[name-dependency-dependencia-de-nombre-incluye-waw-y-war]] · [[definicion-de-dependencia-de-nombre-waw-y-war]]
