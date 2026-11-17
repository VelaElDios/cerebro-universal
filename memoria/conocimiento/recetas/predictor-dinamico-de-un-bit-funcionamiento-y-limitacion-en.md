---
tipo: "receta"
titulo: "Predictor dinámico de un bit: funcionamiento y limitación en bucles anidados"
temas: ["ac", "arquitectura", "bucle-anidado", "maquina-estados", "prediccion-saltos", "predictor-1-bit"]
claves: ["predictor 1 bit", "bit predicción", "máquina dos estados", "registro historia", "contador saturado", "bucle anidado", "mala predicción", "cambio dirección"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[arquitectura]] · [[bucle-anidado]] · [[maquina-estados]] · [[prediccion-saltos]] · [[predictor-1-bit]]

Funcionamiento: un bit por salto condicional. Estados: 0 = predice "no tomado" (NT), 1 = predice "tomado" (T). Transiciones: si salto real = T → estado 1; si salto real = NT → estado 0. La predicción es el valor actual del bit. Limitación: solo recuerda la última ejecución. En bucles anidados, el salto del bucle interno se predice mal dos veces por iteración del bucle externo: al entrar (predice NT, real T) y al salir (predice T, real NT). Ejemplo del texto: bucle externo e interno; en cada iteración externa, el salto interno falla al entrar (predice NT, es T) y al salir (predice T, es NT). Esto motiva predictores de 2 bits (contador saturado) que requieren dos fallos consecutivos para cambiar de predicción.

> Usa un bit de predicción por cada instrucción de salto – El bit refleja el comportamiento de la última ejecución, es decir, si el salto fue tomado o no tomado la última vez – IDEA: Si un salto fue efectivo es probable que vuelva a serlo – Máquina de dos estados – no tomado (0) – tomado (1) – Registro de historia – contador saturado de 1 bit – Predicción – valor del registro de historia – Limitación – Sólo se registra el comportamiento de la ejecución del salto – Dos malas predicciones en los cambios
> — `repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4.pdf` (cita sin comprobar)
