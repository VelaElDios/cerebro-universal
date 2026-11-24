---
tipo: "decision"
titulo: "Prosa de TFG sin cadenas «La figura X muestra…» (regla 13 Javier)"
temas: ["latex", "redaccion", "tfg"]
claves: ["subfigure", "prosa", "manual de usuario", "capturas", "problema: El borrador tenía ~45 frases sueltas tipo «La figura X muestra…»", "una por captura", "lo que delata un trabajo poco profesional.", "solucion: Reescribir cada sección como prosa continua que explica el flujo de uso. Agrupar capturas relacionadas en una figura con `subfigure` (dos por fila", "`\\begin{subfigure}{0.48\\textwidth}`)", "con un caption general y uno por subfigura. Citar las figuras dentro de la explicación con `\\ref`."]
proyectos: ["memoria-procesos"]
fuentes: []
confianza: "propuesto"
fecha: "2026-11-24"
actualizado: "2026-11-24"
---

Temas: [[latex]] · [[redaccion]] · [[tfg]]

Aplicado en capítulos 04-descripcion (manual SaaS) y 04b-juego (manual juego). Cada grupo de capturas relacionadas forma una figura con subfiguras, y el texto explica qué hace el usuario y por qué la app responde, citando las subfiguras con \ref.

Relacionado: [[como-se-agrupan-capturas-con-subfigure]] · [[sin-figuras-repetidas-usar-ref-a-la-figura-existente]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
