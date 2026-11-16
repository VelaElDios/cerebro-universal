---
tipo: "receta"
titulo: "Cómo configurar un proyecto para trabajar sobre un repo externo"
temas: ["cerebro", "proyectos"]
claves: ["repos", "fuentes", "copiar", "protegidos", "repo:nombre", "cerebro.repos.texto_fuentes"]
proyectos: []
fuentes: ["../../README.md"]
confianza: "verificado"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[cerebro]] · [[proyectos]]

Para que el cerebro lea un repo GitHub público: (1) En `proyecto.json` añadir `"repos": {"saas": "https://github.com/usuario/repo"}`. (2) En `"fuentes"` listar lo que ven las IAs: archivos del proyecto (`fuentes/normas.md`) o del repo (`repo:saas/README.md`, `repo:saas/docs/**/*.md`, `repo:saas/@arbol` para listado de archivos). Soportan `*` y `**`. (3) Si el repo tiene imágenes, usar `"copiar": [{"desde": "repo:saas/docs/capturas/**/*.png", "a": "figs/capturas"}]`; las IAs reciben el texto alternativo de cada imagen desde los Markdown del repo. (4) En `"protegidos"` poner patrones de `borrador/` que las IAs no toquen (ej. `figs/*`). Los repos se descargan frescos en cada paso en `.repos/` (no se sube). En `verificar.py` se puede usar `cerebro.repos.texto_fuentes()` para comprobar datos contra las mismas fuentes.

> Copiar `proyectos/_plantilla/` y poner en `proyecto.json` el repo en `repos` y en `fuentes` qué documentos leer (`repo:nombre/...`). Si tiene capturas, `copiar`.
> — `../../README.md`

Relacionado: [[como-se-empieza-un-proyecto-nuevo-en-el-cerebro]]
