---
tipo: "concepto"
titulo: "Uso de Qi en registros flotantes para renombrado dinámico en Tomasulo"
temas: ["ac", "registros", "renombrado", "tomasulo"]
claves: ["Qi", "estado de los registros", "f0", "f4", "f2", "renombrado dinamico"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[registros]] · [[renombrado]] · [[tomasulo]]

La tabla «Estado de los registros» muestra para cada registro flotante (f0, f2, f4, f6, f8, f10, f12) la columna Qi que indica qué unidad funcional o buffer escribirá su próximo valor.
- f0: recibe Qi = «Carga 1» en ciclo 2, luego «Carga 2» en ciclo 6.
- f4: recibe Qi = «Mult 1» en ciclo 2, luego «Mult 2» en ciclo 7.
- f2: nunca muestra Qi (valor disponible desde el inicio).
Esto implementa el renombrado dinámico: las instrucciones leen Vj/Vk si el valor está listo, o Qj/Qk con la etiqueta del productor si no lo está.

> Qi        Carga 1                 Mult 1
> — `repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf`

Relacionado: [[algoritmo-tomasulo-origen-y-objetivo-cpi1]] · [[buffers-de-carga-y-almacenamiento-en-tomasulo]]
