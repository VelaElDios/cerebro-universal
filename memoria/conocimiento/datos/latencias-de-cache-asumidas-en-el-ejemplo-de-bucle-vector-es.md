---
tipo: "dato"
titulo: "Latencias de caché asumidas en el ejemplo de bucle vector-escalar"
temas: ["ac", "cache", "latencia", "tomasulo"]
claves: ["fallo cache 8 ciclos", "acierto cache 4 ciclos", "multiplicación 4 ciclos"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[cache]] · [[latencia]] · [[tomasulo]]

En el ejemplo de bucle (página 113) se fijan las siguientes latencias para la simulación:
- Unidad de multiplicación (fmul.d): **4 ciclos** de ejecución.
- Primera carga (fld f0, 0(x1)): **8 ciclos** por fallo en caché (miss).
- Segunda carga (siguiente iteración): **4 ciclos** por acierto en caché (hit).
Estos valores determinan la duración de la fase "Ejecución" en la tabla de estado de instrucciones y el tiempo que las estaciones de reserva permanecen ocupadas.

> Multiplicación: 4 ciclos 1ª carga: 8 ciclos (fallo en cache) 2ª carga: 4 ciclos (acierto)
> — `repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf`

Relacionado: [[algoritmo-tomasulo-origen-y-objetivo-cpi1]] · [[latencias-asumidas-para-carga-2-ciclos-y-multiplicacion-fp-3]] · [[latencias-de-unidades-funcionales-en-el-ejemplo-tomasulo]] · [[estado-inicial-ciclo-1-de-un-bucle-vector-escalar-en-tomasul]]
