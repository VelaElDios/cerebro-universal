---
tipo: "decision"
titulo: "Verificación de corrección mediante checksum idéntico en las cuatro variantes"
temas: ["ac", "testing", "validacion"]
claves: ["checksum", "s1==s2==s3==s4", "branchless-correctness"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab4/tarea4_2_branchless.cpp"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[testing]] · [[validacion]]

El `main` ejecuta cuatro configuraciones y guarda sus sumas en `s1..s4`:
1. `sumar_con_salto(datos_desordenados)`
2. `sumar_con_salto(datos_ordenados)`
3. `sumar_sin_salto(datos_desordenados)`
4. `sumar_sin_salto(datos_ordenados)` (usa `datos` de nuevo, no `ordenados`; typo en variable `t_sin_salto_ordenado` pero dato es el mismo).
Si `s1 != s2 || s1 != s3 || s1 != s4` → aborta con error "DISCREPANCIA".
Garantiza que la optimización branchless no altera la semántica (suma de elementos ≥ 128).

> Las cuatro deben coincidir, o tu versión está mal.
> — `repo:datos/temarios/AC/Practicas/Code_Lab4/tarea4_2_branchless.cpp`

Relacionado: [[patron-temporal-localidad-temporal-maxima-reutilizando-un-bl]] · [[pointer-chasing-en-std-list-vs-acceso-contiguo-en-std-vector]] · [[por-que-el-orden-de-los-datos-afecta-al-codigo-con-salto-per]] · [[patron-branchless-suma-condicional-mediante-multiplicacion-p]] · [[verificacion-de-correccion-numerica-entre-version-base-y-opt]]
