---
tipo: "decision"
titulo: "Solución a JSON mal formado que devolvía HTML de error de Express"
temas: ["bug", "grada-colchonera", "middleware", "saas"]
claves: ["express.json", "400", "JSON", "prueba técnica"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/docs/documentacion-tecnica.md"]
confianza: "verificado"
fecha: "2026-11-16"
actualizado: "2026-11-17"
---

Temas: [[bug]] · [[grada-colchonera]] · [[middleware]] · [[saas]]

Problema: al enviar JSON inválido, Express respondía con su página de error HTML (status 400) antes de llegar a los controladores, rompiendo clientes que esperan JSON. Causa: el parser `express.json()` lanza error que no era capturado por el manejador de errores de la API. Solución: añadir middleware personalizado inmediatamente después de `express.json()` que capture `SyntaxError` del parser y responda `400` con JSON `{error: {code: 'INVALID_JSON', message: 'JSON mal formado'}}` en toda la API. Cubierto por prueba técnica en `domainPolicy.test.js`.

> | Un JSON mal formado devolvía la página de error HTML de Express | El error ocurría en `express.json()`, antes de la capa API | Manejador propio justo después del parser: `400` en JSON en toda la API (prueba técnica) |
> — `repo:saas/docs/documentacion-tecnica.md`

Relacionado: [[estrategia-de-pruebas-niveles-y-enfoque-error-first]] · [[manejo-de-errores-de-principio-a-fin-de-errores-tipados-a-ui]] · [[manejo-de-errores-tipados-con-formato-comun-y-feedback-en-ui]] · [[modulos-del-backend-y-sus-responsabilidades]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
