---
tipo: "dato"
titulo: "Ejercicio de mejora de disco duro y ley de Amdahl (Ej.23)"
temas: ["ac", "almacenamiento", "disco duro", "ley de amdahl", "speedup"]
claves: ["disco duro", "4 veces más rápido", "speedup 3", "fracción de uso"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema1-Introduccion/Tema1 2026-27.pdf (trozo 4 de 5)"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[almacenamiento]] · [[disco duro]] · [[ley de amdahl]] · [[speedup]]

Problema inverso de Amdahl: dado factor de mejora del componente (speedup_disco = 4) y speedup global deseado (3), hallar la fracción de tiempo de ejecución que debe pasar en el disco (f). Fórmula: speedup_global = 1 / [(1 - f) + (f / speedup_disco)]. Despejar f: 3 = 1 / [(1-f) + f/4] => (1-f) + f/4 = 1/3 => 1 - 3f/4 = 1/3 => 3f/4 = 2/3 => f = 8/9 ≈ 88,9%. El disco debe usarse el 88,9% del tiempo para triplicar el rendimiento global.

> Si se sustituye el disco duro de un ordenador por otro disco cuatro veces más rápido que el actual, calcula el uso que debería hacerse de este dispositivo si se quiere conseguir que el ordenador funcione tres veces más rápido.
> — `repo:datos/temarios/AC/Tema1-Introduccion/Tema1 2026-27.pdf (trozo 4 de 5)`

Relacionado: [[ejercicios-de-evaluacion-de-rendimiento-basados-en-ley-de-am]] · [[patron-secuencial-localidad-espacial-y-prefetcher-hardware]] · [[ley-de-amdahl-aplicada-a-mejora-de-disco-fraccion-de-uso-par]] · [[ley-de-amdahl-aplicada-a-mejora-de-disco]] · [[ley-de-amdahl-para-mejora-de-subsistema-disco-6x-mas-rapido]]
