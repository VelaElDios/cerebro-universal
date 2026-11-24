---
tipo: "decision"
titulo: "Prosa de TFG sin cadenas «La figura X muestra…» (regla 13 Javier)"
temas: ["latex", "redaccion", "tfg", "maquetación", "capturas", "figuras"]
claves: ["subfigure", "prosa", "manual de usuario", "capturas", "problema: El borrador tenía ~45 frases sueltas tipo «La figura X muestra…»", "una por captura", "lo que delata un trabajo poco profesional.", "solucion: Reescribir cada sección como prosa continua que explica el flujo de uso. Agrupar capturas relacionadas en una figura con `subfigure` (dos por fila", "`\\begin{subfigure}{0.48\\textwidth}`)", "con un caption general y uno por subfigura. Citar las figuras dentro de la explicación con `\\ref`."]
proyectos: ["memoria-procesos"]
fuentes: ["memoria/reglas-tfg.md regla 13", "memoria/reglas-tfg.md"]
confianza: "propuesto"
fecha: "2026-11-24"
actualizado: "2026-11-24"
---

Temas: [[latex]] · [[redaccion]] · [[tfg]]

Aplicado en capítulos 04-descripcion (manual SaaS) y 04b-juego (manual juego). Cada grupo de capturas relacionadas forma una figura con subfiguras, y el texto explica qué hace el usuario y por qué la app responde, citando las subfiguras con \ref.

Relacionado: [[como-se-agrupan-capturas-con-subfigure]] · [[sin-figuras-repetidas-usar-ref-a-la-figura-existente]] · [[prosa-de-tfg-sin-listas-de-capturas-regla-13-javier]] · [[cadenas-la-figura-x-muestra-prohibidas-prosa-integrada-con-s]] · [[reescribir-frases-la-figura-x-muestra-como-prosa-integrada]]

## Ampliación (2026-11-24, memoria-procesos)
Aplicado en chapters/04-descripcion.tex (sección 6) y chapters/04b-juego.tex (sección 2). Cada grupo de capturas relacionadas forma una figura con subfiguras, y el texto explica la interacción usuario–aplicación.

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
