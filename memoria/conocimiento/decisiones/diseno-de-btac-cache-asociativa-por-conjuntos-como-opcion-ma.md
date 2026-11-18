---
tipo: "decision"
titulo: "Diseño de BTAC: caché asociativa por conjuntos como opción más usada"
temas: ["ac", "arquitectura", "btac", "diseno-cache", "prediccion-saltos"]
claves: ["BTAC", "asociativa por conjuntos", "direct-mapped", "fully associative", "Pentium II", "HP8500", "R12000"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[arquitectura]] · [[btac]] · [[diseno-cache]] · [[prediccion-saltos]]

Tres diseños comparados: (1) Direct-mapped: menor coste, pero aliasing (dos saltos compiten por misma entrada). (2) Fully associative: menor aliasing, mayor coste hardware. (3) Set-associative: compromiso intermedio, es la opción más usada en la práctica. Ejemplos reales que la usan: Pentium II, HP8500, R12000.

> Cache asociativa por conjuntos: Solución intermedia. La opción más usada. Pentium II HP8500 R12000
> — `repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4.pdf` (cita sin comprobar)

Relacionado: [[funcionamiento-y-actualizacion-de-la-btac-branch-target-addr]] · [[estructuras-hardware-para-prediccion-de-saltos-btac-bht-btb]] · [[implementacion-de-btb-generica-ampliacion-de-btac-con-bits-d]]
