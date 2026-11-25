---
tipo: "decision"
titulo: "Rutas de documentación tras reorganización del bundle (2026-11-19)"
temas: ["documentacion", "latex", "memoria"]
claves: ["docs/", "revision-entrega.md", "documentacion-tecnica.md", "gestion/README.md"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/docs/index.md"]
confianza: "propuesto"
fecha: "2026-11-21"
actualizado: "2026-11-21"
---

Temas: [[documentacion]] · [[latex]] · [[memoria]]

Actualizadas referencias en a4-trazabilidad.tex, a3-uso-ia.tex, 05-evaluacion.tex, a1-desarrollo.tex. Verificado con verificar.py.
relacionado: Portada oficial única y elementos fijos de la plantilla TFG, Cada entrega solo lleva lo de su sprint (alcance coherente)

> La documentación de `docs/` se reorganiza como un bundle: un index.md de entrada, esta cronología y un documento por tema con su cabecera... El contenido sale de los documentos anteriores (`documentacion-tecnica.md`, `gestion/README.md`, `revision-entrega.md` y `hito4-configuracion.md`), que desaparecen"
problema: Tras la reorganización del 19/11/2026, los ficheros antiguos de `docs/` ya no existen; las referencias en la memoria deben apuntar a los nuevos ficheros del bundle.
solucion: Mapeo de rutas antiguas a nuevas: `documentacion-tecnica.md` → `requisitos.md`/`arquitectura.md`; `gestion/README.md` → `sprint-1.md`/`sprint-2.md`; `revision-entrega.md` → `sprint-1.md` (sección «Revisión de la entrega frente al enunciado»); `hito4-configuracion.md` → `procesos.md` (sección «Configuración de los servicios externos»).
> — `repo:saas/docs/index.md` (cita sin comprobar)

Relacionado: [[como-actualizar-referencias-a-documentacion-tras-reorganizac]] · [[como-mapear-este-documento-a-los-capitulos-de-la-memoria-tfg]] · [[como-referenciar-capturas-de-pantalla-en-la-memoria-sin-copi]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]

> ⚠️ Posible contradicción con [[como-mapear-este-documento-a-los-capitulos-de-la-memoria-tfg]]: La Nota A (19/11/2026) afirma que `documentacion-tecnica.md` **desaparece** y se mapea a `requisitos.md`/`arquitectura.md`; la Nota B cita `repo:saas/docs/documentacion-tecnica.md` como documento **fuente vigente** ("este documento") para volcar contenido a la memoria. Además, la Nota A lista ficheros LaTeX actualizados (`a4-trazabilidad.tex`, `a3-uso-ia.tex`, `05-evaluacion.tex`, `a1-desarrollo.tex`) que no coinciden con la estructura de destinos de la Nota B (`capitulos/01-introduccion.tex`, `
