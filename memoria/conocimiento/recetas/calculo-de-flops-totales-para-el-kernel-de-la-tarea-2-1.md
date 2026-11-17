---
tipo: "receta"
titulo: "Cálculo de FLOPs totales para el kernel de la tarea 2.1"
temas: ["ac", "flops", "practica3", "roofline"]
claves: ["Total_FLOPs", "N", "REPETICIONES", "4 operaciones"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Practica3.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[flops]] · [[practica3]] · [[roofline]]

Para el kernel concreto de la práctica (suma sobre un vector), los FLOPs totales son invariantes al patrón de acceso:
  Total_FLOPs = N * REPETICIONES * 4
Donde:
- N = número de elementos del vector
- REPETICIONES = 4 (fijo en el enunciado)
- 4 operaciones de punto flotante por iteración (sumas)
Esto permite comparar patrones aislando solo el efecto del tráfico de memoria.

> el número total de operaciones de punto flotante (FLOPs) en el código de la tarea 2.1 es idéntico en los tres patrones de acceso, ya que todos realizan exactamente las mismas sumas sobre el vector: Total_FLOPs= N * REPETICIONES = N * (4) operaciones
> — `repo:datos/temarios/AC/Practicas/Practica3.pdf`
