---
tipo: "concepto"
titulo: "Definiciones de dependencias de datos: RAW, WAR (antidependencia), WAW (dependencia de salida)"
temas: ["ac"]
claves: ["dependencia datos", "RAW", "WAR", "WAW", "antidependencia", "dependencia salida"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2017.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]]

Dependencia de salida (WAW): ambas instrucciones escriben en el mismo registro/memoria; j después de i → j debe escribir después de i. Antidependencia (WAR): j escribe en un registro que i lee; j después de i → j debe escribir después de que i lea. Dependencia verdadera (RAW): i produce resultado que usa j. La opción b) describe WAR (antidependencia), no WAW. La respuesta correcta es d) Ninguna es correcta (pues b describe WAR).

> Se dice que existe una dependencia de salida entre dos instrucciones i y j (j lógicamente después de i) si a) La instrucción i produce un resultado que usa la instrucción j b) La instrucción j escribe sobre un registro o una posición de memoria que lee la instrucción i c) Ambas instrucciones leen el mismo registro o posición de memoria d) Ninguna es correcta
> — `repo:datos/temarios/AC/examenes/Enero2017.pdf`

Relacionado: [[antidependencia-war-y-dependencia-de-salida-waw-definiciones]]
