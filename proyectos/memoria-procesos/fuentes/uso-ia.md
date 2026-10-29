# Uso de la IA en el proyecto y en esta memoria

Hechos para el anexo «Uso responsable de la inteligencia artificial».

## En el desarrollo de la aplicación (Sprint 1)
- Se usó Claude (Cowork) como asistente: escribió el código, los documentos y los commits (con autoría del alumno y el trailer `Co-Authored-By`), creó y fusionó los PRs y actualizó DoneTonic en el navegador.
- Las cuentas y las credenciales (Neon, Render y Google Cloud) las creó y configuró el alumno.
- El alumno revisó la entrega del Sprint 1 frase a frase contra el enunciado (`docs/revision-entrega.md`), lo que llevó a corregir el permiso de «comprobar si un usuario está activo» (PR #30).
- La calidad del código se apoya en las pruebas automáticas que se ejecutan en el CI en cada PR, no en la palabra de la IA.

## En la redacción de esta memoria
- El borrador lo redactaron IAs gratuitas dentro de «Cerebro Universal», un sistema del alumno en GitHub Actions: en cada paso una IA constructora escribe y otra IA revisora comprueba el resultado contra las fuentes.
- Se usaron modelos gratuitos de varias empresas: Gemini (Google), modelos de la API de NVIDIA (GLM, MiniMax y Nemotron) y modelos gratuitos de OpenRouter. Si un modelo falla, entra el siguiente.
- Las IAs solo podían usar como fuente la documentación del repositorio (que se descarga en cada paso) y estas notas.
- Un test automático (que las IAs no pueden modificar) comprueba que el documento compila, que no quedan huecos de la plantilla, que cada cita existe, que están todos los requisitos, PBIs y tareas, y que ningún número del texto falta en las fuentes.
- Claude preparó la plantilla, las fuentes y ese test, y revisó el resultado compilándolo.
- El alumno revisa y corrige el resultado final antes de entregarlo y es responsable de su contenido.
