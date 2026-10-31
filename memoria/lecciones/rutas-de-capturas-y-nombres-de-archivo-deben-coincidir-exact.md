---
titulo: "Rutas de capturas y nombres de archivo deben coincidir exactamente con figs/capturas/"
temas: ["latex", "figuras", "rutas"]
claves: ["no existe la imagen", "figs/capturas/app/01-registro.png", "figs/capturas/hito4/01-correo-recibido.png"]
estado: "propuesta"
veces: 2
fecha: "2026-10-31"
proyectos: ["memoria-procesos"]
---

Temas: [[latex]] · [[figuras]] · [[rutas]]

## Problema
El capítulo 04-descripcion.tex referenciaba capturas con nombres inventados (01-registro.png, 02-login.png, 03-perfil.png, 04-admin.png, hito4/01-correo-recibido.png, etc.) que no existen en el repositorio. Los nombres reales son 01-inicio.png, 02-registro-validacion.png, 03-entrar-error.png, 04-perfil.png, 05-confirmar-baja.png, 06-usuario-sin-permiso.png, 07-panel-admin.png, 08-admin-busqueda.png, 09-admin-sin-resultados.png, 10-admin-confirmar-eliminar.png, 11-panel-admin-movil.png, 12-perfil-movil.png, 13-pagina-no-encontrada.png para app/; y 01-entrar-google.png, 02-registro-correo-enviado.png, 03-cuenta-pendiente-reenvio.png, 04-reenvio-hecho.png, 05-enlace-invalido.png, 06-cuenta-confirmada.png, 07-primer-acceso.png, 08-google-cuenta-creada.png, 09-error-con-reintento.png, 10-panel-admin-estados.png, 11-privacidad.png para hito4/.

## Solución
Antes de escribir \includegraphics, consultar la lista real de archivos en figs/capturas/ (o §16 de documentacion-tecnica.md) y copiar el nombre exacto. Usar rutas relativas desde la raíz del proyecto LaTeX: figs/capturas/app/01-inicio.png, etc.

## Ejemplo
\includegraphics[width=0.9\textwidth]{figs/capturas/app/01-inicio.png} % correcto

Origen: [[proyectos/memoria-procesos/bitacora|memoria-procesos]]
