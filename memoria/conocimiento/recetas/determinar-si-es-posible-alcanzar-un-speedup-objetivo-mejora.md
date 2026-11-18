---
tipo: "receta"
titulo: "Determinar si es posible alcanzar un speedup objetivo mejorando solo un tipo de instrucción (Ejercicio 22b)"
temas: ["ac", "ley-amdahl", "rendimiento", "saltos"]
claves: ["speedup objetivo", "instrucciones salto", "límite mejora"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema1-Introduccion/Tema1 2026-27.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[ley-amdahl]] · [[rendimiento]] · [[saltos]]

Para saber si se puede alcanzar un speedup global S mejorando solo un componente:
1. Calcular el tiempo actual de ese componente (Saltos: 30s en ambos programas)
2. El tiempo mínimo posible de ese componente es 0 (mejora infinita)
3. Tiempo total mínimo = tiempo_total_original - tiempo_componente
4. Speedup máximo posible = tiempo_total_original / tiempo_total_mínimo

Prog A: Total 200s, Saltos 30s → Mínimo 170s → Speedup máx = 200/170 = 1.176 (17.6%) < 20% → NO
Prog B: Total 210s, Saltos 30s → Mínimo 180s → Speedup máx = 210/180 = 1.167 (16.7%) < 20% → NO
Conclusión: No es posible reducir el tiempo total un 20% mejorando solo saltos, ya que su peso en el total es insuficiente.

> b) ¿Podemos reducir el tiempo total un 20% mejorando solamente los saltos?
> — `repo:datos/temarios/AC/Tema1-Introduccion/Tema1 2026-27.pdf`

Relacionado: [[calculo-de-reduccion-de-tiempo-total-al-mejorar-un-tipo-de-i]] · [[limitacion-de-mejora-en-fraccion-pequena-ley-de-amdahl]] · [[speedup-por-ley-de-amdahl-con-mejora-10x-usada-20-del-tiempo]]
