---
tipo: "receta"
titulo: "Cálculo de CPI en procesador multiciclo con mezcla de instrucciones"
temas: ["ac", "pipeline", "rendimiento"]
claves: ["CPI", "multiciclo", "MIPS", "mezcla instrucciones", "ciclos por tipo"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Noviembre2013.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]] · [[rendimiento]]

Para calcular el CPI medio en un procesador multiciclo: CPI = Σ (fracción_i × ciclos_i). En el ejemplo: CPI = 0.20×5 + 0.25×4 + 0.35×4 + 0.10×3 + 0.10×3 = 1.0 + 1.0 + 1.4 + 0.3 + 0.3 = 4.0 ciclos/instrucción. La respuesta correcta es la opción c) 4.

> El CPI en una implementación multiciclo del MIPS, considerando un programa con la siguiente mezcla de instrucciones: 20% cargas (5 ciclos), 25% almacenamientos (4 ciclos), 35% tipo R (4 ciclos), 10% saltos condicionales (3 ciclos) y 10% saltos incondicionales (3 ciclos)
> — `repo:datos/temarios/AC/examenes/Noviembre2013.pdf`

Relacionado: [[calculo-de-operaciones-por-ciclo-ipc-en-planificacion-vliw-d]]
