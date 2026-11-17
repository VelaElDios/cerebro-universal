---
tipo: "receta"
titulo: "Speedup combinado de mejoras independientes en fracciones disjuntas (ejercicio 13)"
temas: ["ac", "arquitectura-computadores", "ley-amdahl", "mejoras-multiples"]
claves: ["speedup combinado", "multiplicación", "acceso memoria", "mejoras simultáneas"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema1-Introduccion/Tema1_ProbSol.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[arquitectura-computadores]] · [[ley-amdahl]] · [[mejoras-multiples]]

Cuando mejoras afectan a fracciones disjuntas del tiempo (f1, f2, ... f_restante=1-Σfi) con factores k1, k2...: T_nuevo = Σ (fi*T/k_i) + f_restante*T. Speedup = T / T_nuevo = 1 / (Σ fi/k_i + f_restante). Ejercicio: f_mult=0.2 (k=4), f_mem=0.5 (k=2), f_otras=0.3 (k=1). Speedup_mult=1/(0.2/4+0.8)=1.18; Speedup_mem=1/(0.5/2+0.5)=1.33; Combinado=1/(0.2/4+0.5/2+0.3)=1/0.6=1.67.

> Si combinamos ambas mejoras, tenemos: speedup = 100 / (20/4 + 50/2 + 30) = 100/60 = 1.67
> — `repo:datos/temarios/AC/Tema1-Introduccion/Tema1_ProbSol.pdf` (cita sin comprobar)

Relacionado: [[seleccion-de-mejoras-mutuamente-excluyentes-con-ley-de-amdah]]
