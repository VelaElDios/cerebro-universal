---
tipo: "receta"
titulo: "CPI con penalización de saltos resueltos en ID (test AC Q13)"
temas: ["ac", "cpi", "pipeline", "prediccion-saltos"]
claves: ["penalizacion-salto", "ID-stage", "branch-taken", "IPC"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2025.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[cpi]] · [[pipeline]] · [[prediccion-saltos]]

Si el salto se resuelve en la etapa ID (etapa 2), la instrucción siguiente ya se ha cogido en IF (etapa 1). Cuando el salto es tomado, hay que anular la instrucción en IF y coger el destino → **penalización = 1 ciclo por salto tomado**.
- Frecuencia de saltos tomados = 3/10 = 0.3.
- CPI base = 1 (pipeline ideal).
- CPI = `1 + (frecuencia_tomados × penalización) = 1 + 0.3×1 = 1.3`.
- IPC = `1 / CPI = 1 / 1.3 ≈ 0.77`.
Opción correcta: CPI = 1.3, IPC = 0.77.

> Dado un pipeline de 5 etapas en el que los saltos condicionales se resuelven en ID y en el que 3 de cada 10 instrucciones son saltos tomados, indica cuál de las siguientes opciones es la correcta:
> — `repo:datos/temarios/AC/examenes/Enero2025.pdf`
