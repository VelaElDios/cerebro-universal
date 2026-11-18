---
tipo: "decision"
titulo: "Latencias asumidas para carga (2 ciclos) y multiplicación FP (3 ciclos) en el ejemplo docente"
temas: ["ac", "carga", "configuracion", "latencia", "multiplicacion", "tomasulo"]
claves: ["latencia carga", "latencia multiplicacion", "ciclos ejecucion"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[carga]] · [[configuracion]] · [[latencia]] · [[multiplicacion]] · [[tomasulo]]

De la traza se infieren las latencias configuradas en el simulador docente:
- Carga (fld): emisión en ciclo 1, ejecución ciclos 2-3, escritura resultado en ciclo 4 → **latencia 2 ciclos de ejecución + 1 de escritura = 3 ciclos totales desde emisión**.
- Multiplicación double (fmul.d): emisión en ciclo 2, ejecución ciclos 3-5, escritura en ciclo 6 → **latencia 3 ciclos de ejecución + 1 de escritura = 4 ciclos totales desde emisión**.
- Almacenamiento (fsd): emisión en ciclo 3, espera dato hasta ciclo 6, escritura en ciclo 8 → su latencia propia es 1 ciclo pero se retrasa por dependencia RAW con fmul.d.

> fld       f0, 0(x1)                        1                           fmul.d    f4, f0, f2                       2
> — `repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf`

Relacionado: [[latencia-de-carga-fp-y-multiplicacion-doble-en-la-simulacion]] · [[latencias-de-unidades-funcionales-en-el-ejemplo-tomasulo]] · [[secuencia-de-instrucciones-y-latencias-en-ejemplo-tomasulo-c]]
