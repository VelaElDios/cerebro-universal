---
tipo: "dato"
titulo: "Tabla de latencias para instrucciones consecutivas en MIPS64 FP"
temas: ["ac", "latencia", "pipeline"]
claves: ["ALU PF", "S.D", "L.D", "latencia", "forwarding"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June 2024.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[latencia]] · [[pipeline]]

Latencias en ciclos cuando las instrucciones se ejecutan consecutivamente (con forwarding): 1) ALU PF (unidad FP) produciendo resultado para otra ALU PF: 3 ciclos. 2) ALU PF produciendo para S.D (almacenamiento FP): 2 ciclos. 3) L.D (carga FP) produciendo para ALU PF: 1 ciclo. Las instrucciones no listadas no tienen latencia (0 ciclos). Estas latencias determinan los huecos (stalls) necesarios en planificación estática o dinámica.

> Instruction that produces the result Instruction that uses the result Latency in cycles ALU PF ALU PF 3 ALU PF S.D 2 L.D ALU PF 1
> — `repo:datos/temarios/AC/examenes/June 2024.pdf`

Relacionado: [[tabla-de-latencias-entre-instrucciones-productoras-y-consumi]] · [[como-calcular-stalls-en-pipeline-mips64-con-operand-forwardi]] · [[latencias-de-unidades-funcionales-fp-en-examen-ac-june-2020]]
