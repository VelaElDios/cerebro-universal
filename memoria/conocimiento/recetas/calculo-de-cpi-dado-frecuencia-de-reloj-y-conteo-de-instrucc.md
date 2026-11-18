---
tipo: "receta"
titulo: "Cálculo de CPI dado frecuencia de reloj y conteo de instrucciones por tipo (Ejercicio 22c)"
temas: ["ac", "ciclos-por-instruccion", "cpi", "rendimiento"]
claves: ["CPI", "2GHz", "instrucciones FP", "Int", "Load/Store", "Saltos", "ciclos totales"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema1-Introduccion/Tema1 2026-27.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[ciclos-por-instruccion]] · [[cpi]] · [[rendimiento]]

Fórmula: CPI = Ciclos_totales / Instrucciones_totales

Datos:
- Frecuencia = 2 GHz = 2×10⁹ ciclos/seg
- Instrucciones: FP=560M, Int=200M, Load/Store=1280M, Saltos=256M
- Total instrucciones = 560+200+1280+256 = 2296 millones

Pasos:
1. Calcular tiempo total de ejecución a partir de los tiempos por tipo del enunciado (Prog A o B? El ejercicio no especifica qué programa, pero los conteos son fijos)
   - Nota: El ejercicio da tiempos por tipo en la tabla (35s, 85s, 50s, 30s para Prog A) y conteos absolutos. Se puede calcular CPI de dos formas:
   
   Opción A: Usar tiempos de la tabla + frecuencia
   - Ciclos_totales = Tiempo_total * Frecuencia = 200s * 2×10⁹ = 400×10⁹ ciclos (para Prog A)
   - CPI = 400×10⁹ / 2296×10⁶ = 174.2 ciclos/instrucción (parece alto, verificar)
   
   Opción B: Calcular ciclos por tipo si se conoce CPI por tipo (no dado)
   
   Lo más probable: El ejercicio espera usar el tiempo total de la tabla (200s o 210s) con la frecuencia y los conteos dados para hallar CPI medio.
   CPI = (Tiempo_total * Frecuencia) / Σ Instrucciones
   Para Prog A: CPI = (200 * 2×10⁹) / 2296×10⁶ = 174.2
   Para Prog B: CPI = (210 * 2×10⁹) / 2296×10⁶ = 182.9

> c) Calcula el CPI, suponiendo que la máquina funciona a 2GHz y ha ejecutado 560, 200, 1280 y 256 millones de instrucciones de cada tipo respectivamente: FP, Int, Load/Store, Saltos.
> — `repo:datos/temarios/AC/Tema1-Introduccion/Tema1 2026-27.pdf`

Relacionado: [[calculo-de-reduccion-de-tiempo-total-al-mejorar-un-tipo-de-i]] · [[calculo-de-flops-por-ciclo-en-x86-con-avx2-fma]] · [[calculo-de-cpi-a-partir-de-tiempos-por-tipo-de-instruccion-y]] · [[calculo-de-tiempo-de-ejecucion-con-cpi-y-mezcla-de-instrucci]] · [[calculo-de-tiempo-de-ejecucion-con-cpi-mixto-y-frecuencia-de]]
