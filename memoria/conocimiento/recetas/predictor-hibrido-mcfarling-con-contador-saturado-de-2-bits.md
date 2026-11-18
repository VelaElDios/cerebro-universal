---
tipo: "receta"
titulo: "Predictor híbrido McFarling con contador saturado de 2 bits"
temas: ["ac", "hibrido", "mcfarling", "prediccion-saltos"]
claves: ["McFarling", "contador saturado 2 bits", "selector", "P1", "P2"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[hibrido]] · [[mcfarling]] · [[prediccion-saltos]]

Arquitectura híbrida de McFarling:
- Dos predictores componentes (P1 y P2).
- Un array de contadores saturados de 2 bits (uno por entrada de PC o global).
- Tras cada predicción: si P1 acierta y P2 falla → incrementar; si P1 falla y P2 acierta → decrementar; si ambos aciertan o ambos fallan → no cambia.
- El bit más significativo del contador (MSB) selecciona: 1 → usa P1; 0 → usa P2.
- Así el selector aprende qué predictor funciona mejor para cada contexto.

> McFarling: emplea un contador saturado de 2 bits para seleccionar entre dos predictores
> — `repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4.pdf`

Relacionado: [[tabla-de-actualizacion-de-contadores-de-2-bits-saturados-par]] · [[predictor-hibrido-con-selector-de-2-bits-entre-predictor-de]] · [[selector-de-2-bits-para-predictor-hibrido-de-saltos]]
