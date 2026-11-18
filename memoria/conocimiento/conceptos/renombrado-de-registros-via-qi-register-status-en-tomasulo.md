---
tipo: "concepto"
titulo: "Renombrado de registros vía Qi (Register Status) en Tomasulo"
temas: ["ac", "raw", "renombrado-registros", "tomasulo", "waw"]
claves: ["Qi", "f0", "f2", "f4", "f6", "f8", "f10", "f12", "Mult 1", "Suma 2", "Mult 2"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[raw]] · [[renombrado-registros]] · [[tomasulo]] · [[waw]]

La tabla Qi (Register Result Status) muestra qué unidad funcional producirá el valor de cada registro:
- Ciclo 7: f0←Mult1, f2←M(45+x3) [carga 2], f6←Suma2, f8←Suma1, f10←Mult2. f4 y f12 sin Qi (valores disponibles en registro arquitectónico).
- Ciclo 8: f6←M()-M() (resultado de Suma2 ya disponible), f8←M()-M() (Suma1 completó). f0, f2, f10 igual.
- Ciclos 9-13: Qi estable: f0←Mult1, f2←M(45+x3), f6←(M-M)+M() [resultado fadd], f8←M()-M() [resultado fsub], f10←Mult2. f4, f12 sin Qi.
- Resolución WAW en f6: la primera carga escribe en f6 (Qi=Suma2 en c7), pero fadd.d reutiliza f6 como destino; Tomasulo asigna Qi=Mult2? No, en c7 f6←Suma2, luego en c8 f6←M()-M() (valor listo), y fadd.d usa f6 como fuente (Vj/Vk) no como destino en Qi. El WAW se evita porque fadd.d escribe en estación de reserva Suma3 (no mostrada) y el registro f6 se actualiza vía CDB cuando Suma3 termina (c11).

> Estado de los registros                                      f0           f2          f4            f6         f8        f10          f12 Qi         Mult 1 M(45+x3)                     Suma 2 Suma 1           Mult 2
> — `repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf`

Relacionado: [[algoritmo-tomasulo-origen-y-objetivo-cpi1]] · [[buffers-de-carga-y-almacenamiento-en-tomasulo]] · [[renombrado-de-registros-via-qi-en-bucle-con-reuso-de-f0-f2-f]] · [[uso-de-qi-en-registros-flotantes-para-renombrado-dinamico-en]] · [[fichero-de-registros-con-campo-qi-en-tomasulo]]
