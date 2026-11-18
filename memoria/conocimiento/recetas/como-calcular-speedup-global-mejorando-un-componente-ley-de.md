---
tipo: "receta"
titulo: "Cómo calcular speedup global mejorando un componente (Ley de Amdahl)"
temas: ["ac", "benchmark", "rendimiento"]
claves: ["Amdahl", "speedup", "fracción mejorada", "tiempo ejecución"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2025.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[benchmark]] · [[rendimiento]]

Aplicar ley de Amdahl: Speedup_global = 1 / ((1 - f) + f/k), donde f = fracción de tiempo en la parte mejorada (96s/120s = 0.8), k = factor de mejora de esa parte. Se busca Speedup_global = 5. Despejar k: 5 = 1 / (0.2 + 0.8/k) → 0.2 + 0.8/k = 0.2 → 0.8/k = 0 → imposible. Por tanto, respuesta correcta: «Es imposible» (opción d). La fracción no mejorada (20%) limita el speedup máximo a 5x aunque la multiplicación sea infinitamente rápida.

> Supongamos que un programa tarda en ejecutarse en una máquina 2 minutos, de los cuales 96 segundos corresponden a operaciones de multiplicar. ¿Cuánto tengo que mejorar la velocidad de multiplicación si quiero que el programa se ejecute cinco veces más rápido?
> — `repo:datos/temarios/AC/examenes/Junio2025.pdf`

Relacionado: [[analisis-de-dependencias-en-bucle-con-add-d-y-s-d-misma-iter]] · [[algoritmo-tomasulo-origen-y-objetivo-cpi1]] · [[calculo-de-speedup-con-ley-de-amdahl-en-pregunta-de-examen]] · [[ejercicio-de-participacion-en-clase-mejora-de-multiplicacion]] · [[calculo-de-mejora-necesaria-con-ley-de-amdahl-ejemplo-multip]]
