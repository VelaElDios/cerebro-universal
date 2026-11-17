---
tipo: "dato"
titulo: "Configuración de recursos en ejercicio Tomasulo (Ej. 14) y Scoreboard (Ej. 16)"
temas: ["ac", "buffers", "estaciones-reserva", "recursos", "scoreboard", "tomasulo"]
claves: ["2 estaciones por UF", "1 buffer carga", "1 buffer almacenamiento", "UF suma/resta mul"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3_Prob.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[buffers]] · [[estaciones-reserva]] · [[recursos]] · [[scoreboard]] · [[tomasulo]]

**Ejercicio 14 (Tomasulo clásico con buffers limitados)**:
- UF: 1 Suma/Resta (lat 2), 1 Multiplicador (lat 4).
- Estaciones reserva: 2 por UF → **Suma1, Suma2** y **Mul1, Mul2**.
- Buffers: **1 Load Buffer (LD1)**, **1 Store Buffer (ST1)**.
- Instrucciones: fld f2, fld f12, fmul.d f4 f2 f2, fadd.d f2 f2 f12, fsub.d f8 f4 f2, fsd f8.
- Restricciones extra: "En mismo ciclo no se puede escribir en BDC e iniciar ejecución esperando ese dato", "Recurso liberado en T usable en T+1".

**Ejercicio 16 (Scoreboard vs Tomasulo básico, sin buffers explícitos)**:
- UF: latencias fadd/fsub=2, fmul=5, fld/fsd=1.
- Supuesto: "No hay riesgos estructurales que afecten a UF, estaciones de reserva o buffers de carga" → recursos ilimitados / no son cuellos de botella.
- Instrucciones: fadd.d f0 f2 f4, fld f2 12(x2), fsub.d f6 f0 f2, fmul.d f4 f3 f2, fadd.d f6 f4 f6, fsd f4 10(x2).
- Diferencia clave: Scoreboard usa renombrado de registros *no* (WAW/WAR detienen), Tomasulo sí (estaciones reserva renombran).

> Hay dos estaciones de reserva por UF, un buffer da carga y 1 buffer de almacenamiento." / "No hay riesgos estructurales que afecten a las unidades funcionales, a las estaciones de reserva o a los buffers de carga.
> — `repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3_Prob.pdf` (cita sin comprobar)

Relacionado: [[algoritmo-de-tomasulo-reglas-de-simulacion-para-ejercicios-d]] · [[algoritmo-de-marcador-scoreboard-pasos-de-simulacion-para-ej]]
