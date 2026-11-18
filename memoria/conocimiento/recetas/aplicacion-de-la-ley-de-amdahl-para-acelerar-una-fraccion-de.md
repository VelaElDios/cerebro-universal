---
tipo: "receta"
titulo: "Aplicación de la ley de Amdahl para acelerar una fracción del programa"
temas: ["ac", "ley-amdahl", "rendimiento"]
claves: ["Amdahl", "speedup", "fracción mejorada", "tiempo ejecución"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2026.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[ley-amdahl]] · [[rendimiento]]

Para lograr un speedup global de 2× (tiempo total 100 s) cuando la suma consume 120 s de 200 s: la parte no mejorada tarda 80 s, por lo que la suma debe bajar a 20 s. El factor de mejora de la suma es 120/20 = 6. Respuesta correcta: 6 (opción b). Fórmula general: speedup_global = 1 / ((1-f) + f/k), donde f=0.6, speedup_global=2 → k=6.

> Supongamos que un programa tarda en ejecutarse en una máquina 200 segundos, de los cuales corresponden a operaciones de suma 120 segundos ¿Cuánto tenemos que mejorar la velocidad de la suma para que el programa se ejecute dos veces más rápido?
> — `repo:datos/temarios/AC/examenes/Enero2026.pdf`

Relacionado: [[ley-de-amdahl-aplicada-a-mejora-de-una-fraccion-del-tiempo-d]] · [[calculo-de-mejora-necesaria-con-ley-de-amdahl-fraccion-mejor]] · [[aplicacion-de-la-ley-de-amdahl-para-speedup-global-mejorando]]
