---
tipo: "receta"
titulo: "Cómo actualizar referencias a documentación tras reorganización del bundle"
temas: ["documentación", "latex", "mantenimiento"]
claves: ["docs/revision-entrega.md", "docs/documentacion-tecnica.md", "docs/gestion/README.md", "docs/arquitectura.md"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/docs/index.md"]
confianza: "propuesto"
fecha: "2026-11-21"
actualizado: "2026-11-21"
---

Temas: [[documentación]] · [[latex]] · [[mantenimiento]]

Tras la reorganización del bundle documental (2026-11-19), los archivos antiguos de `docs/` desaparecen y su contenido se redistribuye en nuevos ficheros temáticos. Para mantener la trazabilidad en la memoria, hay que sustituir sistemáticamente las referencias a los archivos antiguos por las nuevas:
- `docs/revision-entrega.md` → `docs/sprint-1.md` (sección «Revisión de la entrega frente al enunciado»).
- `docs/documentacion-tecnica.md` → `docs/requisitos.md` (contexto, objetivos, alcance, tablas de RF/RJ/RNF).
- `docs/gestion/README.md` → `docs/sprint-1.md` y `docs/sprint-2.md` (backlog, trazabilidad, evolución).
- Referencias a secciones numeradas de `docs/arquitectura.md` (p. ej. «secciones 4, 13 y 14») → secciones actuales del bundle (seguridad y logs en `arquitectura.md`, métricas en `sprint-2.md`).
Buscar en todos los `.tex` de `chapters/` y `anexos/` las cadenas `docs/` y actualizarlas. Verificar con `verificar.py` que no quedan referencias rotas.

> La documentación de `docs/` se reorganiza como un bundle: un index.md de entrada, esta cronología y un documento por tema con su cabecera... Los documentos anteriores (`documentacion-tecnica.md`, `gestion/README.md`, `revision-entrega.md` y `hito4-configuracion.md`) desaparecen.
> — `repo:saas/docs/index.md` (cita sin comprobar)

Relacionado: [[portada-oficial-unica-y-elementos-fijos-de-la-plantilla]] · [[alcance-por-sprint-cada-entrega-solo-contiene-lo-de-su-sprin]] · [[rutas-de-documentacion-tras-reorganizacion-del-bundle-2026-1]] · [[como-mapear-este-documento-a-los-capitulos-de-la-memoria-tfg]] · [[trazabilidad-completa-requisito-pbi-tarea-pr-82-tareas]] · [[como-referenciar-capturas-de-pantalla-en-la-memoria-sin-copi]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
