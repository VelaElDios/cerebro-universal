---
tipo: "receta"
titulo: "Cómo exportar diagramas Mermaid para la memoria LaTeX"
temas: ["figuras", "grada-colchonera", "latex", "mermaid", "saas", "tfg"]
claves: ["mermaid-cli", "npx", "pdf", "png", "memoria/figuras"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/docs/documentacion-tecnica.md"]
confianza: "verificado"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[figuras]] · [[grada-colchonera]] · [[latex]] · [[mermaid]] · [[saas]] · [[tfg]]

Receta directa: los diagramas de secuencia y arquitectura están escritos en Mermaid dentro de este documento. Para incluirlos en la memoria TFG (LaTeX), ejecutar `npx @mermaid-js/mermaid-cli -i diagrama.mmd -o diagrama.pdf` (o `.png`) y colocar el archivo resultante en `memoria/figuras/`. Así se evita redibujarlos en TikZ/pgf-umlsd y se mantiene consistencia con la documentación técnica.

> **Diagramas.** Todos los diagramas de este documento están en Mermaid. Para la memoria se pueden exportar a PDF o PNG con la CLI de Mermaid (`npx @mermaid-js/mermaid-cli -i diagrama.mmd -o diagrama.pdf`) y guardarlos en `memoria/figuras/`.
> — `repo:saas/docs/documentacion-tecnica.md`

Relacionado: [[diagramas-de-secuencia-con-pgf-umlsd]] · [[como-se-pone-la-portada-oficial-del-tfg-esiiab-uclm]] · [[como-mapear-este-documento-a-los-capitulos-de-la-memoria-tfg]] · [[como-referenciar-capturas-de-pantalla-en-la-memoria-sin-copi]] · [[la-memoria-tfg-se-entrega-en-pdf-con-marcadores-preferibleme]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
