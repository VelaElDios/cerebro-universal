---
tipo: "concepto"
titulo: "Estado de buffers de carga/almacenamiento y estaciones de reserva en ejemplo Tomasulo"
temas: ["ac", "buffers", "estaciones-reserva", "tomasulo"]
claves: ["Carga 1", "Carga 2", "Carga 3", "Almac 1", "Almac 2", "Almac 3", "Suma 1", "Suma 2", "Suma 3", "Mult 1", "Mult 2", "Ocupada", "Direc", "Qi", "Op", "Vj", "Vk", "Qj", "Qk"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[buffers]] · [[estaciones-reserva]] · [[tomasulo]]

Instantánea del ciclo 16 del ejemplo:
Buffers de carga (3 entradas):
- Carga 1: libre (NO)
- Carga 2: libre (NO)
- Carga 3: ocupada (SI), dirección 64, Qi vacío (ya tiene el dato o no espera a ninguna unidad).
Buffers de almacenamiento (3 entradas):
- Almac 1: ocupada, dirección 80, Qi = M(80)*R() (espera resultado de memoria/registro).
- Almac 2: ocupada, dirección 72, Qi = M(72)*R() 4 (notación del temario: espera dato de multiplicación o memoria).
- Almac 3: libre (NO) en ciclo 16; en ciclo 17 pasa a ocupada con Qi = Mult 1.
Estaciones de reserva (3 sumas, 2 multiplicaciones):
- Suma 1, 2, 3: todas libres (NO).
- Mult 1: ocupada (SI), Op=Mult, Vj vacío, Vk = R(f2) (valor del registro f2 disponible), Qj vacío, Qk = Carga 3 (espera el resultado de la carga 3 para el otro operando).
- Mult 2: libre (NO).
Este estado refleja que la segunda fmul.d (emitida en ciclo 7) está en Mult 1 esperando el operando de Carga 3 (la fld del ciclo 6).

> Buffers de carga/almac.                                    Estaciones de reserva Nombre Ocupada Direc.          Qi                                         Nombre          Ocupada         Op                Vj         Vk         Qj      Qk Carga 1      NO Carga 2      NO                      Suma 1               NO Carga 3      SI       64             Suma 2               NO Almac 1      SI       80 M(80)*R()   Suma 3               NO Almac 2      SI       72 M(72)*R() 4 Mult 1               SI        Mult                 R(f2)      Carga 3 Almac 3      NO                      Mult 2               NO
> — `repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf`

Relacionado: [[buffers-de-carga-y-almacenamiento-en-tomasulo]] · [[estructura-de-una-estacion-de-reserva-en-tomasulo]] · [[diferencia-entre-buffers-de-carga-y-de-almacenamiento-en-la]]
