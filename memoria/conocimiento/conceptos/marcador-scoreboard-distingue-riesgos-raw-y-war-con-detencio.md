---
tipo: "concepto"
titulo: "Marcador (Scoreboard) distingue riesgos RAW y WAR con detenciones opuestas"
temas: ["ac", "marcador", "planificacion-dinamica", "riesgos-raw-war", "scoreboard"]
claves: ["RAW fsub.d espera fmul.d", "WAR fadd.d espera fsub.d", "detención escritura vs lectura", "2 UF mul", "2 UF add"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3_Prob.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[marcador]] · [[planificacion-dinamica]] · [[riesgos-raw-war]] · [[scoreboard]]

En el fragmento: fmul.d f0,f6,f4 (S1); fsub.d f8,f0,f2 (S2) -> RAW en f0: S2 lee f0 escrito por S1. Marcador detiene S2 en lectura operandos hasta que S1 escribe resultado. fadd.d f2,f10,f2 (S3) -> WAR en f2: S3 escribe f2 que S2 lee como operando fuente. Marcador detiene S3 en emisión/escritura hasta que S2 ha leído f2 (inicia ejecución). Así, RAW frena al consumidor; WAR frena al productor. Con 2 UF mul (4 ciclos) y 2 UF add/sub (1 ciclo), el marcador gestiona disponibilidad de UF y registro destino (Qj/Qk). Situación pedida: solo fadd.d ha completado ejecución -> mostrar estado de instrucciones, UF, registros (Qi, busy).

> Es crítico que el marcador sea capaz de distinguir riesgos RAW y WAR puesto que los segundos requieren la detención de la instrucción que va a escribir hasta que la instrucción que lee inicia la ejecución, y los primeros requieren detener la instrucción que lee hasta que termina la instrucción que escribe (es decir, justo lo contrario).
> — `repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3_Prob.pdf`

Relacionado: [[deteccion-de-riesgos-war-y-waw-en-marcador-y-bloqueo-de-escr]] · [[tecnica-de-marcador-scoreboard-riesgos-war-waw-obligan-a-det]] · [[completar-tabla-marcador-con-uf-mul-7c-add-5c-div-15c-ejerci]]
