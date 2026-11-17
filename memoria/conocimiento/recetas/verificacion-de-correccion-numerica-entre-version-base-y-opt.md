---
tipo: "receta"
titulo: "Verificación de corrección numérica entre versión base y optimizada ILP"
temas: ["ac", "floating-point", "testing", "verificacion"]
claves: ["verification", "correctness", "floating point equality", "sum comparison"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab4/tarea4_1_ilp.cpp"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[floating-point]] · [[testing]] · [[verificacion]]

**Requisito estricto**: La suma final debe ser **idéntica bit a bit** entre versión base y optimizada.

**Por qué se cumple aquí**:
- Operación: suma de valores positivos idénticos (1.0)
- Orden de evaluación: versión base suma secuencialmente; versión optimizada suma en 4 bloques contiguos y luego combina
- **Asociatividad de punto flotante**: `(a+b)+c ≠ a+(b+c)` en general, pero aquí **sí coincide** porque:
  1. Todos los operandos son exactamente 1.0 (representable exacto en binary64)
  2. Sumas parciales son enteros exactos (1.0, 2.0, 3.0... hasta 25M) → representables exactos en double (53 bits mantisa cubre hasta 2^53 ≈ 9×10^15)
  3. Suma final de 4 enteros exactos → exacta

**Cómo verificar**:
```bash
./ilp_base   # Anota suma (ej: 100000000.000000)
./ilp_opt    # Debe imprimir exactamente lo mismo
```

**Si no coincide**: Bug en índices del unrolling (off-by-one, orden incorrecto de acumuladores). Usar `printf("%.15f\n", sumA)` para ver dígitos completos.

> Ambas implementaciones deben obtener exactamente el mismo resultado.
> — `repo:datos/temarios/AC/Practicas/Code_Lab4/tarea4_1_ilp.cpp`

Relacionado: [[optimizacion-ilp-mediante-desenrollado-de-bucle-con-4-acumul]]
