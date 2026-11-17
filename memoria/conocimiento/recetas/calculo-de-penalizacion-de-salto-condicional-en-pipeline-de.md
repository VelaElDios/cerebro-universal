---
tipo: "receta"
titulo: "Cálculo de penalización de salto condicional en pipeline de 5 etapas"
temas: ["ac", "cpi", "penalización", "pipeline"]
claves: ["sentido EX dirección MEM 3 ciclos", "sentido ID dirección ID 1 ciclo", "sentido EX dirección ID 2 ciclos"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[cpi]] · [[penalización]] · [[pipeline]]

Pasos para calcular la penalización (huecos de retardo) asumiendo que el cauce se detiene durante la latencia: 1) Identificar en qué etapa se resuelve la **condición** (sentido: tomado/no tomado). 2) Identificar en qué etapa se calcula la **dirección destino** (target address). 3) La penalización en ciclos = max(etapa_sentido, etapa_dirección) - etapa_IF (que es 1). En pipeline clásico de 5 etapas (IF=1, ID=2, EX=3, MEM=4, WB=5): - Si sentido en EX (3) y dirección en MEM (4) → max(3,4)-1 = 3 ciclos. - Si ambos en ID (2) → max(2,2)-1 = 1 ciclo. - Si sentido en EX (3) y dirección en ID (2) → max(3,2)-1 = 2 ciclos. Ejemplo numérico del texto: 6 instrucciones (1 salto tomado cada 6) con 2 ciclos de retardo → 8 ciclos totales → CPI real = 8/6 = 1,33 (rendimiento 0,75 inst/ciclo, 25% degradación).

> Para una segmentación de 5 etapas (IF, ID, EX, MEM, WB) las penalizaciones son: Sentido Salto EX, Dir. salto MEM, Penalización 3 Ciclos; Sentido Salto ID, Dir. salto ID, Penalización 1 Ciclos; Sentido Salto EX, Dir. salto ID, Penalización 2 Ciclos
> — `repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4.pdf` (cita sin comprobar)

Relacionado: [[definicion-de-latencia-de-salto-y-huecos-de-retardo]]
