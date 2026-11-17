---
tipo: "decision"
titulo: "Suposición de cauce detenido durante huecos de retardo para cálculo de penalización"
temas: ["ac", "modelo", "penalización", "pipeline"]
claves: ["NOTA: Asume que durante los ciclos de retardo el cauce se detiene"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[modelo]] · [[penalización]] · [[pipeline]]

El modelo pedagógico usado en el temario para calcular penalizaciones asume que **el pipeline se para completamente (stall)** durante los ciclos de latencia del salto, en lugar de buscar técnicas como predicción, delay slots arquitectónicos o ejecución especulativa. Esto simplifica el análisis: la penalización en ciclos = número de burbujas insertadas = latencia medida en ciclos de reloj entre IF del salto y la etapa donde se conoce tanto dirección como sentido. En la práctica real, los procesadores modernos no detienen el cauce sino que predicen y ejecutan especulativamente.

> NOTA: Asume que durante los ciclos de retardo el cauce se detiene
> — `repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4.pdf`

Relacionado: [[calculo-de-penalizacion-de-salto-condicional-en-pipeline-de]]
