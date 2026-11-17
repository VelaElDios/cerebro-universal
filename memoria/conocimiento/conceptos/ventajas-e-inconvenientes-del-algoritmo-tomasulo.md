---
tipo: "concepto"
titulo: "Ventajas e inconvenientes del algoritmo Tomasulo"
temas: ["ac", "planificacion-dinamica", "tomasulo"]
claves: ["cuello botella registros", "riesgos WAR WAW", "desenrollamiento hardware", "predicción saltos", "complejidad hardware", "almacenamientos asociados", "CDB"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[planificacion-dinamica]] · [[tomasulo]]

Resumen de características clave de Tomasulo frente a planificación estática y al marcador:
Ventajas:
1. Elimina el cuello de botella de los registros mediante renombrado implícito (estaciones de reserva y CDB).
2. Evita riesgos WAR (Write After Read) y WAW (Write After Write) gracias al renombrado y a la emisión en orden con ejecución fuera de orden.
3. Permite desenrollamiento de bucles en hardware (dynamic loop unrolling) al permitir múltiples instancias de la misma instrucción en vuelo.
4. No está limitado a bloques básicos si se combina con predicción de saltos.
Inconvenientes:
1. Mayor complejidad de hardware (estaciones de reserva, CDB, lógica de emisión/arbitraje).
2. Requiere muchos almacenamientos asociativos (CAM) por ciclo para la broadcast por CDB y la comparación de etiquetas (Qi).
3. El bus de datos común (CDB) se convierte en cuello de botella de ancho de banda al escalar el número de unidades funcionales.

> • Elimina el cuello de botella de los registros  • Evita riesgos WAR y WAW  • Permite el desenrollamiento en hardware  • No está limitado a bloques básicos (con predicción de saltos)  • Mayor complejidad hardware  • Muchos almacenamientos asociados por ciclo  • CDB limita el rendimiento
> — `repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf`

Relacionado: [[algoritmo-tomasulo-origen-y-objetivo-cpi1]]
