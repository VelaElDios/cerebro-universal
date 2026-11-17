---
tipo: "dato"
titulo: "Tamaño del vector y bloque en bytes y líneas de caché"
temas: ["ac", "cache", "lineas", "memoria"]
claves: ["512 MB", "32 KiB", "64 bytes", "8 int64_t", "línea de caché"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab3/tarea2_1_patrones.cpp"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[cache]] · [[lineas]] · [[memoria]]

Vector total = 2^26 * 8 bytes = 512 MiB. Bloque = 4096 * 8 bytes = 32 KiB (típico tamaño L1 data cache por core). Línea de caché = 64 bytes = 8 int64_t contiguos. Secuencial: 1 fallo cada 8 accesos (ideal). Temporal: ~4096/8 = 512 fallos L1 en primera pasada, luego 0. Aleatorio: ~1 fallo por acceso.

> constexpr std::size_t N = 1ull << 26;        // 2^26= 64M elementos (de tipo int64)\n                                             // Un int64 ocupa 8 bytes --> total= 64M*8= 512 MB\n//Valor del bloque\nconstexpr std::size_t BLOQUE = 4096;         // bloque pequeño: cabe de sobra en L1
> — `repo:datos/temarios/AC/Practicas/Code_Lab3/tarea2_1_patrones.cpp` (cita sin comprobar)
