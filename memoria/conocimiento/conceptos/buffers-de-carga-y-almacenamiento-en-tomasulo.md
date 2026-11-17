---
tipo: "concepto"
titulo: "Buffers de carga y almacenamiento en Tomasulo"
temas: ["ac", "arquitectura", "tomasulo"]
claves: ["buffer carga", "buffer almacenamiento", "load buffer", "store buffer"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[arquitectura]] · [[tomasulo]]

Los load buffers tienen campos: Nombre, Ocupada, Dirección (dirección efectiva calculada). Los store buffers añaden Qi (unidad funcional que producirá el dato a almacenar) y V (valor a almacenar cuando esté listo). Qi=0 indica que el valor ya está disponible en V.

> Buffer de carga Ocupado, indica cuándo está disponible el buffer debido a que se haya completado una carga allí asignada Buffers de carga Nombre Ocupada Dirección Carga 1 Carga 2 Carga 3 Carga 4 Carga 5
> — `repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf`

Relacionado: [[estructura-de-una-estacion-de-reserva-en-tomasulo]] · [[fichero-de-registros-con-campo-qi-en-tomasulo]]
