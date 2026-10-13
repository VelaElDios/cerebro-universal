# Uso de la IA en el proyecto y en esta memoria

Hechos para el anexo «Uso responsable de la inteligencia artificial».

## En el desarrollo de la aplicación (Sprint 1)
- Se usó Claude (Cowork) como asistente: escribió el código, los documentos y los commits (con autoría del alumno y el trailer `Co-Authored-By`), creó y fusionó los PRs y actualizó DoneTonic en el navegador.
- Las cuentas y las credenciales (Neon, Render y Google Cloud) las creó y configuró el alumno.
- El alumno revisó la entrega frase a frase contra el enunciado (`docs/revision-entrega.md`), lo que llevó a corregir el permiso de «comprobar si un usuario está activo» (PR #30).
- La calidad del código se apoya en pruebas automáticas (80) que se ejecutan en el CI en cada PR, no en la palabra de la IA.

## En la redacción de esta memoria
- El borrador lo redactaron IAs gratuitas dentro de «Cerebro Universal», un sistema del alumno en GitHub Actions: una IA constructora (Gemini) escribe y otra IA revisora (modelos gratuitos de OpenRouter) comprueba cada paso.
- Las IAs solo podían usar como fuente la guía del proyecto y la documentación del repositorio.
- Un test automático (que las IAs no pueden modificar) comprueba que el documento compila, que no quedan huecos de la plantilla, que cada cita existe y que ningún número del texto falta en las fuentes.
- Claude preparó la plantilla, las fuentes y ese test.
- El alumno revisa y corrige el resultado final antes de entregarlo y es responsable de su contenido.
