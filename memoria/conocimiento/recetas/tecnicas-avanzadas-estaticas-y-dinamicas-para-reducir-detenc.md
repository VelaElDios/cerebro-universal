---
tipo: "receta"
titulo: "Técnicas avanzadas estáticas y dinámicas para reducir detenciones"
temas: ["ac", "especulacion", "ilp", "planificacion", "segmentacion"]
claves: ["desenrollamiento bucles", "planificación dinámica marcador scoreboard", "renombre registros", "predicción saltos", "emisión múltiple", "análisis dependencias compilador", "segmentación software", "planificación trazas", "especulación", "desambiguación memoria dinámica"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema2-Paralelismo a nivel de instruccion/Tema2-2026-2027.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[especulacion]] · [[ilp]] · [[planificacion]] · [[segmentacion]]

Catálogo de 10 técnicas con su objetivo principal. Estáticas: desenrollamiento (control), análisis de dependencias (CPIideal + datos), segmentación software (CPIideal + datos), planificación de trazas (CPIideal + datos). Dinámicas: planificación con scoreboard (RAW), renombre (WAR/WAW), predicción dinámica (control), emisión múltiple (CPIideal), especulación (datos + control), desambiguación dinámica MEM (RAW memoria). Cada técnica ataca uno o varios componentes del CPI = CPIideal + detenciones.

> Técnicas avanzadas (estáticas y dinámicas) para reducir:  • Más detenciones por riesgos de control  • Más detenciones por riesgos de datos RAW  • Detenciones por riesgos de datos WAR y WAW  • CPIideal  Técnica                    Reduce  Desenrollamiento de bucles                  Riesgos de control  Planificación dinámica con marcador         Riesgos RAW  Planificación dinámica con renombre         Riesgos WAR y WAW  Predicción dinámica de saltos               Riesgos de control  Emisión múltiple de instrucciones           CPI ideal  Análisis de dependencias del compilador     CPI ideal y riesgos de datos  Segmentación software                       CPI ideal y riesgos de datos  Planificación de trazas                     CPI ideal y riesgos de datos  Especulación                                Riesgos de datos y de control  Eliminación dinámica de ambigüedad en MEM   Riesgos RAW con memoria
> — `repo:datos/temarios/AC/Tema2-Paralelismo a nivel de instruccion/Tema2-2026-2027.pdf` (cita sin comprobar)

Relacionado: [[tecnicas-estaticas-basicas-para-reducir-detenciones-en-pipel]]
