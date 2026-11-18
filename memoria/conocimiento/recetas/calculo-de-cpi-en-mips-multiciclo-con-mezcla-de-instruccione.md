---
tipo: "receta"
titulo: "Cálculo de CPI en MIPS multiciclo con mezcla de instrucciones dada"
temas: ["ac", "cpi", "pipeline"]
claves: ["CPI", "multiciclo", "MIPS", "mezcla instrucciones", "ciclos por instrucción"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2014.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[cpi]] · [[pipeline]]

CPI = Σ (fracción_i × ciclos_i) = 0.25×5 + 0.20×4 + 0.30×4 + 0.15×3 + 0.10×3 = 1.25 + 0.80 + 1.20 + 0.45 + 0.30 = 4.0 ciclos/instrucción. La respuesta correcta es 4 ciclos por instrucción (opción c).

> El CPI en una implementación multiciclo del MIPS para un programa con esta mezcla de instrucciones: 25% carga(5 ciclos), 20% almacenamiento(4 ciclos), 30% tipoR(4 ciclos), 15%salto condicional(3 ciclos) y 10% saltos incondicional (3 ciclos), es:
> — `repo:datos/temarios/AC/examenes/Junio2014.pdf`

Relacionado: [[analisis-de-dependencias-en-bucle-con-add-d-y-s-d-misma-iter]] · [[banco-de-registros-en-pipeline-mips-se-accede-en-etapas-id-y]]
