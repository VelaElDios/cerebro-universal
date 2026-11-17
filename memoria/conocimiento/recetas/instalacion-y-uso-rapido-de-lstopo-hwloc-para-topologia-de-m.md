---
tipo: "receta"
titulo: "Instalación y uso rápido de lstopo (hwloc) para topología de memoria"
temas: ["ac", "hwloc", "profiling"]
claves: ["lstopo", "hwloc", "sudo apt install hwloc", "lstopo -v"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Practica4.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[hwloc]] · [[profiling]]

lstopo (del paquete hwloc) muestra la jerarquía de memoria (cachés, NUMA) y la topología de E/S. Instalar con `sudo apt install hwloc` y ejecutar `lstopo -v` para salida detallada. Útil antes de benchmarks para conocer la arquitectura del nodo.

> lstopo (hwloc): Visualiza la jerarquía de memoria y topología de I/O. Instalación: sudo apt install hwloc Uso rápido: lstopo -v
> — `repo:datos/temarios/AC/Practicas/Practica4.pdf` (cita sin comprobar)

Relacionado: [[aos-vs-soa-desperdicio-de-ancho-de-banda-en-cache]] · [[mapeo-de-patrones-de-acceso-en-el-grafico-roofline]]
