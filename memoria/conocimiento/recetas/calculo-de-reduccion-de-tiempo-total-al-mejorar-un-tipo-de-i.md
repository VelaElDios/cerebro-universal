---
tipo: "receta"
titulo: "Cálculo de reducción de tiempo total al mejorar un tipo de instrucción (Ejercicio 22)"
temas: ["ac", "ley-amdahl", "rendimiento"]
claves: ["tiempo ejecución", "coma flotante", "speedup", "porcentaje mejora"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema1-Introduccion/Tema1 2026-27.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[ley-amdahl]] · [[rendimiento]]

Para calcular la reducción del tiempo total al mejorar un tipo de instrucción:
1. Identificar el tiempo original de ese tipo (ej. FP: 35s en Prog A, 50s en Prog B)
2. Aplicar el porcentaje de mejora: tiempo_nuevo = tiempo_original * (1 - mejora)
3. Calcular nuevo tiempo total = suma de todos los tiempos con el tipo mejorado
4. Reducción = (tiempo_original_total - tiempo_nuevo_total) / tiempo_original_total * 100%

Ejemplo Prog A: FP 35s → 28s (20% menos). Total original 200s → nuevo 193s. Reducción = 3.5%
Ejemplo Prog B: FP 50s → 40s. Total original 210s → nuevo 200s. Reducción = 4.76%

> Un computador ejecuta los programas A y B empleando para cada tipo de instrucción los tiempos que se muestran en la tabla: Coma Flotante 35s/50s, Enteros 85s/80s, Load/Store 50s/50s, Saltos 30s/30s
> — `repo:datos/temarios/AC/Tema1-Introduccion/Tema1 2026-27.pdf` (cita sin comprobar)
