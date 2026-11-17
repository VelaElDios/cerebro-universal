---
tipo: "receta"
titulo: "Ejercicios de evaluación de rendimiento basados en Ley de Amdahl"
temas: ["ac", "ganancia de velocidad", "ley de amdahl", "mejora de componente"]
claves: ["Amdahl", "speedup", "ganancia de velocidad", "punto flotante", "multiplicación", "acceso a memoria", "disco duro"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema1-Introduccion/Tema1 2026-27.pdf (trozo 4 de 5)"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[ganancia de velocidad]] · [[ley de amdahl]] · [[mejora de componente]]

Colección de problemas típicos que aplican la ley de Amdahl (speedup global = 1 / [(1 - fracción_mejorada) + (fracción_mejorada / factor_mejora)]). Incluyen: Ej.4: mejora 5x en FP que ocupa 50% del tiempo; Ej.5: buscar fracción de FP para speedup global 3x con mejora 5x; Ej.7: mejora necesaria en FP (80% instrucciones) para speedup global 1.5x; Ej.13: dos mejoras alternativas (multiplicación 4x con 20% uso, memoria 2x con 50% uso) y combinada; Ej.14: elegir entre reducir tiempo multiplicación 25% (10% uso) o memoria 15% (35% uso); Ej.23: disco 4x más rápido, ¿qué fracción de uso para speedup global 3x? Todos se resuelven identificando fracción de tiempo afectada y factor de mejora.

> Supongamos que mejoramos una máquina haciendo que todas las instrucciones en punto flotante se ejecuten cinco veces más rápidas. Si el tiempo de ejecución de algún programa de prueba antes de la mejora de punto flotante es de 10 segundos, ¿cuál será la ganancia de velocidad si la mitad de los 10 segundos se emplea en ejecutar instrucciones de punto flotante?
> — `repo:datos/temarios/AC/Tema1-Introduccion/Tema1 2026-27.pdf (trozo 4 de 5)`

Relacionado: [[patron-temporal-localidad-temporal-maxima-reutilizando-un-bl]]
