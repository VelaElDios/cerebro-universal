---
tipo: "concepto"
titulo: "Estructura de la memoria compartida (CEREBRO.md, estado.md, conocimiento, lecciones, mapas)"
temas: ["bitacora", "cerebro", "conocimiento"]
claves: ["memoria/CEREBRO.md", "proyectos/<nombre>/estado.md", "memoria/conocimiento", "memoria/lecciones", "memoria/temas", "memoria/mapas", "confianza", "verificado", "propuesta"]
proyectos: []
fuentes: ["../../README.md"]
confianza: "verificado"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[bitacora]] · [[cerebro]] · [[conocimiento]]

La memoria es el vault Obsidian/Git. Entrada única: `memoria/CEREBRO.md`. Cada proyecto tiene `proyectos/<nombre>/estado.md` (reescrito por el revisor cada paso, lo primero que lee la siguiente IA). Conocimiento persistente en `memoria/conocimiento/` (conceptos, recetas, decisiones, datos) con metadatos máquina y `confianza: "verificado"`; lo alimentan el revisor (bloque `<<<CONOCIMIENTO>>>`) y el proyecto `aprendizaje` (lee docs de proyectos y temarios de `cerebro-datos`). Lecciones en `memoria/lecciones/` (errores resueltos). Mapas temáticos en `memoria/temas/`, visual en `memoria/mapas/cerebro.canvas`, grafo máquina en `memoria/mapas/grafo.json`; se regeneran cada paso.

> El vault es la memoria de todas las IAs: dé igual cuál esté conectada, lee lo que aprendieron las anteriores y lo usa igual. Puerta de entrada: [`memoria/CEREBRO.md`](memoria/CEREBRO.md). - **Ficha de cada proyecto** (`proyectos/<nombre>/estado.md`): qué es, decisiones y convenciones, estado y siguiente. La reescribe el revisor en cada paso y es lo primero que lee la siguiente IA. - **Conocimiento** (`memoria/conocimiento/`): conceptos, recetas (cómo lo hacemos), decisiones (y por qué), datos y documentos aprendidos, con cabecera para máquinas y una cita literal comprobada (`confianza: "verificado"`). Lo escriben el revisor (bloque `<<<CONOCIMIENTO>>>`) y el proyecto `aprendizaje`, que lee la documentación de los proyectos y los temarios del repo privado `cerebro-datos`. - **Lecciones** (`memoria/lecciones/`): errores ya resueltos. - **Mapas** (`memoria/temas/` como nodos centrales, `memoria/mapas/cerebro.canvas` como mapa visual y `memoria/mapas/grafo.json` para máquinas): se regeneran en cada paso.
> — `../../README.md`

Relacionado: [[confianza-del-conocimiento-verificado-o-propuesto]] · [[como-se-empieza-un-proyecto-nuevo-en-el-cerebro]] · [[los-datos-de-entrenamiento-van-a-un-repo-privado]] · [[como-trabaja-el-cerebro-constructor-prueba-revisor]] · [[campos-de-proyecto-json-y-su-proposito]] · [[como-dar-instrucciones-al-cerebro-sin-tocar-el-borrador]]
