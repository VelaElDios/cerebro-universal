---
tipo: "dato"
titulo: "Evolución del registro base x1 y Qi de registros FP en el ejemplo Tomasulo"
temas: ["ac", "qi", "registros", "tomasulo"]
claves: ["x1", "f0", "f2", "f4", "f6", "f8", "f10", "f12", "Qi", "Carga 3", "Mult 1"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[qi]] · [[registros]] · [[tomasulo]]

Estado del registro base y del registro de estado de resultados (Qi) en ciclos 16-18:
- Registro base x1 = 64 (dirección base para las cargas/almacenamientos).
- Tabla Qi (qué unidad funcional escribirá en cada registro FP):
  - f0: Qi = Carga 3 (la segunda fld f0,0(x1) emitida en ciclo 6, en ejecución en Carga 3).
  - f2: Qi vacío (valor ya disponible, R(f2) usado en Mult 1).
  - f4: Qi = Mult 1 (la segunda fmul.d f4,f0,f2 emitida en ciclo 7, en Mult 1).
  - f6, f8, f10, f12: Qi vacíos.
En ciclo 19, x1 cambia a 56 (probablemente actualización del puntero de bucle tras la segunda iteración), manteniéndose en 56 en ciclo 20.

> Estado de los registros                                       f0            f2          f4            f6           f8       f10          f12       x1 = 64                          Qi        Carga 3                  Mult 1
> — `repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf`

Relacionado: [[estado-de-registros-resultado-register-result-status-en-el-m]] · [[escritura-de-resultado-y-actualizacion-de-qi-en-registro-des]]
