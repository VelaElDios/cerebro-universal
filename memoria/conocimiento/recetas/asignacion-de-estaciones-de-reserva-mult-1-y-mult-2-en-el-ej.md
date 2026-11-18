---
tipo: "receta"
titulo: "Asignación de estaciones de reserva Mult 1 y Mult 2 en el ejemplo"
temas: ["ac", "estaciones reserva", "multiplicacion", "tomasulo"]
claves: ["Mult 1", "Mult 2", "Vj", "Vk", "Qj", "Qk", "R(f2)", "Carga 1", "Carga 2"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[estaciones reserva]] · [[multiplicacion]] · [[tomasulo]]

En la tabla «Estaciones de reserva», las filas Mult 1 y Mult 2 muestran:
- Mult 1 (ciclo 2): Ocupada=SI, Op=Mult, Vj=R(f2) (valor de f2 listo), Vk=vacío, Qj=vacío, Qk=Carga 1 (espera el resultado de la carga 1 para f0).
- Mult 2 (ciclo 7): Ocupada=SI, Op=Mult, Vj=R(f2), Qk=Carga 2 (espera la segunda carga).
La notación `R(f2)` indica que el operando j (f2) está disponible en el banco de registros; `Carga 1`/`Carga 2` en Qk indica que el operando k (f0) llegará desde ese buffer de carga.

> Mult 1          SI        Mult                         R(f2)   Carga 1
> — `repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf`

Relacionado: [[buffers-de-carga-y-almacenamiento-en-tomasulo]] · [[algoritmo-tomasulo-origen-y-objetivo-cpi1]] · [[como-evoluciona-la-tabla-de-estaciones-de-reserva-en-tomasul]] · [[eleccion-de-dos-estaciones-de-multiplicacion-mult-1-y-mult-2]] · [[convencion-de-nomenclatura-en-tablas-de-tomasulo-del-temario]]
