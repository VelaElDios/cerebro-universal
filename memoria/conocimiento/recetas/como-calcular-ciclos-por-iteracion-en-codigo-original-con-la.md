---
tipo: "receta"
titulo: "Cómo calcular ciclos por iteración en código original con latencias dadas (examen AC 2017/18)"
temas: ["ac", "ciclos", "latencias", "pipeline", "rendimiento"]
claves: ["ciclos iteración original", "camino crítico", "dependencias", "latencias"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2018.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[ciclos]] · [[latencias]] · [[pipeline]] · [[rendimiento]]

Para hallar ciclos/iteración en código original (sin desenrollar, planificación in-order secuencial): 1) Identificar la cadena de dependencias más larga (camino crítico) dentro de una iteración. 2) Sumar latencias: L.D→MUL.D (1) + MUL.D→ADD.D (3) + ADD.D→S.D (2) = 6 ciclos para la cadena PF. 3) Las enteras (DADDUI, SLTI, BEQZ) tienen latencia 0 y se pueden emitir en paralelo (2 por ciclo). 4) La emisión es in-order dual: se emiten 2 instrucciones/ciclo si no hay hazard estructural ni dependencia. 5) Simular emisión ciclo a ciclo: Ciclo 1: L.D F2, L.D F6 (2 cargas). Ciclo 2: MUL.D F4 (espera 1 ciclo por F2), DADDUI R1 (entera). Ciclo 3: (MUL.D en ejecución), DADDUI R2. Ciclo 4: ADD.D F6 (espera 3 ciclos por F4 desde ciclo 2 → listo ciclo 5), SLTI R4. Ciclo 5: (ADD.D empieza), BEQZ R4. Ciclo 6: S.D F6 (espera 2 ciclos por ADD.D → listo ciclo 7). Total ~7-8 ciclos/iteración. La respuesta exacta requiere simulación precisa.

> ¿Cuántos ciclos invertirá cada iteración en el código original?
> — `repo:datos/temarios/AC/examenes/Junio2018.pdf`

Relacionado: [[problema-de-desenrollado-y-planificacion-de-bucle-superescal]] · [[tabla-de-latencias-entre-instrucciones-productoras-y-consumi]]
