---
tipo: "receta"
titulo: "Qué mostrar en esquema hardware Tomasulo con especulación (parte a examen)"
temas: ["ac", "pipeline", "tomasulo"]
claves: ["esquema hardware Tomasulo especulacion", "ROB estaciones reserva buffer carga interconexion BDC"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2014.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]] · [[tomasulo]]

Para la parte a) del examen, el esquema debe incluir y conectar:
1. **Unidades Funcionales (UFs) segmentadas**: 3 UFs (suma/resta, multiplicación, división) cada una con su estación de reserva (2 entradas c/u).
2. **Buffer de Carga** (2 entradas) conectado a memoria/datos.
3. **ROB** (4 entradas) conectado al BDC (Bus Común de Datos).
4. **BDC** (Common Data Bus) que conecta salidas de UFs, buffer carga y ROB → entradas de estaciones de reserva, buffer carga y ROB.
5. **Banco de registros FP** con puerto de lectura para emisión y puerto de escritura desde ROB (terminación).
6. **Unidad de emisión/despacho** que renombra registros usando ROB y estaciones de reserva.

**Información en cada entrada ROB** (Tomasulo con especulación):
- Tipo instrucción (carga, almacenamiento, operación FP, salto, etc.)
- Registro destino (arquitectónico)
- Valor/resultado (cuando disponible)
- Estado: Emisión / Ejecución / Escritura resultado / Terminación (Commit)
- PC / dirección salto (para recuperación)
- Posible: máscara de excepciones, bits de predicción

**Información en cada entrada Estación de Reserva**:
- Op (operación a realizar)
- Qj, Qk: etiquetas (números ROB) de operandos fuente no disponibles
- Vj, Vk: valores de operandos fuente ya disponibles
- Busy: si la entrada está ocupada
- Destino: etiqueta ROB donde se escribirá resultado
- Posible: estado de la UF asociada

**Buffer de Carga** (similar a ER pero para cargas):
- Dirección efectiva (base + offset calculado)
- Q: etiqueta ROB del registro base si no disponible
- V: valor base si disponible
- Destino: etiqueta ROB del registro destino
- Busy

> Realiza un esquema con los componentes hardware del sistema mostrando su interconexión. Indica claramente la información almacenada en el ROB y las estaciones de reserva.
> — `repo:datos/temarios/AC/examenes/Junio2014.pdf`

Relacionado: [[buffer-de-reordenamiento-rob-en-tomasulo-con-especulacion-ca]] · [[buffers-de-carga-y-almacenamiento-en-tomasulo]] · [[algoritmo-tomasulo-los-resultados-se-difunden-por-el-bus-com]]
