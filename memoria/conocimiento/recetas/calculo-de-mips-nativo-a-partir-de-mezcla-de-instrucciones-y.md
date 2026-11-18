---
tipo: "receta"
titulo: "Cálculo de MIPS nativo a partir de mezcla de instrucciones y CPI por tipo"
temas: ["ac", "mips", "rendimiento"]
claves: ["MIPS nativo", "frecuencia reloj", "ciclos por instrucción", "mezcla instrucciones"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2021.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[mips]] · [[rendimiento]]

Para obtener MIPS nativo: 1) Calcular CPI medio ponderado = Σ (%_tipo_i × ciclos_tipo_i). 2) MIPS = (Frecuencia_MHz) / CPI_medio. En el ejemplo: FP mul 10%×6=0,6; FP add 15%×4=0,6; FP div 5%×20=1,0; Int 70%×2=1,4 → CPI=3,6. Frecuencia=1000 MHz → MIPS=1000/3,6≈277,78 (opción a).

> The native MIPS value of this computer is: a) 277.78 b) 321.3 c) 211.1 d) None of the above
> — `repo:datos/temarios/AC/examenes/January2021.pdf`

Relacionado: [[calculo-de-mips-a-partir-de-frecuencia-cpi-por-tipo-y-mezcla]] · [[calculo-de-mips-con-cpi-ponderado-y-frecuencia-de-reloj]] · [[como-calcular-cpi-medio-y-mips-nativo-con-mezcla-de-instrucc]]
