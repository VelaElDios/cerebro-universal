---
tipo: "receta"
titulo: "Secuencia obligatoria cuando faltan fuentes en mensaje del revisor"
temas: ["constructor", "flujo-trabajo", "fuentes", "memoria-procesos"]
claves: ["fuentes faltantes", "solicitar fuentes", "bloqueo", "verificar.py"]
proyectos: ["memoria-procesos"]
fuentes: ["bitácora del proyecto (paso actual)"]
confianza: "propuesto"
fecha: "2026-11-19"
actualizado: "2026-11-19"
---

Temas: [[constructor]] · [[flujo-trabajo]] · [[fuentes]] · [[memoria-procesos]]

Si al recibir el mensaje del revisor faltan fuentes críticas:
1. El constructor DEBE detenerse y solicitar las fuentes al usuario (no continuar corrigiendo diagramas/maquetación).
2. En la respuesta al revisor, listar explícitamente qué fuentes faltan y por qué son necesarias.
3. Solo tras recibir las fuentes, proceder a: (a) verificar números, (b) corregir diagramas, (c) maquetación.
4. El revisor marcará "cambios" y bloqueará el avance hasta que estén las fuentes.
5. Esto evita trabajo en vano (corregir diagramas que luego hay que tocar de nuevo al cambiar números).

> TAREA CRÍTICA 1: Solicitar al usuario las 4 fuentes faltantes... Sin ellas, verificar.py seguirá fallando
> — `bitácora del proyecto (paso actual)` (cita sin comprobar)

Relacionado: [[como-manejar-fuentes-faltantes-en-verificacion-automatica-de]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
