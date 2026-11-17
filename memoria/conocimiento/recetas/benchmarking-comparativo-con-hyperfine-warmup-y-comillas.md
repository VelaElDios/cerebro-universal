---
tipo: "receta"
titulo: "Benchmarking comparativo con Hyperfine (warmup y comillas)"
temas: ["ac", "benchmarking", "hyperfine"]
claves: ["hyperfine", "--warmup", "comillas", "sudo apt install hyperfine"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Practica4.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[benchmarking]] · [[hyperfine]]

Hyperfine ejecuta benchmarks estadísticos. Instalar con `sudo apt install hyperfine`. Uso típico: `hyperfine --warmup 3 './ejecutable_A' './ejecutable_B'`. El `--warmup 3` descarta las 3 primeras ejecuciones (calentamiento de cachés/TLB). **Importante**: usar comillas simples alrededor de cada comando para que Hyperfine los trate como unidades; sin comillas, la shell expande argumentos y rompe la medición.

> Hyperfine: Herramienta de benchmarking comparativo con soporte estadístico. Instalación: sudo apt install hyperfine Uso rápido: hyperfine --warmup 3 './ejecutable_A' './ejecutable_B' TEN CUIDADO: Asegúrate de hacer un uso correcto de las comillas.
> — `repo:datos/temarios/AC/Practicas/Practica4.pdf` (cita sin comprobar)

Relacionado: [[calentamiento-warm-up-para-poblar-tlb-y-evitar-page-faults]] · [[mapeo-de-patrones-de-acceso-en-el-grafico-roofline]]
