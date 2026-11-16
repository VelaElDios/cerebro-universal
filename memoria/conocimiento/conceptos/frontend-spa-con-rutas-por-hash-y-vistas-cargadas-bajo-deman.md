---
tipo: "concepto"
titulo: "Frontend SPA con rutas por hash y vistas cargadas bajo demanda"
temas: ["frontend", "grada-colchonera", "saas", "spa"]
claves: ["hash routes", "ui.js", "vistas bajo demanda", "import()", "estado", "cabecera", "formularios", "avisos", "componentes", "diálogos", "modal", "api.js"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/docs/documentacion-tecnica.md"]
confianza: "verificado"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[frontend]] · [[grada-colchonera]] · [[saas]] · [[spa]]

SPA de una página con enrutado por hash (`public/js/ui.js`): rutas `#/` (inicio), `#/entrar`, `#/registro`, `#/perfil`, `#/jugar`, `#/admin`, y 404 ("Fuera de juego"). Cada ruta declara acceso (protegida, solo invitados, solo admin); la UI redirige pero la protección real es server-side. Vistas en `ui/vistas/*.js` exportan `montar(raiz, contexto)` y devuelven función limpieza; se cargan lazy con `import()`. Estado global en `ui/estado.js` (usuario actual); cabecera (`ui/cabecera.js`) se repinta al cambiar (mote, avatar, enlaces según rol). Formularios (`ui/formulario.js`): validación al escribir (tras tocar campo) y al enviar, errores con `aria-describedby`, botón "Mostrar contraseña", doble envío bloqueado con spinner. Avisos (`ui/avisos.js`): mensajes temporales en zona `aria-live`, errores con `role="alert"`; los que vienen por redirección (`?aviso=...`) se leen al cargar y se limpian de la URL. Componentes (`ui/componentes.js`): spinner, estado vacío, estado error con botón "Reintentar" y `mensajeDeError` que traduce cualquier error a texto legible y loguea en consola. Diálogos (`ui/modal.js`): confirmación accesible con `<dialog>` nativo (foco en botón seguro, `Esc` cierra, foco vuelve al origen); usado antes de acciones destructivas.

> SPA con rutas por hash (public/js/ui.js): #/ inicio, #/entrar, #/registro, #/perfil, #/jugar y #/admin, y una vista 404 («Fuera de juego»). Cada ruta declara si es protegida, solo para invitados o solo para administradores; la interfaz redirige, pero la protección real está en el servidor.
> — `repo:saas/docs/documentacion-tecnica.md`

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
