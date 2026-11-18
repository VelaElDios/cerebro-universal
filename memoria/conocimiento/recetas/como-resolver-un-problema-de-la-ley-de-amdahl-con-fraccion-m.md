---
tipo: "receta"
titulo: "Cómo resolver un problema de la Ley de Amdahl con fracción mejorada y speedup objetivo"
temas: ["ac", "rendimiento"]
claves: ["Ley de Amdahl", "speedup", "fracción mejorada", "tiempo de ejecución"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema1-Introduccion/Tema1 2026-27.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[rendimiento]]

Pasos: 1) Identificar tiempo total T (100 s) y tiempo de la parte mejorable T_mej (80 s). 2) La fracción no mejorada es T_no_mej = 20 s. 3) El speedup objetivo es S = 5, por tanto el nuevo tiempo total debe ser T' = T / S = 20 s. 4) Como la parte no mejorada sigue tardando 20 s, la parte mejorada debe tardar 0 s, lo que implica un speedup infinito en la multiplicación. Conclusión: no es posible alcanzar speedup 5x si el 20% del código no se toca. La fórmula general: speedup_mejora = (T_mej) / (T/S - T_no_mej).

> Supongamos que un programa tarda en ejecutarse en una máquina 100 segundos, de los cuales 80 corresponden a operaciones de multiplicar. ¿Cuánto tengo que mejorar la velocidad de multiplicación si quiero que el programa se ejecute cinco veces más rápido?
> — `repo:datos/temarios/AC/Tema1-Introduccion/Tema1 2026-27.pdf`

Relacionado: [[ley-de-amdahl-formula-del-tiempo-de-ejecucion-nuevo]] · [[como-calcular-speedup-global-mejorando-un-componente-ley-de]] · [[ejercicio-de-participacion-en-clase-mejora-de-multiplicacion]] · [[calculo-de-mejora-necesaria-con-la-ley-de-amdahl-test-ac-q3]]
