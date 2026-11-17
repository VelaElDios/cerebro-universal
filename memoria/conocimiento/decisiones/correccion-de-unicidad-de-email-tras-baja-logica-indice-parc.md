---
tipo: "decision"
titulo: "Corrección de unicidad de email tras baja lógica: índice parcial y findByEmail ignora eliminadas"
temas: ["base-de-datos", "grada-colchonera", "migracion", "saas"]
claves: ["migración 005", "índice parcial", "UNIQUE", "findByEmail", "cuenta eliminada"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/docs/documentacion-tecnica.md"]
confianza: "verificado"
fecha: "2026-11-16"
actualizado: "2026-11-17"
---

Temas: [[base-de-datos]] · [[grada-colchonera]] · [[migracion]] · [[saas]]

Problema: usuario eliminaba su cuenta (baja lógica) y luego no podía registrarse ni entrar con Google con ese email porque la restricción `UNIQUE` en `users.email` bloqueaba la reinserción, y `findByEmail` encontraba la cuenta eliminada impidiendo nuevo login. Descubierto 29/10/2026. Solución: migración 005 crea índice parcial único `CREATE UNIQUE INDEX ON users(email) WHERE deleted_at IS NULL`; `findByEmail` añade `WHERE deleted_at IS NULL`; al eliminar se pone `deleted_at = now()`, se libera el `nickname` y la cuenta sale del ranking. Así, un email eliminado puede usarse para nueva cuenta (registro normal o Google). Se añadieron pruebas del caso completo.

> | Quien eliminaba su cuenta (sobre todo de Google) no podía volver a entrar nunca con ese email (lo encontró un amigo probando la app, 29/10/2026) | Por la baja lógica la fila seguía en `users` con su email, que era `UNIQUE`; además, por diseño, una cuenta eliminada no podía entrar «ni con Google» | Migración 005: el email solo es único entre las cuentas no eliminadas (índice parcial); `findByEmail` ignora las eliminadas, así que registrarse o entrar con Google crea una cuenta nueva;
> — `repo:saas/docs/documentacion-tecnica.md`

Relacionado: [[estrategia-de-pruebas-niveles-y-enfoque-error-first]] · [[desglose-del-alcance-del-sprint-1-por-hitos-y-fechas]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
