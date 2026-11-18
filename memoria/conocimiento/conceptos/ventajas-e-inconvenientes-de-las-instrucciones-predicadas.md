---
tipo: "concepto"
titulo: "Ventajas e inconvenientes de las instrucciones predicadas"
temas: ["ac", "compilador", "ilp", "instrucciones-predicadas", "prediccion-saltos"]
claves: ["ventajas", "inconvenientes", "bloques básicos", "compilador", "recursos", "ancho de banda", "flujo control complejo"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[compilador]] · [[ilp]] · [[instrucciones-predicadas]] · [[prediccion-saltos]]

**Ventajas:**
1. Elimina saltos condicionales → elimina fallos de predicción y burbujas de pipeline.
2. Genera bloques básicos más grandes → el compilador tiene más libertad para reordenar instrucciones, hacer software pipelining, y explotar ILP.

**Inconvenientes:**
1. Cambia la ISA: añade registros predicados y versiones predicadas de instrucciones → complejidad en decode, issue, renombrado, writeback.
2. Instrucciones con predicado falso siguen consumiendo: fetch, decode, issue, unidades funcionales, ancho de banda de caché de instrucciones, puertos de registro.
3. Solo útil para estructuras `if-then-else` simples; bucles, switches, llamadas a función no se predicen bien.
4. Adopción real: la mayoría de ISAs (x86, ARM, RISC-V) tienen solo *algunas* instrucciones condicionales (mov, select); solo IA64/EPIC y algunas DSP/GPU tienen predicación generalizada.

> Ventajas: • Capaz de eliminar saltos (y la necesidad de predecirlos) • Bloques básicos más grandes (el compilador puede planificar mejor) Inconvenientes: • Afecta al conjunto de instrucciones y complica su ejecución • Las instrucciones descartadas consumen recursos y ancho de banda • Uso limitado si el control de flujo es más complejo que una simple alternativa • Muchas arquitecturas incluyen unas pocas instrucciones condicionales sencillas; solo unas pocas incluyen versiones condicionales de la mayoría de las instrucciones
> — `repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4.pdf` (cita sin comprobar)

Relacionado: [[instrucciones-predicadas-convertir-dependencias-de-control-e]] · [[ejemplo-de-transformacion-de-salto-a-instrucciones-predicada]] · [[salto-retardado-y-instrucciones-predicadas-como-alternativas]]
