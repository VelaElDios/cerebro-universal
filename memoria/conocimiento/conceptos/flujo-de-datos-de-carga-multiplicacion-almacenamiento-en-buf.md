---
tipo: "concepto"
titulo: "Flujo de datos de carga → multiplicación → almacenamiento en buffers Tomasulo"
temas: ["ac", "buffers", "flujo datos", "tomasulo"]
claves: ["Carga 1", "Carga 2", "Almac 1", "Almac 2", "Mult 1", "Mult 2", "Qi"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[buffers]] · [[flujo datos]] · [[tomasulo]]

El flujo de cada iteración:
1. Buffer de carga (Carga 1/2) se marca Ocupada=SI con la dirección efectiva (80/72) y Qi vacío (la carga no espera a nadie).
2. Estación Mult (Mult 1/2) se reserva con Qk apuntando al buffer de carga correspondiente.
3. Cuando la carga termina, su resultado viaja por el bus común (CDB) a Mult y al registro f0 (Qi se limpia).
4. Mult ejecuta y, al terminar, envía resultado a CDB → registro f4 y buffer de almacenamiento (Almac 1/2).
5. Buffer de almacenamiento (Almac 1/2) pasa a Ocupada=SI, dirección=80/72, Qi=Mult 1/2 (espera el dato de la multiplicación).
6. Cuando Mult escribe en CDB, Almac recibe el dato y puede hacer la escritura en memoria.

> Almac 1      SI       80        Mult 1
> — `repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf`

Relacionado: [[buffers-de-carga-y-almacenamiento-en-tomasulo]] · [[asignacion-de-estaciones-de-reserva-mult-1-y-mult-2-en-el-ej]]
