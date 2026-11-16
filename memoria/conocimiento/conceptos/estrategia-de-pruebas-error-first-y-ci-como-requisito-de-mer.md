---
tipo: "concepto"
titulo: "Estrategia de pruebas error-first y CI como requisito de merge"
temas: ["grada-colchonera", "pruebas", "saas"]
claves: ["error-first", "CI", "GitHub Actions", "regresiones", "merge"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/docs/documentacion-tecnica.md"]
confianza: "verificado"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[grada-colchonera]] · [[pruebas]] · [[saas]]

Enfoque error-first: escribir pruebas que validen primero los caminos de error (entradas inválidas, permisos, fallos de red, estados límite) antes que el happy path.
CI obligatorio: GitHub Actions ejecuta tests, lint y build en cada PR; no se puede fusionar sin CI en verde.
Resultado: cero regresiones detectadas en producción durante todo el desarrollo de ambos sprints.
Aplicable a: validación de formularios, middlewares de auth/roles, endpoints API, lógica de juego (determinismo, colisiones).

> Probar primero los **casos de error** y tener el CI como requisito para fusionar evitó regresiones durante todo el desarrollo.
> — `repo:saas/docs/documentacion-tecnica.md`

Relacionado: [[estrategia-de-pruebas-niveles-y-enfoque-error-first]] · [[formato-de-logs-json-y-eventos-registrados]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
