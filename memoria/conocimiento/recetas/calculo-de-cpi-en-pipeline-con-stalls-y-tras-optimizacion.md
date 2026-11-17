---
tipo: "receta"
titulo: "Cálculo de CPI en pipeline con stalls y tras optimización"
temas: ["ac", "cpi", "pipeline", "rendimiento"]
claves: ["CPI", "ciclos por instrucción", "stalls", "burbujas", "estado estacionario", "start-up finish-up"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3_Prob.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[cpi]] · [[pipeline]] · [[rendimiento]]

Definición usada en el temario: **CPI = Ciclos totales / Instrucciones ejecutadas** (o CPR = Ciclos Por Instrucción, mismo concepto).
Metodología:
1. **Código original**: Dibujar *pipeline timing diagram* para varias iteraciones hasta alcanzar estado estacionario (patrón repetitivo).
   - Contar ciclos de una iteración completa en estado estacionario (desde IF de I1 iteración i hasta IF de I1 iteración i+1).
   - CPI = ciclos_iteración / num_instrucciones_por_iteración.
   - Incluir stalls (burbujas --) como ciclos extra.
2. **Código con segmentación software / desenrollado**:
   - Generar código transformado (con start-up + loop body + finish-up).
   - Dibujar timing del *loop body* desenrollado/planificado en estado estacionario.
   - CPI_optimizado = ciclos_cuerpo_estado_estacionario / (instrucciones_útiles_en_ese_cuerpo).
   - Start-up y finish-up se amortizan en bucles largos (n→∞), no cuentan para CPI teórico.
Ejemplo típico: Bucle 6 instrucciones, 2 stalls/iter → 8 ciclos/iter → CPI = 8/6 = 1.33. Tras desenrollar 2x y planificar sin stalls → 12 instrucciones en 12 ciclos → CPI = 1.0.

> Calcula el CPI del código." / "Calcula el CPI del código obtenido tras aplicar la segmentación software." / "Indica detenciones que se producen al ejecutar el código y calcula el CPR" / "Calcula el CPR que se obtiene con el nuevo código (con desenrollamiento).
> — `repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3_Prob.pdf` (cita sin comprobar)

Relacionado: [[parametros-estandar-para-ejercicios-de-segmentacion-software]] · [[desenrollamiento-de-bucle-minimo-para-eliminar-detenciones-e]]
