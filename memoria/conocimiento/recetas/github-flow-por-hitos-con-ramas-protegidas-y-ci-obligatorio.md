---
tipo: "receta"
titulo: "GitHub Flow por hitos con ramas protegidas y CI obligatorio"
temas: ["ci", "git", "grada-colchonera", "metodologia", "saas"]
claves: ["GitHub Flow", "hito-N/integracion", "main", "ramas protegidas", "CI", "PR", "rebase", "feature/rediseno-y-juego", "juego/personajes-pixel", "juego/movilidad-hub"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/docs/documentacion-tecnica.md"]
confianza: "verificado"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[ci]] · [[git]] · [[grada-colchonera]] · [[metodologia]] · [[saas]]

Flujo GitHub Flow por hitos (diagrama Mermaid en sección 4.3):

1. **Tarea Tx en DoneTonic** → Rama `hito-N/Tx-descripcion` desde `hito-N/integracion`
2. **Commits** en español, imperativo, con identificador tarea: `[T5] Añade el repositorio de usuarios en memoria` (según CONTRIBUTING.md)
3. **PR** `[Tx] → hito-N/integracion`
4. **CI**: Pruebas + imagen Docker
   - Rojo → vuelta a commits
   - Verde → Fusión
5. **Tarea HECHA** en tablero
6. **¿Todas las tareas del hito?** → PR `hito-N/integracion → main`
7. **CI en main** → Verde → `main → despliegue automático` → Release `hito-N`

Particularidades:
- `main` y `hito-*/integracion` protegidas: solo PR + CI verde
- **Hito 4**: una rama por tarea (`hito-4/T22-google-oauth`, `T23-correo`, `T24-confirmacion`, `T25-secretos-hito4`, `T26-privacidad`) integrada directamente en `main` con PRs #37–#41. Como dependían unas de otras, se reubicaron (rebase) sobre el `main` real antes de abrir los PRs.
- **Sprint 2 (juego)**: ramas `feature/rediseno-y-juego`, `juego/personajes-pixel` y `juego/movilidad-hub`, con un PR a `main` por fase (#36 y #44–#54) y uno por arreglo (#51, #55, #56). Cada tarea de DoneTonic indica en su descripción el PR donde está.

> `main` y `hito-*/integracion` están **protegidas**: solo admiten cambios por PR y exigen el CI en verde.
> — `repo:saas/docs/documentacion-tecnica.md`

Relacionado: [[definicion-de-hecho-dod-para-tareas-e-hitos]] · [[deshacer-el-paso-entero-si-rompe-la-compilacion]] · [[tocar-trozos-con-cambiar-en-vez-de-reescribir-archivos-enter]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
