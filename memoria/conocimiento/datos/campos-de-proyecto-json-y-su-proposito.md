---
tipo: "dato"
titulo: "Campos de proyecto.json y su propósito"
temas: ["cerebro", "proyectos"]
claves: ["estado", "temas", "necesita", "comando_prueba", "repos", "fuentes", "copiar", "protegidos", "reintentar_si", "archivo_principal", "pasos", "max_pasos", "max_intentos", "max_archivos_por_paso", "roles", "ultima_ejecucion"]
proyectos: []
fuentes: ["../../README.md"]
confianza: "verificado"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[cerebro]] · [[proyectos]]

Tabla de campos (todos opcionales salvo los mínimos): `estado` (`en-construccion`|`pausado`|`terminado`); `temas` (array de strings para filtrar lecciones); `necesita` (claves de `config/entornos.json` + `apt`/`pip`); `comando_prueba` (ejecutable en `borrador/`, 0=ok); `repos` (dict nombre→URL GitHub público, se clona en `.repos/` cada paso); `fuentes` (globs de archivos del proyecto `fuentes/...` o del repo `repo:saas/...`, incluye `@arbol`); `copiar` (array de `{desde, a}` para traer assets a `borrador/`); `protegidos` (globs de `borrador/` intocables por IAs); `reintentar_si` (regex: el constructor solo reintenta si el fallo coincide); `archivo_principal` (si no existe, la prueba falla sin ejecutarse); `pasos`/`max_pasos` (contador/límite, al llegar pausa el proyecto); `max_intentos` (reintentos del constructor tras fallo de prueba); `max_archivos_por_paso` (límite de escrituras por respuesta de IA); `roles` (override de IAs por rol para este proyecto); `ultima_ejecucion` (timestamp ISO, lo escribe el orquestador para rotación).

> En `proyecto.json`: `nombre`, `temas` (para elegir lecciones), `necesita` (qué instalar), `comando_prueba` y, al final, `"estado": "en-construccion"`.
> — `../../README.md`

Relacionado: [[como-se-empieza-un-proyecto-nuevo-en-el-cerebro]] · [[como-configurar-un-proyecto-para-trabajar-sobre-un-repo-exte]] · [[rotacion-de-proyectos-por-tiempo-sin-avanzar]]
