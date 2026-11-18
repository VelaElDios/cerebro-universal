---
tipo: "receta"
titulo: "Cálculo de CPI base en pipeline con penalización por saltos sin BTB"
temas: ["ac", "pipeline", "prediccion-saltos"]
claves: ["CPI", "pipeline 5 etapas", "salto condicional", "salto incondicional", "penalización", "frecuencia saltos"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2016.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]] · [[prediccion-saltos]]

Para calcular CPI base sin predicción (o predicción siempre-no-tomado): CPI = 1 + Σ(frecuencia_tipo_salto × penalización_tipo_salto). Penalización = ciclos perdidos cuando el salto es tomado y la dirección se conoce tarde. En pipeline 5 etapas IF/ID/EX/MEM/WB: salto condicional resuelve dirección en MEM → si tomado, se pierden 3 ciclos (IF, ID, EX de instrucciones siguientes ya fetchadas). Salto incondicional resuelve dirección en ID → si tomado, se pierden 1 ciclo (IF de siguiente). Frecuencias dadas: condicionales 30% (0.30), incondicionales 9% (0.09). De condicionales, 75% tomados. CPI_base = 1 + (0.30 × 0.75 × 3) + (0.09 × 1) = 1 + 0.675 + 0.09 = 1.765.

> Tenemos un procesador segmentado con 5 etapas IF, ID, EX, MEM y WB, donde para una instrucción de salto condicional la dirección del salto es conocida al final de la etapa MEM y el sentido al final de la etapa EX, y para una instrucción de salto incondicional la dirección del salto es conocida al final de la etapa ID.
> — `repo:datos/temarios/AC/examenes/Junio2016.pdf`

Relacionado: [[accion-del-procesador-ante-fallo-de-prediccion-de-salto]] · [[alternativas-de-deteccion-de-instruccion-de-salto-en-pipelin]]
