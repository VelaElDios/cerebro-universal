---
tipo: "concepto"
titulo: "Distinción entre Arquitectura (ISA) y Organización (Microarquitectura)"
temas: ["ac", "arquitectura", "isa", "microarquitectura"]
claves: ["ISA", "Instruction Set Architecture", "microarquitectura", "organización", "arquitectura"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema1-Introduccion/Tema1 2026-27.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[arquitectura]] · [[isa]] · [[microarquitectura]]

La **arquitectura** (ISA) es la interfaz entre hardware y software de bajo nivel: atributos visibles al programador que afectan a la ejecución del programa (repertorio de instrucciones, representación de datos, modos de direccionamiento, E/S). La **organización** (microarquitectura) son las unidades funcionales y sus interconexiones que implementan la ISA; incluye detalles transparentes al programador (señales de control, interfaces con periféricos, tecnología de memoria). Una misma arquitectura puede tener múltiples organizaciones (ej.: AMD Opteron e Intel Core i7 comparten ISA x86 pero distinta organización) y una organización puede realizarse con distinta tecnología (ej.: Intel Core i7 e Intel Xeon 7560).

> Se refiere a aquellos atributos del sistema que son visibles al programador, es decir, los que tienen un impacto directo sobre la ejecución de un programa
> — `repo:datos/temarios/AC/Tema1-Introduccion/Tema1 2026-27.pdf`

Relacionado: [[aos-vs-soa-desperdicio-de-ancho-de-banda-en-cache]] · [[calculo-de-flops-ciclo-para-avx2-con-fma]] · [[distincion-entre-arquitectura-organizacion-y-tecnologia-en-p]] · [[arquitectura-vs-organizacion-misma-arquitectura-implica-mism]] · [[definicion-de-arquitectura-de-computador-visible-al-programa]]
