---
tipo: "receta"
titulo: "Cómo referenciar capturas de pantalla en la memoria sin copiar archivos"
temas: ["capturas", "figuras", "grada-colchonera", "latex", "saas", "tfg"]
claves: ["graphicspath", "includegraphics", "docs/capturas/app", "docs/capturas/hito4", "docs/capturas/produccion"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/docs/documentacion-tecnica.md"]
confianza: "verificado"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[capturas]] · [[figuras]] · [[grada-colchonera]] · [[latex]] · [[saas]] · [[tfg]]

La plantilla LaTeX de la memoria (`memoria/main.tex`) ya tiene configurado `\graphicspath` con tres carpetas del repositorio: `docs/capturas/app/` (capturas generales de la app), `docs/capturas/hito4/` (capturas específicas del Hito 4: email, OAuth, errores, privacidad) y `docs/capturas/produccion/` (capturas del despliegue real en Cloud Run). Por tanto, para insertar una captura en la memoria basta usar `\includegraphics{nombre-sin-extension}` (ej. `\includegraphics{07-panel-admin}`) sin copiar archivos. El índice completo con descripción de cada captura está en la sección 16 de este documento.

> **Capturas.** `\graphicspath` de `memoria/main.tex` ya busca en `docs/capturas/app/`, `docs/capturas/hito4/` y `docs/capturas/produccion/`, así que basta con `\includegraphics{07-panel-admin}`. La lista completa, con lo que muestra cada una, está en la [sección 16](#16-índice-de-capturas).
> — `repo:saas/docs/documentacion-tecnica.md`

Relacionado: [[agrupar-capturas-con-subfigure]] · [[figuras-que-comparten-pagina-con-el-texto-parametros-de-flot]] · [[inventario-de-capturas-de-pantalla-con-trazabilidad-a-requis]] · [[como-centralizar-capturas-duplicadas-entre-capitulos-en-late]] · [[como-mapear-este-documento-a-los-capitulos-de-la-memoria-tfg]] · [[una-imagen-en-un-solo-sitio-y-en-el-resto-una-referencia]] · [[agrupar-capturas-relacionadas-en-subfiguras-con-prosa-integr]] · [[cada-imagen-aparece-una-sola-vez-en-el-capitulo-canonico]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
