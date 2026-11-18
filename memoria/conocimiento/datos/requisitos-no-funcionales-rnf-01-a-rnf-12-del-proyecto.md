---
tipo: "dato"
titulo: "Requisitos no funcionales RNF-01 a RNF-12 del proyecto"
temas: ["grada-colchonera", "requisitos", "saas"]
claves: ["RNF-01", "RNF-02", "RNF-03", "RNF-04", "RNF-05", "RNF-06", "RNF-07", "RNF-08", "RNF-09", "RNF-10", "RNF-11", "RNF-12", "bcrypt", "httpOnly", "secure", "sameSite", "Cloud Run", "Render", "accesibilidad", "responsive", "60 FPS", "trazabilidad", "privacidad", "mantenibilidad"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/docs/documentacion-tecnica.md"]
confianza: "verificado"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[grada-colchonera]] · [[requisitos]] · [[saas]]

Lista completa de 12 requisitos no funcionales con su implementación técnica:
- RNF-01 Seguridad: bcrypt, cookies httpOnly+secure+sameSite, regeneración sesión, permisos servidor, consultas parametrizadas
- RNF-02 Secretos fuera del código: variables de entorno, Secret Manager en producción, fallo al arrancar si falta secreto obligatorio
- RNF-03 Separación en capas: API → lógica → datos/integraciones con inyección de dependencias (sección 5)
- RNF-04 Pruebas automáticas y CI obligatorio: 322 pruebas con node:test, ramas protegidas exigen CI verde
- RNF-05 Despliegue continuo en URL pública: Cloud Run (principal) y Render (alternativo), sin intervención manual
- RNF-06 Disponibilidad y coste: escala a cero (capas gratuitas y créditos educación), versión anterior sigue sirviendo si nueva no arranca
- RNF-07 Accesibilidad: HTML semántico, foco gestionado, aria-live en avisos, aria-describedby en errores, manejo teclado, prefers-reduced-motion
- RNF-08 Responsive: panel admin a tarjetas en móvil, joystick táctil en juego
- RNF-09 Rendimiento juego: 60 FPS en portátil normal, simulación paso fijo, búsqueda espacial por celdas, texturas cacheadas y precargadas
- RNF-10 Trazabilidad: Requisito → PBI → tarea → rama → PR → release (sección 4.4)
- RNF-11 Privacidad: política pública, ranking sin correo, logs ocultan datos sensibles
- RNF-12 Mantenibilidad: sin frameworks ni compilación frontend, equilibrio juego en fichero config, módulos pequeños y comentados

> | Id | Requisito | Cómo se cumple | |---|---|---| | RNF-01 | **Seguridad** de credenciales y sesiones | Hash bcrypt, cookie `httpOnly` + `secure` + `sameSite`, regeneración de la sesión, permisos en el servidor, consultas parametrizadas (sección 8) |
> — `repo:saas/docs/documentacion-tecnica.md`

Relacionado: [[metadatos-del-proyecto-la-grada-colchonera]] · [[requisitos-funcionales-del-sprint-1-13-rf-con-trazabilidad]] · [[requisitos-funcionales-del-juego-sprint-2-20-rj-con-trazabil]] · [[seguridad-bcrypt-coste-10-sin-secretos-en-repo-secret-manage]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
