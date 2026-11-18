---
tipo: "receta"
titulo: "Volcado de ROB (Reorder Buffer) en ciclo de finalización de primera carga en Tomasulo especulativo"
temas: ["ac", "especulacion", "rob", "simulacion", "tomasulo"]
claves: ["ROB", "reorder buffer", "4 entradas", "estado instrucción", "destino", "valor", "ciclo finalización L.D"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2022.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[especulacion]] · [[rob]] · [[simulacion]] · [[tomasulo]]

En el ciclo exacto donde termina la 1ª L.D (Write Result completado), el ROB de 4 entradas muestra: cada entrada con campos: Nº Entrada, Ocupada (S/N), Instrucción, Estado (Ejecutando/Escribiendo/Completado), Destino (registro ROB# o Fx), Valor (valor real o tag ROB#). Las instrucciones posteriores a la L.D pueden estar en estados anteriores. La L.D completada tendrá Estado=Completado/Escribiendo, Valor=dato_cargado. Entradas vacías: Ocupada=N.

> Completa la tabla para mostrar el contenido del ROB (que sólo tiene 4 entradas) justo en el mismo ciclo en el que finaliza la primera instrucción L.D.
> — `repo:datos/temarios/AC/examenes/Enero2022.pdf`

Relacionado: [[simulacion-tomasulo-con-especulacion-parametros-clave-y-rest]] · [[configuracion-tomasulo-con-especulacion-para-examen-enero-20]]
